1. Problem Statement
Calculate electricity bills using consumption slabs, fixed charges, surcharges, and rebates. Compare monthly bills and identify unusual increases.
2. Algorithm
1. Input consumption for each month.
2. Calculate slab charges, fixed charges, and surcharge.
3. Apply rebate and calculate the final bill.
4. Compare bills and identify unusual increases.
5. flowchart:(meramid):
flowchart TD
    A([Start]) --> B[/Input monthly units/]
    B --> C[Calculate slab charges]
    C --> D[Add fixed charges and surcharge]
    D --> E[Apply rebate and calculate bill]
    E --> F{More months?}
    F -- Yes --> B
    F -- No --> G[Compare monthly bills]
    G --> H[/Display bills and unusual increases/]
    H --> I([End])

7. Sample Input
Units: 80
Units: 100
Units: 250
6. Sample Output
Bill: 197.4
Bill: 262.5
Bill: 892.5
Unusual increase in month 3
