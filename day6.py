#logical opearator
'''
and, or, not

Operator	Meaning
and	        Both conditions must be True
or         	Any one condition must be True
not     	Reverse the result

'''

#and
#print(3>2 and 4<2) #&&
#    true and false = False
#    true and true  = True
#    false and true = false
#    False and false = false

#or Operator
#print(3>2 or 4<2) ##||
#    true or false = true
#    false or true = true
#    false or false = false
#     true or true  = true

#not operator
# print(not(3>2)) #false
# print(not(3<2)) #true

# print()
a = 5
b = 3
c = 4
d = False
e = True
f = False
g = True
h = 10
i = 10
j = False

x = not a < b + c * 2 and not (d or e) == f or g and h != i or not j
'''           
        a <  b + c * 2         (d or e)
           not(True) and not(False)  or True and false or not(False)
                False and True or True and false or  True
                     False or False or True
                           False or True
                                True
'''
print(x)

# x = 10
# a = x
# x1 = 11
# print(id(x), id(x1))
# print(id(x), id(a))
# print(id(10) is id(10))

a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)

