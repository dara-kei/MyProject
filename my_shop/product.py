class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    def __str__(self):
        return f'{self._name} - {self._price} dollars (left {self._quantity})'

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError(f'Price must be positive, got {value}')
        self._price = value
        return self._price


    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError(f'Quantity must be positive, got {value}')
        self._quantity = value
        return self._quantity


    def change_quantity(self, amount):
        self._quantity += amount

    def reduce_quantity(self, amount):
        if amount <= 0:
            raise ValueError(f'Amount must be positive, got {amount}')
        elif self._quantity < amount:
            raise ValueError(f"You don't have enough stock! Available: {self._quantity}, got amount: {amount}")
        self._quantity -= amount




