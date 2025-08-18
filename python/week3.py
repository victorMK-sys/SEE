original_price = float(input("Enter original price of your item: $"))
discount_price = float(input("Enter discount of the item: "))

def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    price = price - (price * discount_percent / 100)
  
  return price

print(f"Item price: {calculate_discount(original_price, discount_price):.2f}")