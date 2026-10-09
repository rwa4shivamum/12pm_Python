name = "Shivam"
age = 23
isAdult =23
height = 5.8 
# print(id(name), id(age))
# print(name, age, isAdult, height)
# #collection of datatype
# lst = ["Shivam",23,True, 5.8]
# '''
# defn of list:it is a collection data types which used to store multiple element in single variable with different data types or same
# #hetrogenous(mixture of many datatypes)
# #1.ordered: we can Access the element by using index, and also updating the element by using index, and delete the element by using index
# #2.mutable: we can make changes in list,also we can update the values or element
# #3.hetrogenous
# #4.Dyanamic Typed 
# #5.notated by [] sqare braces
# ''' 
# #index          0        1      2
# #negativeIndex -3       -2       -1
# lstOfName = ["shiv", "shivan","ksjdf"] 
# #              1        2        3
# print(lstOfName[1])
# lstOfName[1] = "dev" #this update the value
# print(lstOfName)
# name = "shvam"
# # lstofAge = [12, 12,14,15,16]
# # lstofBool = [True, False, True]
# # print(id(lst))
# print(lstOfName[0])#postive indexing 
# print(lstOfName[2])#negative indexng
# lstOfName.append(3)
# #lst have multiple inbuilt function to perform some operation on list
# print(lstOfName)
# # print(dir(lstOfName))
# lst = ["Shivam",23,True, 5.8]
# lst2 = lst.copy()
# lst.append(5)
# lst.reverse()
# print(lst)
# print(lst2)
# print(dir(lst))

# lstofNum = [15,14,16,12,18,10,10,20,40]
# print(lst[0])
# print(lst[1])
# # print(lst[0])
# # max = lst[0]
# # print(len(lst))
# for i in range(len(lstofNum)):
#     print(lstofNum[i])

# i=0
# while(i<len(lstOfName)):
#     print(lstOfName[i])
#     i+=1
# # for i in range(lstofNum):
# #     print(i)

# '''
# 1.list:
#  i.defn:collection of data in a single data type or multiple
#    a.mutable(means-> can be change)
#    b.dynamically typed(runtime datatype specify)
#    c.hetrogenous(mix of many data Types)
#    d.notoded by []
#    c.ordered(index based access, modify, delete)
#  ii.inbuilt function
#    a.append(add element last of list)
#    b.remove(remove element by given element)
#    c.reverse(reverse the original list)
#    d.copy(copy of list stored in another varible)
#    c.count(element)
#    d.sort() 
#    e.pop()
#    f.extend()
#    g.insert()
#    h.clear()
#  iii.iterate a list using for, while
# '''
# #      1   9   3025 25
# #      0 1 2 3 4  5 6
# lst = [1,2,3,4,55,5,5]
# print(lst[2]**2)
# # print(lst.count(5))
# # lst.sort()
# # print(lst)
# # print(lst.pop())
# # print(lst)
# # lst2= [1,2,3,4,5,65]
# # lst.extend(lst2)
# # print(lst)
# # lst.insert(6, 939)
# # print(lst)
# # print(lst.index(939))
# # lst.clear()
# # print(lst)

# # for i in lst:
# #     print(i**2)
# print(len(lst))
# lstOfSquare = []
# for i in range(0,len(lst)):
#     if i%2==0:
#         lstOfSquare.append(lst[i]**2)
# print(lstOfSquare)
# #0 2 4 6
# #[3,9,3025,25]
# i=0
# while(i<len(lst)):
#     print(lst[i])
#     i+=1

# print(7%2)
#      0 1 2 3 4
# lst = [1,2,3,4,5]
#      1 4 27 256 3125
# for i in range(0,len(lst)):
#     lst[i] = lst[i]**lst[i]

'''
i=0; lst[0]=1**1 lst[0]=1;
i=1; lst[1]=2**2 lst[1]=4;
i=2; lst[2]=3**3 lst[2]=9
'''
# print(lst)

# name = "sjovam"
# for i in lst:
#     i**2
lst = [1,2,3,4,5]
lst2 = [i**2 for i in lst] #list
print(lst2)
print(lst)

lst3 = []
for i in lst:
    lst3.append(i**2)
print(lst3)



#lst = [1,2,3,4,5,6,7,8]
# lstOfEven = []
# for i in lst:
#     if(i%2==0):
#         lstOfEven.append(i)
# print(lstOfEven)
# lstofEven2 = [lst[i] for i in range(len(lst)) if lst[i]%2==0]
# lisofEven3 = [i for i in lst if i%2==0]
# lstofEven4 = ["even" if i%2==0 else "odd" for i in lst]
# print(lstofEven4)

lst = [1,2,3,4,5,6,7,8]
lst2 = []
for i in range(len(lst)):
    if(lst[i]%2==0):
        lst2.append("even")
    else:
        lst2.append("odd")
print(lst2)
'''
lst2 = [], i=0; lst[0]%2==0; lst2.append("odd"); lst2 = ["odd"]
lst2 = ["odd"], i=1; lst[1]%2==0; lst2.append("even"); lst2 = ["odd", "even"]
 lst2 = ["odd", "even"]; i=2
'''