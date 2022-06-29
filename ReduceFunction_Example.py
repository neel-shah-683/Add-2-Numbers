from functools import reduce


l = [3, 4, 7, 8, 2, 1, 12, 1, 45]

res = reduce(max,l)
print(res)