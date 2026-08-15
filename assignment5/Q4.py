#  WAP to print armstrong number within a given range.

start=int(input('enter start number'))
end=int(input('enter end number'))
print('enter armstrong number')
for i in range(start,end+1):
    temp=i
    digits=len(str(i))
    total=0

    while temp>0:
        digit=temp%10
        total=total+digit**digits
        temp=temp//10

        if total==i:
         print(i)