#convert distant given in feet and inches into meter and centimeter.

feet=float(input('enter the feet'))
inches=float(input('enter the inches'))

totalinches =(feet*12)+inches
meter=totalinches*0.0254
centimeters=totalinches*2.54

print('distance of meter',meter)
print('distance of centimeter',centimeters)

 