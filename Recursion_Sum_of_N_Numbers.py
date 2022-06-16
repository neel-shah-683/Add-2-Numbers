num = int(input("Enter Any Number: "))

def recur_func(x):
    if x <= 1:
        return x
    else:
        return x + recur_func(x - 1)

result = recur_func(num)
print("Sum of",num,"Numbers =",result)