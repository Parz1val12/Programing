# MCCC Snack Bar Receipt
# Calculates the subtotal, tax, and total for one customer order.

TAX_RATE = 0.07

# Input
customer_name = input("Customer name: ")
item = input("Item: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

# Processing
subtotal = price * quantity
tax = subtotal * TAX_RATE
total = subtotal + tax

# Output
print()
print(f"--- Receipt for {customer_name} ---")
print(f"Item:      {item}")
print(f"Quantity:  {quantity}")
print(f"Subtotal:  ${subtotal:.2f}")
print(f"Tax (7%):  ${tax:.2f}")
print(f"Total:     ${total:.2f}")