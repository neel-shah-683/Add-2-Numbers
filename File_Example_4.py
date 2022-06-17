words = ["Program"]

file = open ("File_Example_4.txt")
a = file.read()

for word in words:
    str1 = a.replace(word,"#")
    file = open("File_Example_4.txt","w")
    file.write(str1)

file.close()
