import csv
class MyGadgeteStore:
    # Class attribute
    pay_rate = 0.8  # In 20% discount pay rate will be 0.8
    all = []

    def __init__(self, name: str, price: float, quantity= 0): # Instructor

        # Validation checker
        assert price >= 0, f"Price: {price} must be greater than or equal to zero"
        assert quantity >= 0, f"Quantity: {quantity} must be greater than or equal to zero"

        # Attribute assigning
        self.__name = name
        self.price = price
        self.quantity = quantity

        MyGadgeteStore.all.append(self)
    @property
    def name(self):
        return self.__name

    def calculate_total_price(self):
        return self.price * self.quantity  # instance attribute

    def apply_discount(self):
        self.price = self.price * self.pay_rate
    #
    # def __repr__(self):
    #     return f"MyGadgeteStore('{self.name}', {self.price}, {self.quantity})')"

    # @classmethod
    # def instantiate_from_csv(cls):
    #     with open('store.csv', 'r') as file:
    #         reader = csv.DictReader(file)
    #         products = list(reader)
    #
    #         for product in products:
    #             MyGadgeteStore(
    #                 name=product.get('product'),
    #                 price=float(product.get('price')),
    #                 quantity=int(product.get('quantity'))
    #             )
    # @staticmethod
    # def is_integer(number):
    #     if isinstance(number, float):
    #         return number.is_integer()
    #     elif isinstance(number, int):
    #         return True
    #     else:
    #         return False
# MyGadgeteStore.instantiate_from_csv()
# print(MyGadgeteStore.all)

# print(MyGadgeteStore.is_integer(324.0))
# print(324.0.is_integer())

item1 = MyGadgeteStore("iPad", 400, 0)
item1.__name= "maamg"
print(item1.__name)

