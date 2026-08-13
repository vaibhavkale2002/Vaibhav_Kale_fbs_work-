# write a program to check if given 3 digit number is a palindrome or not.

a=int(input('enter a 3 digit number'))

first=a//100              #first digit
last=a%10                 #last digit

if first==last:
    print(a,'a palindrome number')
else:
    print(a,'not a palindrome number')