sub1 = int(input("Enter SUB1 Marks:\n"))
sub2 = int(input("Enter SUB2 Marks:\n"))
sub3 = int(input("Enter SUB3 Marks:\n"))

total = sub1 + sub2 + sub3
avg = total / 3

if(avg < 33):
    print("You Are Failed:")
else:
    print("You Passed...!")