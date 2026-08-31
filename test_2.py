# Q1.

year = int(input("Enter a year: "))

if year % 4 != 0:
    print("Not a Leap Year")
elif year % 100 != 0:
    print("Leap Year")
elif year % 400 != 0:
    print("Not a Leap Year")
else:
    print("Leap Year")



# Q2.Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
# Eg : - 428 , 214 etc.

num = int(input("Enter a 3 digit number: "))

first = num // 100
second = (num // 10) % 10
third = num % 10

if first == 2 * second and first == third / 2:
    print("Yes, you have done it")
else:
    print("Please try next time")


# Q3A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

import math

radius = 20
length = 50
breadth = 40
wire_cost = 35
times = 5

if 2 * radius == breadth:
    perimeter = (2 * length) + breadth + (math.pi * radius)
else:
    perimeter = 2 * (length + breadth) +math.pi * radius

total_wire = perimeter * times

total_cost = total_wire * wire_cost

print("Perimeter of field =", round(perimeter, 2), "m")
print("Total wire required =", round(total_wire, 2), "m")
print("Total cost = Rs.", round(total_cost, 2))


# Q4Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.


length = float(input("Enter length of the wall (m): "))
height = float(input("Enter height of the wall (m): "))
cost_per_sq_m = float(input("Enter painting cost per sq.m: "))

wall_area = length * height

total_area = 4 * wall_area

if total_area > 0 and cost_per_sq_m > 0:
    total_cost = total_area * cost_per_sq_m
    print("Total area to be painted =", total_area, "sq.m")
    print("Total cost of painting = Rs.", total_cost)
else:
    print("calculate the total cost.")


# Q5.A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST 


p1 = float(input("Enter price of product 1: "))
p2 = float(input("Enter price of product 2: "))
p3 = float(input("Enter price of product 3: "))
p4 = float(input("Enter price of product 4: "))
p5 = float(input("Enter price of product 5: "))


total = p1 + p2 + p3 + p4 + p5


if total > 0:
    gst = total * 18 / 100
    bill = total + gst

    print("Total before GST = Rs.", total)
    print("GST (18%) = Rs.", gst)
    print("Total bill = Rs.", bill)
else:
    print("invalid prise amount!")
