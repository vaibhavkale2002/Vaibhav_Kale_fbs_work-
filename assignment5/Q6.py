# write a program to print first n prime numbers.

n=int(input('enter how many prime number'))
count=0
a=2
while count<n:
    first=0

    for i in range(1,a+1):
        if a%i==0:
            first+=1

    if first==2:
        print(a)
        count+=1

    a+=1
