num = int(input("Enter Any Number: "))

def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)

result = factorial(num)
print("Factorial of",num,"=",result)