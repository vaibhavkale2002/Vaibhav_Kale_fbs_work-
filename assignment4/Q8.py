#WAP to find which numbers are divisible by 7 and multiple  of 5 in a given range.

a=int(input('enter starting number'))
b=int(input('enter ending number'))
print('divisible by 7 and multiple of 5')

for i in range(a,b+1):
    if i%7==0 and i%5==0:
        print(i)