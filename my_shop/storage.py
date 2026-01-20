from product import Product
import json
from datetime import datetime
import logging


class Storage:
    def __init__(self):
        self._products = {}
        self._sales = []

    def get_sales(self):
        return self._sales

    def add_product(self, name, price, quantity):
        try:
            new_product = Product(name, price, quantity)
            logging.info(f"New product created: name: {name}, price: {price}, quantity {quantity}")
        except ValueError:
            logging.error(f"Failed to create product {name}")
            raise
        if name not in self._products:
            self._products[name] = new_product
            logging.debug(f"New product {name} added to list of products")

        else:
            logging.warning(f"Product {name} have already added")
            raise ValueError(f"Product with name {name} already exists")

    def get_product(self, name):
        if name in self._products:
            logging.info(f"Requested product {name} is displayed")
            return self._products[name]
        else:
            logging.warning(f"Product {name} not existed")
            raise ValueError(f"Product with name {name} does not exist")

    def restock_product(self, name, quantity):
        product = self._products.get(name)
        if product is None:
            logging.error(f"Product {name} not existed")
            raise ValueError(f"Product with name {name} does not exist")
        if quantity <= 0:
            logging.warning("Invalid quantity entered")
            raise ValueError("Restock quantity must be positive")
        product.change_quantity(quantity)
        logging.info(f"Restock quantity of {name} changed by user in quantity of {quantity}")

    def remove_product(self, name):
        product = self._products.get(name)
        if product is None:
            logging.warning(f"Product {name} not existed")
            raise ValueError(f"Product with name {name} does not exist")
        del self._products[name]
        logging.info(f"Product {name} deleted by user")

    def sell_product(self, name, quantity):
        product = self._products.get(name)
        if product is None:
            logging.error(f"Product {name} not existed")
            raise ValueError(f"Product with name {name} does not exist")
        product.reduce_quantity(quantity)
        logging.debug(f"Quantity of product {name} reduced by {quantity}")
        total = product.price * quantity
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sale = {
            "time" : time,
            "name" : name,
            "quantity" : quantity,
            "price" : product.price,
            "total" : total
        }
        logging.info(f"New sale created. Name: {name}, quantity: {quantity}, total price: {total}")
        self._sales.append(sale)
        logging.debug(f"New sale of {name} added to sales list")
        return sale

    def save_sale_to_file(self, sale):
        try:
            with open("shift_report.json", "r", encoding="utf-8") as f:
                logging.debug("Json file shift_report.json opened")
                sales = json.load(f)

        except FileNotFoundError:
            logging.info("File not found. Starting with empty sales list")
            sales = []
        sales.append(sale)

        with open("shift_report.json", "w", encoding="utf-8") as f:
            logging.debug("Json file shift_report.json written")
            json.dump(sales, f, indent = 2)


    def shift_report(self):
        if len(self._sales) == 0:
            print("No sales")
            logging.debug("No sales")
            return
        total_sum = 0
        for i in self._sales:
            print(f'{i["time"]} / {i["name"]} in quantity {i["quantity"]} cost {i["total"]} dollars')
            total_sum += i["total"]
        print("#############")
        print(f"Total price: {total_sum}")
        logging.info(f"Shift report displayed with te total sum: {total_sum}")


    def get_all_products(self):
        return list(self._products.values()) # вернет объект класса Product!



