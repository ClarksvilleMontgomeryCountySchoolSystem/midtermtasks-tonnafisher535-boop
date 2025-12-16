

# Testing flag - will be set by test
TESTING = True
item = None
price = None
quantity = None

print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"

   Prosperity comes in threes!
========================================

ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
""")
print(s.menu)


# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)
def get_purchase_info():
    item = float(input("Enter item name: ")
    price = float(input("Enter item prices: "))
    quantity = int(input("Enter quantity: "))
    return item, price, quantity

# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()

# TODO: Calculate subtotal, tax, and total
subtotal = price * quantity
# Tax rate: 9.5%
tax = subtotal *0.095
total = subtotal + tax

# TODO: Round total to 2 decimal places using round()
subtotal = round(subtotal, 2)

# TODO: Print receipt
print("--------------------------")
print(f"{item} x{quantity} @ ${price:.2f} each")
print("--------------------------")
# Print subtotal, tax, and total here
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
print("\nThank you for shopping at\nthe Peculiar Emporium!")#AFTER PASTING YOUR ANSWER YOU MUST REMOVE THE LINE "import s"
#YOUR CODE WILL FAIL IF YOU DO NOT DELETE THE LINE!!!!!!!!!!!!!
