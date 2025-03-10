student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total = 0
maxx = student_scores[0]

for score in student_scores:
    if maxx < score:
        maxx = score

for i in range(1,101):
    total += i
    if i == 100:
        print(total)

# print(maxx)
