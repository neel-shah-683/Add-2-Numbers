a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))

def Max(x, y, z):
    if (x > y and x > z):
        return x 
    elif(y > z):
        return y
    else:
        return z  

Maximum = Max(a,b,c)
print("Maximum = ",Maximum)