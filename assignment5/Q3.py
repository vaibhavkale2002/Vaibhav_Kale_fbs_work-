#3  Accept no. of passengers from user andper ticket cost. then accept age of each passenger and then calculate total amount
#  to ticket to travel for all of them based onfollowing condition
#  a.children below 12=30% discount
#  b.senior citizen(above59)=50% discount
#  c.others need to pay full.

p=int(input('enter the passenger'))
prise=int(input('enter prise of ticket'))
total=0
for i in range(1,p+1):
    age=int(input('enter the age passenger{i}:'))
    if age<12:
        ticket=prise-(prise*30/100)
    elif age>59:
        ticket=prise-(prise*50/100)
    else:
        ticket=prise
    total=total + ticket
print('total ticket amount',total)