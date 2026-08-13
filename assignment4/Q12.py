
#write a program to check if given number is armstrong number or not.
#(hint:153=1*1*1+5*5*5+3*3*3,1634=1*1*1*1+6*6*6*6+3*3*3*3+4*4*4*4).

a=int(input('enter the number ='))
count=len(str(a))
temp=a
#print(count)
armo=0
while a>0:
    dig=a%10
    armo=armo+(dig**count)
    a//=10

if temp==armo:
        print(f'{temp} is a armstrong number')
else:
        print(' is a not a armstrong number')

