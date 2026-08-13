# write a program to check if user has entered correct userid and password.

correct_userid='vaibhav' 
correct_password='1234'

userid=input('enter userid')
password=input('enter password')

if userid==correct_userid and password==correct_password:
    print('login successful')
else:
    print('invalid user id or password')

