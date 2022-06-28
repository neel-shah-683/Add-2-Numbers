list = [2, 8, 7, 9, 4, 6, 10, 12]
for index, item in enumerate(list):
    if(index % 2 == 0 ):
        if(index >= 1 and index <= 7):
            print("Index -> ", index, "Items -> ", item)
