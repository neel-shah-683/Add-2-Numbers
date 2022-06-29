l = [10, 20, 4, 7, 45, 89, 12, 35]

div = lambda num: num % 5 == 0

res = list(filter(div,l))
print(res)
