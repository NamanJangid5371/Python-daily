score = []

for i in range[1,11]:
    s = int(input(f"Enter the score of match {i}:"))
    score.append(s)

print("Total Score:",sum(score))
print("The average score:",sum(score)/len(score))
print("Highest score:",max(score))
if score>50:
    