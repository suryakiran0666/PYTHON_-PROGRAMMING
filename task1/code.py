students = []
n = int(input("Number of students: "))
for i in range(n):
    name = input("Name: ")
    marks = float(input("Aggregate marks: "))
    subject = float(input("Minimum subject marks: "))
    att = float(input("Attendance %: "))
    income = float(input("Family income: "))
    if marks >= 75 and subject >= 60 and att >= 75 and income <= 200000:
        students.append((name, marks, att))
students.sort(key=lambda x: (x[1], x[2]), reverse=True)
print("Scholarship Ranking:")
for rank, s in enumerate(students, 1):
    print(rank, s[0], s[1], s[2])
