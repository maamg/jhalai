class MyElectronicsShop:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def calculate_total_price(self):
        return self.price * self.stock_quantity


i_phone = MyElectronicsShop('iPhone', 100, 100)
print(i_phone.stock_quantity)
print(i_phone.name)
print(i_phone.price)
mac_book = MyElectronicsShop('MacBook', 500, 100)
Total_iphone_value = i_phone.calculate_total_price()
# print(Total_iphone_value)