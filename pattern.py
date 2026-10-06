'''
*????
**???
***??
****?
*****
'''
n=5
for i in range(0,n,1):
    for j in range(i+1):
        print("*", end="")
    print()
'''
i=0, i<5
   j=0, 0<1, j=1, 1<1F
i=1, 1<5T
   j=0, j<2, 0<2, j=1<2, j=2<2 F

*
**

'''

i=0
while(i<n):
    j=0
    while(j<=i):
        print("*", end="")
        j+=1
    z=0
    while(z<=(n-i-2)*2+1):
        print(" ", end="")
        z+=1
    j=0
    while(j<=i):
            print("*", end="")
            j+=1
    print()
    i+=1
i=n
while(i>=0):
    j=0
    while(j<=i):
        print("*", end="")
        j+=1
    z=0
    while(z<=(n-i-2)*2+1):
        print(" ", end="")
        z+=1
    j=0
    while(j<=i):
            print("*", end="")
            j+=1
    print()
    i-=1

for i in range(0,n,1):
     for j in range(0,i,1):
          print("*", end="")
     for z in range(0,(n-i-2)*2+1,1):
          print(" ", end="")
     for j in range(0,i,1):
          print("*", end="")
     print()


'''
i=0;n=5, 0<5 
   j=0, 0<=0 T;j++
   j=1, 1<=0F
   z=0, z<=(5-0-2)0<=3T,z=1
   z=1, 1<=3T,z=2
   z=2, 2<=3T,z=3
   z=3, 3<=3T,z=4
   z=4, 4<=3F
      j=0; 0<=0 T *, j=1; 1<=0 F
i=1; 1<5 T,
   j=0, 0<=1 T, j++
   j=1, 1<=1 T, j=2<=1 F
   z=0, 0<=5-1-2(0<=2)T, z=1
   z=1, 1<=2T, z=2
   z=2, 2<=2T, z=3
   z=3, 3<=2F
i=2; 2<5 T
    j=0, 0<=2, j=1
    j=1, 1<=2, j++
    j=2, 2<=2, j++
    j=3, 3<=2F

*????
**???


*????????*
**??????**
***????***
****??****
**********

????*
???**
??***
?****
*****
*****
*   *
*   *
*   *
*****
'''
student1 = "shivam"
student2 = "sani"
student3 = "shv"
num1 = 5
num2 = 10
print(f"My name is {student1}, and Second classMate was {student2}, and third classmate was {student3} {num1 + num2}")

n=5
for i in range(0,5+1,1):
     for j in range(0,5+1,1):
          if(i==0 or i==n or j==0 or j==n):
               print("*", end="")
          else:
               print(" ", end="")
     print()