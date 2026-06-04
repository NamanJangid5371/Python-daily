Student_Score = {
    "Maths":85,
    "Science":92,
    "History":78,
    "Englis":88
}

Scores_only = Student_Score.values()

total_score = sum(Scores_only)

no_of_subject = len(Scores_only)

average = total_score/no_of_subject

print(f"Student average score {average:.1f}")

if average>=80:
    print("Studetn is Pass!")
else:
    print("Student is fale.")