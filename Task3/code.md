1. Problem Statement
Calculate consultation, diagnostic, and treatment charges. Apply concessions, validate the bill, and classify the patient's payment status.
2. Algorithm
1. Input consultation, diagnostic, and treatment charges.
2. Calculate the total and apply concessions.
3. Validate the payment amount.
4. Classify the payment status and display the bill.
5. flowchart:(meramid):
flowchart TD
    A([Start]) --> B[/Input charges and payment/]
    B --> C[Calculate total bill]
    C --> D{Eligible for concession?}
    D -- Yes --> E[Apply 10% discount]
    D -- No --> F[Keep original bill]
    E --> G[Calculate final bill]
    F --> G
    G --> H{Payment covers bill?}
    H -- Yes --> I[Paid]
    H -- No --> J[Pending]
    I --> K[/Display bill and status/]
    J --> K
    K --> L([End])
   Sample Input
Consultation: 1000
Diagnostics: 2000
Treatment: 3000
Payment: 5000
6. Sample Output
Final Bill: 5400.0
Pending: 400.0
