class Programmer:
    company = "Microsoft"

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def printDetails(self):
        print("Company = ",self.company)
        print("\tName = ",self.name,"\n\tID = ",self.ID,"\n")

neel = Programmer("NEEL",1)
yash = Programmer("YASH",2)
neel.printDetails()
yash.printDetails()
