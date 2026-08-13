#WAP to print all number in a range  divisible by a given number 
a=int(input('enter the start number'))
b=int(input('enter the ending number'))
c=int(input('enter the divisor'))
print('number divisor by',c )

for i in range(a,b+1):
    if i % c==0:
        print(i)
