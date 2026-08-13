#write a program to check whether the triangle is equilateral,isosceles or scalene triangle.
a=float(input('enter first sides'))
b=float(input('enter second sides'))
c=float(input('enter third sides'))

if (a+b>c) and (a+c>b) and (b+c>a):
    if a==b==c:
        print('triangle is equilateral')
    elif a==b or b==c or a==c:
        print('triangle is isosceles')
    else:
        print('triangle is scalene')
else:
    print('a valid triangle.')