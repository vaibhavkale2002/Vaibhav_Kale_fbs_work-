# Q1 Write a program to find the area and perimeter of following figure (Accept the
# length, breadth and radius from user:

length=int(input('enter the number'))
breadth=int(input('enter the number '))
radius=float(input('enter the number'))

arearectangle=length*breadth
circlearea=0.5*3.14*radius**2
area=arearectangle+circlearea

perimeter=(2*length)+ breadth+3.14*radius

print('area=',area)
print('perimeter=',perimeter)

#Q2.Write a program to calculate simple interest based on Principal, Rate and Time
#(SI = P*R*T/100)


# P = int(input("Enter Principal "))
# R = float(input("Enter rate of intrest "))
# T = int(input("Enter time(year) "))

# SI = (P * R * T) / 100

# print(f"Simple Interest =", SI)

#Q3
# km = float(input(" distance in kilometers: "))

# M = km * 1000
# CM = km * 100000

# print("Distance in meters =", M)
# print("Distance in centimeters =", CM)

