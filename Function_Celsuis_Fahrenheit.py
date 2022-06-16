cel = int(input("Enter Celsius: "))


def cel_to_fah(x):
        return (x * 9/5) + 32 

celsius = cel_to_fah(cel)
print("Fahrenheit = ",celsius)