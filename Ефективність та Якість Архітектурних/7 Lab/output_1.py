# output_1.py

class Product:
    def __init__(self, product_id, name, category, price):
        self.__product_id = product_id  # Приватне поле
        self.__name = name  # Приватне поле
        self.__category = category  # Приватне поле
        self.__price = price  # Приватне поле

    # Геттери для доступу до приватних полів
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_price(self):
        return self.__price

    # Сеттер для зміни ціни
    def set_price(self, new_price):
        self.__price = new_price


class InventoryManagement:
    def __init__(self, products):
        self.products = products

    def print_product_details(self, product_id):
        for product in self.products:
            if product.get_product_id() == product_id:
                print(f"Product ID: {product.get_product_id()}, Name: {product.get_name()}, Category: {product.get_category()}, Price: {product.get_price()}")


# Приклад використання класів
products = [
    Product(1, "Laptop", "Electronics", 1200),
    Product(2, "Smartphone", "Electronics", 800),
    Product(3, "Chair", "Furniture", 150)
]

inventory = InventoryManagement(products)
inventory.print_product_details(1)
inventory.print_product_details(2)
