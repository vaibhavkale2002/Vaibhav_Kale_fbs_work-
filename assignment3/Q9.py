# input 5 subject marks from user and display grade(eg.first class, second class..)

m1=float(input('enter marks of subject 1:'))
m2=float(input('enter marks of subject 2:'))
m3=float(input('enter marks of subject 3:'))
m4=float(input('enter marks of subject 4:'))
m5=float(input('enter marks of subject 5:'))

total=m1+m2+m3+m4+m5
percentage = total / 5

print('total mark =', total)
print('percentage =',percentage)

if percentage >=90:
    print('grade:first class')
elif percentage >=70:
    print('grade:first class')
elif percentage >=50:
    print('grade:second class')
elif percentage >=40:
    print('grade:second class')
elif percentage >=35:
    print('grade:pass class')
else:
    print('grade:fail')
