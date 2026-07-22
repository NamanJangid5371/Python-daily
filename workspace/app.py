import streamlit as st
from pathlib import Path
from datetime import datetime

# ----------------------------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="FileDesk | File Handling System",
    page_icon="📁",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------------
# CUSTOM STYLING
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
        html, body, [class*="css"] { font-family: 'Segoe UI', sans-serif; }

        .main-title {
            font-size: 2.4rem;
            font-weight: 800;
            background: linear-gradient(90deg, #4F46E5, #06B6D4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0;
        }
        .sub-title {
            color: #6B7280;
            font-size: 1rem;
            margin-top: 0.2rem;
            margin-bottom: 1.5rem;
        }

        .stat-card {
            background: #ffffff;
            border-radius: 14px;
            padding: 18px 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.06);
            border: 1px solid #EEF0F3;
            text-align: center;
        }
        .stat-value { font-size: 1.6rem; font-weight: 700; color: #4F46E5; }
        .stat-label { font-size: 0.85rem; color: #6B7280; }

        div[data-testid="stForm"] {
            background: #ffffff;
            padding: 24px;
            border-radius: 16px;
            border: 1px solid #EEF0F3;
            box-shadow: 0 2px 12px rgba(0,0,0,0.05);
        }

        .stButton>button {
            border-radius: 10px;
            font-weight: 600;
            padding: 0.5rem 1.2rem;
            border: none;
            background: linear-gradient(90deg, #4F46E5, #06B6D4);
            color: white;
            transition: 0.2s;
        }
        .stButton>button:hover {
            opacity: 0.9;
            transform: translateY(-1px);
        }

        section[data-testid="stSidebar"] {
            background: #111827;
        }
        section[data-testid="stSidebar"] * {
            color: #F3F4F6 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# WORKSPACE SETUP
# All file operations are sandboxed inside a local "workspace" folder so the
# app is safe to demo (won't touch the rest of your system).
# ----------------------------------------------------------------------------
WORKSPACE = Path("workspace")
WORKSPACE.mkdir(exist_ok=True)

if "message" not in st.session_state:
    st.session_state.message = None  # (type, text)


def flash(msg_type, text):
    st.session_state.message = (msg_type, text)


def show_flash():
    if st.session_state.message:
        msg_type, text = st.session_state.message
        getattr(st, msg_type)(text)
        st.session_state.message = None


def human_size(num_bytes):
    for unit in ["B", "KB", "MB", "GB"]:
        if num_bytes < 1024:
            return f"{num_bytes:.1f} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.1f} TB"


# ----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# ----------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## 📁 FileDesk")
    st.caption("A simple file management console")
    st.markdown("---")
    page = st.radio(
        "Navigate",
        ["🏠 Dashboard", "📝 Create", "📖 Read", "✏️ Update", "🗑️ Delete"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption(f"Workspace: `{WORKSPACE.resolve().name}/`")
    st.caption("Built with Python + Streamlit")

# ----------------------------------------------------------------------------
# HEADER
# ----------------------------------------------------------------------------
st.markdown('<p class="main-title">File Handling System</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-title">Create, read, update and delete files — all from one clean dashboard.</p>',
    unsafe_allow_html=True,
)

files = sorted([f for f in WORKSPACE.iterdir() if f.is_file()])

# ----------------------------------------------------------------------------
# DASHBOARD
# ----------------------------------------------------------------------------
if page == "🏠 Dashboard":
    total_size = sum(f.stat().st_size for f in files)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f'<div class="stat-card"><div class="stat-value">{len(files)}</div>'
            f'<div class="stat-label">Total Files</div></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<div class="stat-card"><div class="stat-value">{human_size(total_size)}</div>'
            f'<div class="stat-label">Storage Used</div></div>',
            unsafe_allow_html=True,
        )
    with c3:
        last_modified = (
            datetime.fromtimestamp(max(f.stat().st_mtime for f in files)).strftime("%d %b, %H:%M")
            if files
            else "—"
        )
        st.markdown(
            f'<div class="stat-card"><div class="stat-value">{last_modified}</div>'
            f'<div class="stat-label">Last Modified</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("###  ")
    st.subheader("📂 Files in workspace")

    if not files:
        st.info("No files yet. Head to **Create** to add your first file.")
    else:
        for f in files:
            stat = f.stat()
            col1, col2, col3 = st.columns([5, 2, 2])
            col1.write(f"**{f.name}**")
            col2.write(human_size(stat.st_size))
            col3.write(datetime.fromtimestamp(stat.st_mtime).strftime("%d %b %Y, %H:%M"))
        st.divider()

# ----------------------------------------------------------------------------
# CREATE
# ----------------------------------------------------------------------------
elif page == "📝 Create":
    st.subheader("Create a new file")
    show_flash()

    with st.form("create_form", clear_on_submit=True):
        name = st.text_input("File name", placeholder="e.g. notes.txt")
        content = st.text_area("File content", height=200, placeholder="Write something...")
        submitted = st.form_submit_button("🚀 Create File")

    if submitted:
        if not name.strip():
            flash("error", "Please enter a file name.")
        else:
            path = WORKSPACE / name
            if path.exists():
                flash("error", f"⚠️ '{name}' already exists.")
            else:
                try:
                    path.write_text(content)
                    flash("success", f"✅ '{name}' created successfully.")
                except Exception as err:
                    flash("error", f"An error occurred: {err}")
        st.rerun()

# ----------------------------------------------------------------------------
# READ
# ----------------------------------------------------------------------------
elif page == "📖 Read":
    st.subheader("Read a file")
    show_flash()

    if not files:
        st.info("No files available to read. Create one first.")
    else:
        chosen = st.selectbox("Choose a file", [f.name for f in files])
        if chosen:
            path = WORKSPACE / chosen
            try:
                content = path.read_text()
                st.code(content if content.strip() else "(this file is empty)", language=None)
                st.download_button("⬇️ Download this file", data=content, file_name=chosen)
            except Exception as err:
                st.error(f"An error occurred: {err}")

# ----------------------------------------------------------------------------
# UPDATE
# ----------------------------------------------------------------------------
elif page == "✏️ Update":
    st.subheader("Update a file")
    show_flash()

    if not files:
        st.info("No files available to update. Create one first.")
    else:
        chosen = st.selectbox("Choose a file", [f.name for f in files])
        path = WORKSPACE / chosen if chosen else None

        operation = st.radio(
            "What would you like to do?",
            ["Rename", "Append content", "Overwrite content"],
            horizontal=True,
        )

        if operation == "Rename":
            with st.form("rename_form"):
                new_name = st.text_input("New file name")
                go = st.form_submit_button("✏️ Rename")
            if go and path:
                new_path = WORKSPACE / new_name
                if not new_name.strip():
                    flash("error", "Please enter a new name.")
                elif new_path.exists():
                    flash("error", f"⚠️ '{new_name}' already exists.")
                else:
                    try:
                        path.rename(new_path)
                        flash("success", f"✅ Renamed to '{new_name}'.")
                    except Exception as err:
                        flash("error", f"An error occurred: {err}")
                st.rerun()

        elif operation == "Append content":
            with st.form("append_form"):
                data = st.text_area("Text to append", height=150)
                go = st.form_submit_button("➕ Append")
            if go and path:
                try:
                    with open(path, "a") as fs:
                        fs.write("\n" + data)
                    flash("success", f"✅ Content appended to '{chosen}'.")
                except Exception as err:
                    flash("error", f"An error occurred: {err}")
                st.rerun()

        elif operation == "Overwrite content":
            current = path.read_text() if path and path.exists() else ""
            with st.form("overwrite_form"):
                data = st.text_area("New content (replaces everything)", value=current, height=200)
                go = st.form_submit_button("♻️ Overwrite")
            if go and path:
                try:
                    path.write_text(data)
                    flash("success", f"✅ '{chosen}' overwritten successfully.")
                except Exception as err:
                    flash("error", f"An error occurred: {err}")
                st.rerun()

# ----------------------------------------------------------------------------
# DELETE
# ----------------------------------------------------------------------------
elif page == "🗑️ Delete":
    st.subheader("Delete a file")
    show_flash()

    if not files:
        st.info("No files available to delete.")
    else:
        chosen = st.selectbox("Choose a file to delete", [f.name for f in files])
        st.warning(f"This will permanently delete **{chosen}**.")
        confirm = st.checkbox("I understand this cannot be undone.")
        if st.button("🗑️ Delete File", disabled=not confirm):
            try:
                (WORKSPACE / chosen).unlink()
                flash("success", f"✅ '{chosen}' deleted successfully.")
            except Exception as err:
                flash("error", f"An error occurred: {err}")
            st.rerun()