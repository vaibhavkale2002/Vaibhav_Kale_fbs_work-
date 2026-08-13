#WAP to check if given number strong number.  
a=int(input('enter the number'))
temp=a
sum=0
while temp>0:
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    temp=temp//10
if sum==a:
        print(a,'is a strong number')
else:
        print(a,'is a not strong number')