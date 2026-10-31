1. Problem Statement
Evaluate multiple mobile plans based on usage, validity, and budget. Calculate excess usage charges and identify the most economical eligible plan.
2. Algorithm
1. Input budget, required data, and validity.
2. Enter the details of three mobile plans.
3. Calculate extra data charges and total cost.
4. Check budget, data, and validity constraints.
5. Display the cheapest eligible plan.
3. Flowchart :-(Mermaid)
4. 
flowchart TD
    A([Start]) --> B[/Input budget, data usage, validity/]
    B --> C[Initialize mobile plans]
    C --> D[Select a plan]
    D --> E[Calculate excess charges]
    E --> F[Calculate total cost]
    F --> G{Validity sufficient and cost within budget?}
    G -- Yes --> H{Cheapest eligible plan?}
    H -- Yes --> I[Update best plan]
    H -- No --> J{More plans?}
    I --> J
    G -- No --> J
    J -- Yes --> D
    J -- No --> K{Best plan exists?}
    K -- Yes --> L[/Display best plan and cost/]
    K -- No --> M[/Display No eligible plan/]
    L --> N([End])
    M --> N :

5. Sample Input
Enter budget: 300
Data required (GB): 2.5
Validity required (days): 28

6. Sample Output
Most Economical Plan: Basic
Excess Charges: 25.0
Total Cost: 224.0

Note: The mobile plan prices and excess charges are illustrative values for this program.
