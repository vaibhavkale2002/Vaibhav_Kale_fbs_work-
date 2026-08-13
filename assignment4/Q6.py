#WAP tp check if a given number is prime number or not . 
num=int(input('enter number'))
count=0

for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print(num,'is a prime number')
else:
    print(num,'is a not a prime number ')
