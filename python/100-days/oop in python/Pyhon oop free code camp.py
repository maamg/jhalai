class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


item_1 = Item("phone", 100, 80)
item_2 = Item("Laptop", 2332, 3)

item_2.has_num_pad = False

print(item_1.price)
print(item_2.has_num_pad)

# item_1.name = ""
# item_1.price = 100
# item_1.quantity = 42
#
# item_2.name = "laptop"
# item_2.price = 300043
# item_2.quantity = 4

