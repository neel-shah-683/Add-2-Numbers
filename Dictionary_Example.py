# Dictionary of Hindi keys with their corresponding english translation
myDict = {
    "Sher" : "Lion",
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Chasmah" : "Spectacles"
}
print("Options are: ",myDict.keys())

a = input("\nEnter Any Word From Above Options: ")

print("\nMeaning of ",a," = ",myDict.get(a))