# write a program to prompt user to enter userid and password. if id and password is incorrect give him change 
#   to re-enter the credentials. let him try 3 times. after that program to terminate.

correct_user_id= 'vaibhav'
correct_password= 4530

for i in range(3):
    userid=(input('enter userid'))
    password=int(input('enter password'))
    if userid==correct_user_id and password==correct_password:
        print('login succesfully')
        break
    else:
        print('login not succesfully')
else:
    print(' let him try 3 times. after that program to terminate. ')
