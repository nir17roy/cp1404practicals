# shop_calculator.py (while version)

number_of_items = int(input("Number of items: "))
total_price = 0
item_count = 0

while item_count < number_of_items:
    price = float(input("Price of item: "))
    total_price += price
    item_count += 1

if total_price > 100:
    total_price *= 0.9  # Apply 10% discount

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
