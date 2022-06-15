num = int(input("Enter Any Number: "))
    
sum = 0

# 1st Approach

'''i = 1
while i <= num:
    sum = sum + i
    i = i + 1'''

# 2nd Approach

while num > 0:
    sum = sum + num
    num = num - 1
print("Sum = ",sum)