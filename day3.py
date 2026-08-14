#Operators in python
'''
An operators is a symbol that perform an operation on varibles or value
name = "kunal" #variable

'''

# name = "kunal" #variable
num = 1
num2 = 3
print(num + num2)#here I used varible to perform some operation using operator
# num , num2 are operand, while + was operator
print(2 + 3)#here I used value to perform some operation using operator

# Types of Operator in Python
'''
Python has mainly:
1.Arithmetic operators(We perform mathematical operation on arithmatic operators)
2.Assignment Operators
3.Comparison OPerators
4.Logical Operators
5.Identity Operators
6.Membership Operators
7.Bitwise Operators
'''
#Arithmatic:- +,-,*,/,//,%,**
'''
Operator	Meaning	Example
+           Addition           10 + 5
-           Subtraction           10 - 5
*           Multiplication           10 * 5
/           Division           10 / 5
//           Floor Division           10 // 3
%           Modulus           10 % 3
**           Power           2 ** 3
'''

print(2+3)
print(type(2*3.3))
print(2*3)
print(9/2)#here type of division was float
print(9//2)#here we got the floor value and dataype was int
print(9%2)#it alway return remainder value
print(2**10)#2*2*2*2*2
print(2*2*2*2*2)
'''
ciel:3 

     2.3

floor: 2

-1 0 1 2
'''


#Assignment OPerators (used to assign values)
'''
= This operator used to asssign value on varible
+=

'''
name = None
print(name)

a = 2
a = a + 2 #a=4
a += 2 #a=4 + 2 = 6
a = a - 2
a = a*2
a = a**2
a = a//2
a = a%2

print(a)
b = a + 2
print(a,b)