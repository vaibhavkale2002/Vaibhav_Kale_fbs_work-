#write a program to check if person  is eligible to marry or not( male age>=21 and female>=18)

gender=input('enter gender(M/F):')
age=int(input('enter age'))
if(gender=='F'):
    if(age>=18):
        print('femail is eligible for marry:')
    else:
        print('femail is not eligible for marry:')
else:
    if(age>=21):
        print('male is eligible for marry')
    else:
        print('male is not eligible for marry')
