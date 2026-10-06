name = "Shivam"
age = 23
isAdult =23
height = 5.8 
print(id(name), id(age))
print(name, age, isAdult, height)
#collection of datatype
lst = ["Shivam",23,True, 5.8]
'''
defn of list:it is a collection data types which used to store multiple element in single variable with different data types or same
#hetrogenous(mixture of many datatypes)
#1.ordered: we can Access the element by using index, and also updating the element by using index, and delete the element by using index
#2.mutable: we can make changes in list,also we can update the values or element
#3.hetrogenous
#4.Dyanamic Typed 
#5.notated by [] sqare braces
''' 
#index          0        1      2
#negativeIndex -3       -2       -1
lstOfName = ["shiv", "shivan","ksjdf"] 
#              1        2        3
print(lstOfName[1])
lstOfName[1] = "dev" #this update the value
print(lstOfName)
name = "shvam"
# lstofAge = [12, 12,14,15,16]
# lstofBool = [True, False, True]
# print(id(lst))
print(lstOfName[0])#postive indexing 
print(lstOfName[2])#negative indexng
lstOfName.append(3)
#lst have multiple inbuilt function to perform some operation on list
print(lstOfName)
# print(dir(lstOfName))
lst = ["Shivam",23,True, 5.8]
lst2 = lst.copy()
lst.append(5)
lst.reverse()
print(lst)
print(lst2)
print(dir(lst))

lstofNum = [15,14,16,12,18,10,10,20,40]
print(lst[0])
print(lst[1])
# print(lst[0])
# max = lst[0]
# print(len(lst))
for i in range(len(lstofNum)):
    print(lstofNum[i])

i=0
while(i<len(lstOfName)):
    print(lstOfName[i])
    i+=1
# for i in range(lstofNum):
#     print(i)