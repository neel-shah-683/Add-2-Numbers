a = input("Enter Any Text:\n")

if("make lot of money" in a):
        spam = True
elif("buy now" in a):
        spam = True
elif("click this" in a):
        spam = True
elif("subscribe this" in a):
        spam = True
else:
        spam = False

if(spam):
        print("Entered Text is Spam")
else:
        print("Entered Text is not Spam")