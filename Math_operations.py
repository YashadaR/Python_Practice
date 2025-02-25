# class Math_Operations:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def add(self):
#         return self.a + self.b +self.c

# M = Math_Operations(10, 20, 30)
# print(M.add())

class Math_Operations:
    def __init__(self):
        pass

    def add(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        return self.a + self.b +self.c

M = Math_Operations()
# M.a = 10
# M.b = 20
# M.c = 30
print(M.add(10, 20, 30))
