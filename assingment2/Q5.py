#WAP to calculate selling price of book based on cost prise and discount.
cp=float(input('enter the cost prise'))
discount=float(input('enter the discunt'))

sp=cp-(cp*discount)/100

print('selling prise',sp)