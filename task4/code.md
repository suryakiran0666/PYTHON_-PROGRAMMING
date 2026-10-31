. Problem Statement
Calculate an employee's gross salary using basic pay, allowances, overtime, and incentives. Apply progressive deductions and display the net salary.
2. Algorithm
1. Read basic pay, allowances, overtime, and incentives.
2. Calculate gross salary.
3. Calculate deductions using salary slabs.
4. Calculate net salary.
5. Display the salary statement.
3. Flowchart  ---(Mermaid)
 flowchart TD
    A([Start]) --> B[/Input salary details/]
    B --> C[Calculate gross salary]
    C --> D[Calculate deductions]
    D --> E[Calculate net salary]
    E --> F[/Display salary statement/]
    F --> G([End])
   ---
5. Sample Input
Basic pay: 25000
Allowances: 5000
Overtime: 2000
Incentives: 3000


6. Sample Output
--- SALARY STATEMENT ---
Gross Salary: 35000.0
Deduction: 2500.0
Net Salary: 32500.0


Note: The deduction slabs are illustrative examples for this program, not official tax rules.
