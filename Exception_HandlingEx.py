try:
    a = int(input("Enter Any Number: "))
    b = a / 0
except ValueError as e:
    print("Please Enter a  Valid Input Digit Number...")
except ZeroDivisionError as e:
    print("You have an error in your Input: ")
except:
    print("Your Input is not valid.")