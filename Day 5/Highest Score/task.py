student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# total_score=sum(student_scores)
# print(total_score)
# Highest_marks=max(student_scores)
# print(Highest_marks)
max_score=0
for scores in student_scores:
    if scores>max_score:
        max_score=scores
print(max_score)


