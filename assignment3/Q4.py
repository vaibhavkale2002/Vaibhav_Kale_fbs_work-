#write  a program to input all sides of a triangle and check whether triangle is valid or not.

a=float(input('enter first sides'))
b=float(input('enter second sides'))
c=float(input('enter third sides'))

if a+b>c and a+c>b and b+c>a:
    print('triangle is valid')
else:
    print('triangle is not valid')