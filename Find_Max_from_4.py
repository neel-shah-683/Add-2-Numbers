n1 = int(input("Enter Number1 : \n"))
n2 = int(input("Enter Number2 : \n"))
n3 = int(input("Enter Number3 : \n"))
n4 = int(input("Enter Number4 : \n"))

if(n1 > n2 and n1 > n3 and n1 > n4):
        print(n1," is Maximum")
elif(n2 > n3 and n2 > n4):
        print(n2, " is Maximum")
elif(n3 > n4):
        print(n3," is Maximum")
else:
        print(n4," is Maximum")
