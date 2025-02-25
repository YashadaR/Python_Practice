class Product:
    # class variable
    tax_rate = 0.12

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def final_price(self):
        return self.price + Product.calculate_tax(self.price)
    
    # class method update_tax_rate that updates the tax rate for all products.
    @classmethod
    def update_tax_rate(cls, new_rate):
        cls.tax_rate = new_rate
        # print(f"New tax rate for all products :{new_rate}")

    # static method calculate_tax that calculates the tax for a given price.
    @staticmethod
    def calculate_tax(price):
        return price * Product.tax_rate
    
P1 = Product("Mobile", 60000)
print(f"Final price of product {P1.name}:{P1.final_price()}")

print(f"Tax for {P1.price}:{P1.calculate_tax(P1.price)}")