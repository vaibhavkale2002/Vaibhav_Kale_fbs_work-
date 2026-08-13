#write a program to enter P,T,R and calculate compound interest

p= int(input('enter amount of principle'))
r = int(input('enter rate of intrest'))
t = int(input('enter the time(year)'))

ci = p*(1+r/100)**t-p

print(f'compound interest is',ci)