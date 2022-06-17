file = open("File_Example_2.txt")
a = file.read()
print(a+"\n")
if "Python" in a:
    print("Python is Present: ")
else:
    print("Python is not Present: ")
file.close()