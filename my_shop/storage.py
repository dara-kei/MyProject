from product import Product
import json
from datetime import datetime


class Storage:
    def __init__(self):
        self._products = {}
        self._sales = []

    def get_sales(self):
        return self._sales

    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity)
        if name not in self._products:
            self._products[name] = new_product
        else:
            raise ValueError(f"Product with name {name} already exists")

    def get_product(self, name):
        if name in self._products:
            return self._products[name]
        else:
            raise ValueError(f"Product with name {name} does not exist")

    def restock_product(self, name, quantity):
        product = self._products.get(name)
        if product is None:
            raise ValueError(f"Product with name {name} does not exist")
        if quantity <= 0:
            raise ValueError("Restock quantity must be positive")
        product.change_quantity(quantity)

    def remove_product(self, name):
        product = self._products.get(name)
        if product is None:
            raise ValueError(f"Product with name {name} does not exist")
        del self._products[name]

    def sell_product(self, name, quantity):
        product = self._products.get(name)
        if product is None:
            raise ValueError(f"Product with name {name} does not exist")
        product.reduce_quantity(quantity)
        total = product.price * quantity
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sale = {
            "time" : time,
            "name" : name,
            "quantity" : quantity,
            "price" : product.price,
            "total" : total
        }
        self._sales.append(sale)
        return sale

    def save_sale_to_file(self, sale):
        # sale_with_time = sale.copy()
        # sale_with_time["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open("shift_report.json", "r", encoding="utf-8") as f:
                sales = json.load(f)

        except FileNotFoundError:
            sales = []
        sales.append(sale)

        with open("shift_report.json", "w", encoding="utf-8") as f:
            json.dump(sales, f, indent = 2)


    def shift_report(self):
        if len(self._sales) == 0:
            print("No sales")
            return
        total_sum = 0
        for i in self._sales:
            print(f'{i["time"]} / {i["name"]} in quantity {i["quantity"]} cost {i["total"]} dollars')
            total_sum += i["total"]
        print("#############")
        print(f"Total price: {total_sum}")


    def get_all_products(self):
        return list(self._products.values()) # вернет объект класса Product!



