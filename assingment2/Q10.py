#write a program to reverse three-digit number.

x=int(input('enter the reverce value'))

hundreds=x//100
tens=(x//10)%10
units=x%10

rev=(units*100)+(tens*10)+hundreds
print('enter the reverce value',rev)
