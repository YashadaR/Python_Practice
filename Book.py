class Book:
    Discount_rate = 0.01

    def __init__(self, name, price):
        self.name = name
        self.price = price

        #Book.Discount_rate += 1

    def description(self):
        return f"Book name is {self.name} and price is {self.price}."

    @classmethod
    def new_discount_rate(cls, rate):
        cls.Discount_rate = rate
        return f"Discount rate is {cls.Discount_rate*100}%"
    
B1 = Book("ABC", 1000)
print(Book.new_discount_rate(0.05))

print(B1.description())

