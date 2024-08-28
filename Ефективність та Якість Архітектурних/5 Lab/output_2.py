# output_1.py

class Product:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

class ProductSearch:
    def search_product(self, products, query):
        # Пошук товару за запитом
        results = [product for product in products if query.lower() in product.name.lower()]
        return results

class ProductDisplay:
    def display_product(self, product):
        # Відображення інформації про товар
        print(f"Product Name: {product.name}")
        print(f"Product Price: {product.price}")
        print(f"Product Type: {product.type}")

class ProductOrder:
    def order_product(self, product, quantity):
        # Замовлення товару
        print(f"Ordered {quantity} of {product.name}")
        # Тут може бути додана логіка для зменшення кількості на складі, тощо

# Приклад використання класів
if __name__ == "__main__":
    products = [
        Product("Laptop", 1200, "Electronics"),
        Product("Smartphone", 800, "Electronics"),
        Product("Shirt", 40, "Clothing")
    ]

    search = ProductSearch()
    display = ProductDisplay()
    order = ProductOrder()

    query = "Laptop"
    results = search.search_product(products, query)
    
    for product in results:
        display.display_product(product)
        order.order_product(product, 2)
