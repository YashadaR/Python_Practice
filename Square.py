#Area of square & perimeter of square

class Square:
    side = 8
    # def __init__(self):
        # self.side = side

    def area(self):
        return self.side*2

    def perimeter(self):
        return self.side*4

S = Square()
print(f"Area of square is {S.area()}")
print(S.perimeter())


        
