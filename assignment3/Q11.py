#accept age of five people and also per person ticket amount and then calculate total
#  amount to ticket to travel for all of them based on following condition:
#  a. children below 12 =30% discount
#  b. senior citizen(above 59)=50% discount
#  c. other need to pay full.

total=0
for i in range(1,6):
    print('person',i)

    age=int(input('enter age:'))
    ticket=float(input('enter ticket amount:'))

if age<12:
    amount=ticket-(ticket*0.30)     #30% discount
elif age>59:
    amount=ticket-(ticket*0.50)     #50% discount
else:
    amount=ticket                   # full amount

    print('ticket amount pay=',amount)

    total=total+amount

print('total ticket amount of 5 people=',total)

               