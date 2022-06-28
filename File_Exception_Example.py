from msilib.schema import File

def readFile(filename):
    try:
        f1 = open(filename,"r")
        print(f1.read(),"\n")
    except:
        print(f"File {filename} Not Found\n")


readFile("File_Example_2.txt")
readFile("File_Example_3.txt")
readFile("File_Example_4.txt")