import math 

class Calculator:

    def __init__(self, number):
        self.number = number
    
    def square(self):
        result = self.number * self.number
        print("Square of ",self.number," = ",result,"\n")

    def cube(self):
        result = self.number * self.number * self.number
        print("Cube of ",self.number," = ",result,"\n")

    def sqrt(self):
        result = math.sqrt(self.number)
        print("Square Root of ",self.number," = ",result)

num = Calculator(3)
num.square()
num.cube()
num.sqrt()
