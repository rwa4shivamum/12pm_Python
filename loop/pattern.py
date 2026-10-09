'''
****
****
****
****
'''

i=0
while(i<=4):
    j=0
    while(j<=4):
        print(i,j)
        j = j+1
    
    i = i+1

'''
i=0;i<=4(0<=4)True
   j=0;j<=4(0<=4)True,print(0,0);j=1
   j=1;j<=4(1<=4)True,print(0,1);j=2
   j=2;j<=4(2<=4)True,print(0,2);j=3
   j=3;j<=4(3<=4)True,print(0,3);j=4
   j=4;j<=4(4<=4)True,print(0,4);j=5
   j=5;j<=5(5<=4)False
i=1,i<=4(1<=4)True
   j=0;j<=4(0<=4)True,print(0,0);j=1
   j=1;j<=4(1<=4)True,print(0,1);j=2
   j=2;j<=4(2<=4)True,print(0,2);j=3
   j=3;j<=4(3<=4)True,print(0,3);j=4
   j=4;j<=4(4<=4)True,print(0,4);j=5
   j=5;j<=5(5<=4)False






0 0   
0 1
0 2
0 3
0 4
1 0
1 1
1 2
1 3
1 4
'''

# n=6
# i=0
# while(i<n):
#     j=0
#     while(j<n):
#         print("*", end="")
#         j = j + 1
#     print("\n")
#     i = i + 1


'''
*
**
***
****
*****
'''

n=6
i=0
while i<n:
    j=0
    while j<=i:
        print("*", end="")
        j =j + 1
    print()
    i = i+1

'''
n=6
i=0 (i=(0<=6)T; j=0; j<=i(0<=0)T;j=1
                j=1; j<=i(1<=0)F;
i=1 (i=1<=6)T; j=0; j<=1(0<=1)T;j=1
               j=1; j<=i(1<=1)T;j=2
               j=2; j<=i(2<=1)F
i=2 (i=(2<=6)T;j=0; j<=i(0<=2)T;j=1
               j=1; j<=i(1<=2)T;j=2
               j=2; j<=i(2<=2)T:j=3
               j=3; j<=i(3<=2)F





*
**
***
****
*****

*****
****
***
**
*



    *
   ***
  *****
 ******* 
*********
'''

i=4
while(i>=1):
    print(i)
    i -= 1

n=5
i=n
while(i>=1):
    j=1
    while(j<i):
        print("?", end="")
        j += 1
    z=0
    while(z<=(n-i)*2):
        print("*", end="")
        z += 1
    print()
    i -= 1

'''
n=5,i=5;i= 5>=1 T;j=1,j<i(1<5)T,j=2
                  j=2,j<i(2<5)T,j=3
                  j=3,j<i(3<5)T,j=4
                  j=4,j<i(4<5)T,j=5
                  j=5,j<i(5<5)F
                                    z=0,z<=5-5=0<=0T,z=1
                                    z=1,z<=5-5= 1<=0 F
n=5,i=4,i= 4>=1 T;j=1 to i=4; z=0 to 1

????*
???**

'''
#range-inbuilt function start, stop, step 
#                        0,     10,   2
#0,1,2,3,4,5,6,7,8,9
#0,2,4,6,8
             #stop
for i in range(10):#bydefault start value 0 , by default step value 1
    print(i)
           #start,stop
for i in range(5,10):#by default step 1
    print(i)

print("below was start stop step")

#   start, stop, step
for i in range(1,10,2):
    print(i)

'''
initialize
condition
increment.decrement
'''
print("Here reverse loop")
i=10
while(i>=1):
    print(i)
    i -= 1
print("Here reverse loop using for lop")
for i in range(10,-10,-2):
    print(i)

'''
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6 7 8 9 10

'''