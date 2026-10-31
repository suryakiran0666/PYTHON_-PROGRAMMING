1. Problem Statement
Calculate railway fares for multiple passengers based on distance, travel class, age concessions, reservation fees, and cancellation penalties.
2. Algorithm
1. Read the number of passengers.
2. Input age, distance, class, and cancellation status for each passenger.
3. Calculate base fare and apply age concessions.
4. Add reservation fee and apply cancellation penalty.
5. Display each passenger's fare and total amount.
3. Flowchart:-(Mermaid):
4. 
flowchart TD
    A([Start]) --> B[/Input number of passengers/]
    B --> C[/Input age, distance, class, cancellation/]
    C --> D[Calculate base fare]
    D --> E[Apply age concession]
    E --> F[Add reservation fee]
    F --> G{Cancelled?}
    G -- Yes --> H[Apply cancellation penalty]
    G -- No --> I[Calculate final fare]
    H --> I
    I --> J[/Display passenger fare/]
    J --> K{More passengers?}
    K -- Yes --> C
    K -- No --> L[/Display total fare/]
    L --> M([End])

Distance (km): 100
Class (S/A): S
Cancelled (y/n): n
Age: 30
Distance (km): 100
Class (S/A): A
Cancelled (y/n): y
6. Sample Output
Fare: 140.0
Fare: 210.0
Total fare: 350.0
Note: The fare rates, reservation fee, age concessions, and cancellation rules are illustrative values for this program, not official railway rules.












Do you like this personality?
