# write a program to prompt user to enter userid and password. after varifying 
#  userid and password display a 4 digit random number and ask user to enter the
#   same. if user enters the number then show him success message otherwise failed.
#    (something like captcha)

import random
userid ='vaibhav'
password ='4530'
   
uid =input('enter user id:')
psd =input('enter the password')

if uid==userid and psd==password:
    captcha =random.randint(1000,9999)
    print('captcha',captcha)

    user_captcha=int(input('enter the captcha'))
    if user_captcha == captcha:
        print('login successfull')
    else:
        print('captcha varifycation failed')
else:
    print('invalid userid and password')