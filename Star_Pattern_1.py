'''
* 

* *

* * *

* * * *

* * * * *
'''

num = int(input("Enter Any Number: "))

for i in range(1, num+1):
    for j in range(1, num+1):
        if(j <= i):
            print("* ",end="")
        
    print("\n")
