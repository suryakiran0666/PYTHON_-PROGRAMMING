1. Problem Statement
Evaluate students based on aggregate marks, subject-wise minimum marks, attendance, and family income. Rank eligible students and resolve ties using attendance.
2. Algorithm
1. Input student details and eligibility criteria.
2. Check subject marks, attendance, and income.
3. Select eligible students.
4. Rank by aggregate marks; use attendance to break ties.
5. Display the ranked list.
6. flow chart:(mermaid):
7. 
flowchart TD
    A([Start]) --> B[/Input student details/]
    B --> C{Meets all criteria?}
    C -- Yes --> D[Add to eligible list]
    C -- No --> E[Reject applicant]
    D --> F{More students?}
    E --> F
    F -- Yes --> B
    F -- No --> G[Rank by marks and attendance]
    G --> H[/Display ranking/]
    H --> I([End])
. Sample Input
Number of students: 2
Name: Ravi
Aggregate marks: 85
Minimum subject marks: 70
Attendance %: 90
Family income: 150000
Name: Sita
Aggregate marks: 85
Minimum subject marks: 65
Attendance %: 95
Family income: 180000
6. Sample Output
Scholarship Ranking:
1 Sita 85.0 95.0
2 Ravi 85.0 90.0
