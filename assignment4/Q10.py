#WAP to check if given number is perfect number.
x=int(input('enter the number'))
sum=0
for i in range(1,x):
    if x % i==0:
     sum=sum+i
if sum==x:
    print(x,'is a perfect number')
else:
    print(x,'is a not perfect number')