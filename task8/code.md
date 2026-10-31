1. Problem Statement
Calculate manufacturing cost, wastage, revenue, and profit, then check whether the profit target is achieved.
2. Algorithm
1. Input costs, selling price, quantity, and target.
2. Calculate total cost and profit.
3. Check the profit target and display the result.
3. Flowchart:(Mermaid):
flowchart TD
A([Start]) --> B[/Input costs and target/]
B --> C[Calculate total cost and profit]
C --> D{Profit >= Target?}
D -- Yes --> E[/Target Achieved/]
D -- No --> F[/Target Not Achieved/]
E --> G([End])
F --> G
5. Sample Input
Material cost: 500
Labour cost: 100
Wastage %: 10
Machine cost: 50
Selling price per item: 800
Quantity: 2
Profit target: 200
6. Sample Output
Total Cost: 1300.0
Profit: 300.0
Target Achieved
