#i=1 to 5
n=5
#1 to n like:1,2,3,4,5
i=1
while(i<=n):
    print(i)
    i += 1

#n to 1 like:5,4,3,2,1
n=5
while(n>=1):
    print(n)
    n = n - 1

'''
n=5(initilization);n>=1(5>=1)True (condition Phase);print 5;n=5-1; n=4
n=4;n>=1(4>=1)True (condition Phase);print 4;n=4-1; n=3
n=3;n>=1(3>=1)True (condition Phase);print 3;n=3-1; n=2
n=2;n>=1(2>=1)True (condition Phase);print 2;n=2-1; n=1
n=1;n>=1(1>=1)True (condition Phase);print 1;n=1-1; n=0
'''
# step1 : 5
# step2 : 4
# step3 : 3
# step4 : 2
# step5 : 1


i=1
while(i<=10):
    if i%2==0:
        print(i)
    i += 1

'''
i=1; i<=10(1<=10True); if(1%2==0)F; i=1+1=2
i=2; i<=10(2<=10True); if(2%2==0)T;print(i); i=2+1=3
i=3; i<=10(3<=10True); if(3%2==0)F;i=3+1=4
'''
#2,
print(1%2)
print(1/2)


'''
****
****
****
****
'''

i=0
while(i<=4):
    print(i)
    i = i+1
