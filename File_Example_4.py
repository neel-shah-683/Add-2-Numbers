file = open ("File_Example_4.txt")
a = file.read()

str = a.replace("Program","#")

file = open("File_Example_4.txt","w")
file.write(str)

file.close()
