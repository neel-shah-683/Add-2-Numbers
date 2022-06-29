num = int(input("Enter Any Number:"))

list = [str(i*num) for i in range(1, 11)]

table = "\n".join(list)

print(table)