l = [10, 20, 4, 7, 45, 89, 12, 35]


def divi(num):
    if num % 5 == 0:
        return True
    else:
        return False


res = list(filter(divi,l))
print(list(res))
