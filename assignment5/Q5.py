# WAP to print prime number between 1 to 100.

for a in range(2,101):
    count=0

    for i in range(1,a+1):
        if a%i==0:
            count+=1
    if count==2:
        print(a)