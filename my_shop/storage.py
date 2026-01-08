from product import Product

class Storage:
    def __init__(self):
        self._products = {}

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
        print(f"The final price is {product.price * quantity}")
        return product.price * quantity

    def get_all_products(self):
        return list(self._products.values()) # вернет объект класса Product!



