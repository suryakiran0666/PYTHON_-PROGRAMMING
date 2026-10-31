1. Problem Statement
Develop a Python program to calculate bills for multiple products using quantities, category-specific taxes, threshold discounts, and maximum discount limits. Generate an itemized invoice.
2. Algorithm
1. Input the number of products.
2. Enter product name, category, price, and quantity.
3. Calculate subtotal and category-specific tax.
4. Apply threshold discounts with a maximum limit.
5. Display the itemized invoice and final bill.
3. Flowchart:(Mermaid):

flowchart TD
    A([Start]) --> B[/Input number of products/]
    B --> C[/Input product details/]
    C --> D[Calculate subtotal]
    D --> E[Apply category tax]
    E --> F{Subtotal >= 1000?}
    F -- Yes --> G[Calculate discount]
    F -- No --> H[Discount = 0]
    G --> I[Limit discount to maximum]
    H --> J[Calculate final bill]
    I --> J
    J --> K[/Display invoice/]
    K --> L([End])

5. Sample Input
Number of products: 2
Product: Rice
Category (F/E): F
Price: 500
Quantity: 2
Product: Headphones
Category (F/E): E
Price: 1000
Quantity: 1
6. Sample Output
Rice Amount: 1000.0 Tax: 50.0
Headphones Amount: 1000.0 Tax: 180.0
Subtotal: 2000.0
Tax: 230.0
Discount: 200.0
Final Bill: 2030.0


Note: Tax rates, discount thresholds, and the maximum discount are illustrative values for this Python exercise, not official tax rules.
