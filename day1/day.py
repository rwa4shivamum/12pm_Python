# nam1 = input("Enter a Name:")
# #variable name = variable value
# print(nam1)

#Data Types
'''
1.Primitive Data Type
 i.int(integer like: 1,2,3,4)
 ii.float(decimal value like: 2.2)
 iii.boolean(true, false like: like kunal was adult: True)
 iv.str(character like a,b,c we can store)
 v.complex Number(real number + imaginary number, 3 + 2j)

2.Non-Primitive data Type(or Collection data Type)
  i.list
  ii.string
  iii.set
  iv.dectionary
  v.tuple
'''

name = "shivam" #(string data type)
age = 22 #int data type
salary = 3333.33 #float data type
isAdult  = True #bool

print(isAdult, salary)

#1.new Line \n
print("Hello\nShivam")
#tab space
print("python\tJava\tC++")

#separatoe(sep)
print("2026","05","12", sep="-")#2026-05-12


print("Hello", end=" ")
print("students")

for i in range(5):
    print("shivam", end=" ")


age = int(input("Enter your age: "))
print(type(age))


num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2: "))
print(num1 + num2)

name = "shivam"
suranme = "mishra"
print(name + suranme)