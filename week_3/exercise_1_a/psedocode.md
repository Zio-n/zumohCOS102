**Function:** Checkout(purchasedItems, paymentMethod)

  **Input:**
    * purchasedItems: List of items purchased by the customer
    * paymentMethod: String representing the payment method (e.g., "Cash", "Credit Card")

  **Output:**
    * None (performs actions related to checkout)

  **Steps:**
    1. Display order summary:
        * List of purchased items with quantity and price
        * Subtotal
        * Tax (if applicable)
        * Total amount due
    2. **If** paymentMethod is "Cash":
        * Prompt cashier for received cash amount
        * **While** received cash amount < total amount due:
            * Display message "Insufficient funds"
            * Prompt cashier for additional cash
            * Update received cash amount
        * **End While**
        * Calculate change amount: received cash amount - total amount due
        * Print receipt with purchased items, total amount, and change amount
        * Dispense change to customer
    3. **Else If** paymentMethod is "Credit Card":
        * Prompt cashier to swipe credit card
        * Simulate credit card processing (communicate with payment gateway - not shown here)
        * **If** credit card processing is successful:
            * Print receipt with purchased items, total amount, and payment method
        * **Else**
            * Display message "Credit card processing failed"
    4. **End If**
    5. Update inventory for purchased items (reduce stock levels)
    6. Thank the customer for their purchase