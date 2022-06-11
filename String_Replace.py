str = '''Dear <|NAME|>
You are selected!

Date: <|DATE|>
'''
name = input("Enter Your Name: ")
date = input("Enter Date: ")

str = str.replace("<|NAME|>",name+",")
str = str.replace("<|DATE|>",date)

print(str)