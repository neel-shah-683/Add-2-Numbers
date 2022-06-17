def game():
    return 50

a = game()

file = open("File_Example_3.txt")
b = file.read()

if b == "":
    file = open("File_Example_3.txt","w")
    file.write(str(a))
    file.close()

elif int(b) < a:
    file = open("File_Example_3.txt","w")
    file.write(str(a))
    file.close()  