# write a program to solve the following series:
#  a. 1!+2!+3!+4!+......n!
#  b. N +N^2 +N^3 +N^4.....+N^N(here ^ means exponent)
#  c.S=a+a2/2+a3/5-x4/7+....to n terms

a=int(input('enter the number'))
fact=1
sum=0

for i in range(1,a+1):
    fact=fact*i
    sum=sum+fact

print("sum=",sum)