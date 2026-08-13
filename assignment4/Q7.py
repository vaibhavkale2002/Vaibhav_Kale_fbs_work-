#WAP to print all integers upto n that aren't divisible by 2 & 3 .

n=int(input('enter the value'))
print('number not divisible by 3 and 2')

for i in range(1,n+1):
    if i%2!=0 and i%3!=0:
        print(i)