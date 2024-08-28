# output_1.py

def calculate_total_price(product_prices, discount, tax_rate=0):
    total_price = 0
    for price in product_prices:
        if discount:
            total_price += price * 0.9  # 10% discount
        else:
            total_price += price
    if tax_rate:
        total_price *= (1 + tax_rate)
    return total_price

# Приклад використання функцій
product_prices = [100, 200, 300]
print("Total Price without tax:", calculate_total_price(product_prices, discount=True))
print("Total Price with tax:", calculate_total_price(product_prices, discount=True, tax_rate=0.05))
