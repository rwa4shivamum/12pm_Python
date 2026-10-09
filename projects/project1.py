print("Welcome to interactive Personal Data Collector")

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
height = float(input("Enter your height in meters: "))
favNumber = int(input("Enter your Favourite Number: "))

print("Thank you! Here is the information we Collected: ")


print(f"Name: {name} (Type: {type(name)}, Memory Adderess: {id(name)})")

# currectYear = 2026
# print(currectYear - age)