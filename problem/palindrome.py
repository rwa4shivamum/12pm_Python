
num = 1223
num2 = num #num2 = 1223
# print(num%10)
# print(num//10)
reversNum = 0 #3221
sum = 0
count = 0
while(num > 0):
    dig = num % 10
    sum += dig
    count += 1
    reversNum = (reversNum * 10) + dig
    num = num // 10
print(sum,count)

'''
num =1223; reverNum = 0; dig = 3; revesNum = 0 + 3= revesNum=3 , num = 1223 // 10 num=122
num =122; reversNum = 3; dig = 2; reversNum = (3*10) + 2=32, num = 122 // 10 num=12
num =12; reverSNum=32; dig = 2; reverSNUm = (32*10) + 2=322, num = 12 // 10 num = 1
num = 1; reverSum=322; dig = 1; reverSnum = (322*10) + 1= 3220 + 1=3221 ; num = 1 // 10 num = 0
'''
# 1 5 3 9 8 2
print(1//10)
num = 12212
list = [12,32,14,15,16]
#       0  1  2  3  4
