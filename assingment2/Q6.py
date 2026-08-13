# WAP to calculate total salary of employee based on basic,da=10% of basic,ta=12% of basic ,hra=15% of basic.

basic=float(input('enter the salery:' ))

da= basic*(10/100)
ta= basic*(12/100)
hra= basic*(15/100)

finalsalary=basic+da+ta+hra

print(f'finalsalary={finalsalary}')
  