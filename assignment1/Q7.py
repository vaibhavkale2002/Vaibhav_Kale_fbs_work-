#program to find the roots of a quadratic equation
a = int(input('enter number'))
b = int(input('enter number'))
c = int(input('enter number'))

x1 = (-b+(b*b-4*a*c)**0.5)/2*a
x2 = (-b-(b*b-4*a*c)**0.5)/2*a

print(x1)
print(x2) 