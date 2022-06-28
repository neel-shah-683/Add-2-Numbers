# Print Multiplication Table of any number using list comprehension
num = int(input("Enter Any Number:"))

table = [num*i for i in range(1, 11)]
print(table)
