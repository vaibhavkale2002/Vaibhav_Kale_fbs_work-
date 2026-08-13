# write a program to convert days into year,weeks and days.

days=int(input('enter the number:'))

year=days//365
day=days%365
weak=day//7
day=day%7

print(f'year {year}, weak {weak}, day {day}:')
