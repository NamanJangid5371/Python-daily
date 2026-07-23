import json
from pathlib import Path
from datetime import datetime

import pandas as pd
import streamlit as st

# ----------------------------------------------------------------------------
# Config & data layer
# ----------------------------------------------------------------------------
DATABASE = "school_data.json"

st.set_page_config(
    page_title="School Manager",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)


def load_data():
    if Path(DATABASE).exists():
        with open(DATABASE, "r") as f:
            content = f.read()
            if content:
                return json.loads(content)
    return {"students": [], "teachers": []}


def save_data(data):
    with open(DATABASE, "w") as f:
        json.dump(data, f, indent=4)


if "data" not in st.session_state:
    st.session_state.data = load_data()

data = st.session_state.data


def validate_email(email: str) -> bool:
    return "@" in email and "." in email and " " not in email


def find_student(roll_no):
    return next((s for s in data["students"] if s["roll_no"] == roll_no), None)


def find_teacher(emp_id):
    return next((t for t in data["teachers"] if t["emp_id"] == emp_id), None)


# ----------------------------------------------------------------------------
# Styling
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .main > div { padding-top: 1.5rem; }
    .stat-card {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
        border-radius: 14px;
        padding: 1.1rem 1.3rem;
        color: white;
    }
    .stat-card h2 { margin: 0; font-size: 2rem; }
    .stat-card p { margin: 0; opacity: 0.85; font-size: 0.85rem; }
    .section-title {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
    }
    div[data-testid="stMetric"] {
        background-color: rgba(99, 102, 241, 0.08);
        border-radius: 12px;
        padding: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# Sidebar navigation
# ----------------------------------------------------------------------------
st.sidebar.title("🎓 School Manager")
page = st.sidebar.radio(
    "Navigate",
    [
        "📊 Dashboard",
        "🧑‍🎓 Register Student",
        "🧑‍🏫 Register Teacher",
        "📝 Add Grades",
        "🔍 Student Details",
        "🔍 Teacher Details",
        "📁 All Records",
    ],
)

st.sidebar.markdown("---")
st.sidebar.caption(f"Data file: `{DATABASE}`")
st.sidebar.caption(f"Students: {len(data['students'])} · Teachers: {len(data['teachers'])}")

# ----------------------------------------------------------------------------
# Dashboard
# ----------------------------------------------------------------------------
if page == "📊 Dashboard":
    st.title("📊 Dashboard")
    st.write("Overview of your school's records.")

    all_grades = [g for s in data["students"] for g in s.get("grades", {}).values()]
    avg_grade = sum(all_grades) / len(all_grades) if all_grades else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Students", len(data["students"]))
    c2.metric("Total Teachers", len(data["teachers"]))
    c3.metric("Grades Recorded", len(all_grades))
    c4.metric("Average Grade", f"{avg_grade:.1f}" if all_grades else "—")

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-title">🧑‍🎓 Recent Students</div>', unsafe_allow_html=True)
        if data["students"]:
            df = pd.DataFrame(data["students"])[["name", "roll_no", "age", "email"]]
            st.dataframe(df.tail(5), use_container_width=True, hide_index=True)
        else:
            st.info("No students registered yet.")

    with col2:
        st.markdown('<div class="section-title">🧑‍🏫 Recent Teachers</div>', unsafe_allow_html=True)
        if data["teachers"]:
            df = pd.DataFrame(data["teachers"])[["name", "subject", "emp_id", "email"]]
            st.dataframe(df.tail(5), use_container_width=True, hide_index=True)
        else:
            st.info("No teachers registered yet.")

# ----------------------------------------------------------------------------
# Register Student
# ----------------------------------------------------------------------------
elif page == "🧑‍🎓 Register Student":
    st.title("🧑‍🎓 Register a Student")

    with st.form("student_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full name")
            age = st.number_input("Age", min_value=3, max_value=100, step=1)
        with c2:
            email = st.text_input("Email")
            roll_no = st.text_input("Roll number")

        submitted = st.form_submit_button("Register Student", use_container_width=True)

        if submitted:
            if not name or not email or not roll_no:
                st.error("Please fill in all fields.")
            elif not validate_email(email):
                st.error("Invalid email address.")
            elif find_student(roll_no):
                st.error(f"A student with roll number '{roll_no}' already exists.")
            else:
                data["students"].append(
                    {
                        "name": name,
                        "age": int(age),
                        "email": email,
                        "roll_no": roll_no,
                        "grades": {},
                    }
                )
                save_data(data)
                st.success(f"Student '{name}' registered successfully! 🎉")

# ----------------------------------------------------------------------------
# Register Teacher
# ----------------------------------------------------------------------------
elif page == "🧑‍🏫 Register Teacher":
    st.title("🧑‍🏫 Register a Teacher")

    with st.form("teacher_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full name")
            age = st.number_input("Age", min_value=18, max_value=100, step=1)
            subject = st.text_input("Subject taught")
        with c2:
            email = st.text_input("Email")
            emp_id = st.text_input("Employee ID")

        submitted = st.form_submit_button("Register Teacher", use_container_width=True)

        if submitted:
            if not name or not email or not subject or not emp_id:
                st.error("Please fill in all fields.")
            elif not validate_email(email):
                st.error("Invalid email address.")
            elif find_teacher(emp_id):
                st.error(f"A teacher with employee ID '{emp_id}' already exists.")
            else:
                data["teachers"].append(
                    {
                        "name": name,
                        "age": int(age),
                        "email": email,
                        "subject": subject,
                        "emp_id": emp_id,
                    }
                )
                save_data(data)
                st.success(f"Teacher '{name}' registered successfully! 🎉")

# ----------------------------------------------------------------------------
# Add Grades
# ----------------------------------------------------------------------------
elif page == "📝 Add Grades":
    st.title("📝 Add Grades")

    if not data["students"]:
        st.info("No students registered yet. Register a student first.")
    else:
        options = {f"{s['name']} ({s['roll_no']})": s["roll_no"] for s in data["students"]}
        choice = st.selectbox("Select student", list(options.keys()))
        roll_no = options[choice]
        student = find_student(roll_no)

        with st.form("grade_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                subject = st.text_input("Subject")
            with c2:
                marks = st.number_input("Marks", min_value=0.0, max_value=100.0, step=0.5)

            submitted = st.form_submit_button("Add Grade", use_container_width=True)

            if submitted:
                if not subject:
                    st.error("Please enter a subject.")
                else:
                    student["grades"][subject] = marks
                    save_data(data)
                    st.success(f"Grade for '{subject}' added to {student['name']}'s record.")

        if student["grades"]:
            st.markdown("#### Current grades")
            gdf = pd.DataFrame(
                [{"Subject": k, "Marks": v} for k, v in student["grades"].items()]
            )
            st.dataframe(gdf, use_container_width=True, hide_index=True)
            avg = sum(student["grades"].values()) / len(student["grades"])
            st.metric("Average", f"{avg:.1f}")

# ----------------------------------------------------------------------------
# Student Details
# ----------------------------------------------------------------------------
elif page == "🔍 Student Details":
    st.title("🔍 Student Details")

    if not data["students"]:
        st.info("No students registered yet.")
    else:
        options = {f"{s['name']} ({s['roll_no']})": s["roll_no"] for s in data["students"]}
        choice = st.selectbox("Select student", list(options.keys()))
        s = find_student(options[choice])

        grades = s.get("grades", {})
        avg = sum(grades.values()) / len(grades) if grades else 0

        c1, c2, c3 = st.columns(3)
        c1.metric("Name", s["name"])
        c2.metric("Roll No", s["roll_no"])
        c3.metric("Average Grade", f"{avg:.1f}" if grades else "—")

        st.write(f"**Age:** {s['age']}  ·  **Email:** {s['email']}")

        st.markdown("#### Grades")
        if grades:
            gdf = pd.DataFrame([{"Subject": k, "Marks": v} for k, v in grades.items()])
            st.dataframe(gdf, use_container_width=True, hide_index=True)
        else:
            st.info("No grades recorded yet.")

# ----------------------------------------------------------------------------
# Teacher Details
# ----------------------------------------------------------------------------
elif page == "🔍 Teacher Details":
    st.title("🔍 Teacher Details")

    if not data["teachers"]:
        st.info("No teachers registered yet.")
    else:
        options = {f"{t['name']} ({t['emp_id']})": t["emp_id"] for t in data["teachers"]}
        choice = st.selectbox("Select teacher", list(options.keys()))
        t = find_teacher(options[choice])

        c1, c2, c3 = st.columns(3)
        c1.metric("Name", t["name"])
        c2.metric("Employee ID", t["emp_id"])
        c3.metric("Subject", t["subject"])

        st.write(f"**Age:** {t['age']}  ·  **Email:** {t['email']}")

# ----------------------------------------------------------------------------
# All Records
# ----------------------------------------------------------------------------
elif page == "📁 All Records":
    st.title("📁 All Records")

    tab1, tab2 = st.tabs(["Students", "Teachers"])

    with tab1:
        if data["students"]:
            rows = []
            for s in data["students"]:
                grades = s.get("grades", {})
                avg = sum(grades.values()) / len(grades) if grades else None
                rows.append(
                    {
                        "Name": s["name"],
                        "Roll No": s["roll_no"],
                        "Age": s["age"],
                        "Email": s["email"],
                        "Subjects Graded": len(grades),
                        "Average": round(avg, 1) if avg is not None else "—",
                    }
                )
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        else:
            st.info("No students registered yet.")

    with tab2:
        if data["teachers"]:
            df = pd.DataFrame(data["teachers"])[["name", "subject", "emp_id", "age", "email"]]
            df.columns = ["Name", "Subject", "Employee ID", "Age", "Email"]
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("No teachers registered yet.")

    st.markdown("---")
    st.caption(f"Last refreshed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")