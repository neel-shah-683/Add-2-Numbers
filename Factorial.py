from re import I


num = int(input("Enter Any Number: "))

fact = 1
for i in range(1, num+1):
    fact = fact * i 

print("Factotial of ",num," = ",fact)