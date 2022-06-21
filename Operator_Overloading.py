#  (a + ib) (c + id) = (ac - bd) + i(ad + bc).

class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)

    def __mul__(self, c):
        mulreal = self.real * c.real - self.imaginary * c.imaginary  
        mulimagi = self.real* c.imaginary + self.imaginary * c.real
        return Complex(mulreal,mulimagi)
        
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(3, 2)
c2 = Complex(1, 7)
print("Addition = ",c1 + c2)
print("Multiplication = ",c1 * c2)