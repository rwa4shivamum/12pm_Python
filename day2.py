# age = int(input("Enter Age: "))

# print(age)
# print(type(age))#

# age = input("Enter age: ") #By default string
# print(type(age))

print(type(int("5")))

#Type Conversion (To convert one data type to another data type) Or Type Casting
'''
Data Type: int= 89, string="",'', float=89.2, bool=true

like: string to integer
like integer to string
like bool to integer

'''

#input() #type string

#Explicit Type Casting (type conversion by self or human)
boolValue = False #true = 1, false = 0
age = -1
saalry = 2300.12
strin = "jksnf"
print(type(strin))
print(type(saalry))
print(type(age))
print(type(boolValue))

#here we convert bool to other data type
print(int(boolValue)) #type conversion from bool to int
print(type(str(boolValue))) #type conversion from bool to string
print(type(float(boolValue))) #type conversion from bool to float

#here we convert number to other  data type
print(type(bool(age))) #here we cnvert int to bool (Warning: except 0 and empty value all other value are true)
print(str(age)) #here we convert int to string
print(float(age)) #here we convert int to float

#here we convert 


#inmplicit(Type conversion by python)

a = 10 #int
b = 5.5 #float

c = a+b
print(type(c))



