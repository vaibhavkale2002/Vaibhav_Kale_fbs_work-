#Q1=WAP to print following pattern
#a
for i in range(1,6):
  for j in range(1,6):
     if(i==1 or i==5 or j==1 or j==5):
        print('*', end=' ')
     else:
        print(' ', end=' ')
  print()

#b
n=4
b=1
for i in range(1,n+1):
    for j in range(i):
        print(b,end=' ')
        b=b+1
    print()


#c
n=4
for i in range(n):
    for j in range(n-i-1):
        print('',end=' ')
    num=1
    for j in range(i+1):
        print(num,end=' ')
        num=num*(i-j)//(j+1)
    print()




#d
n=5
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end=' ')
    print()



#e
for i in range(1,6):
   for j in range(1,6-i):
      print(' ',end=' ')
   for j in range (1,i+1):
      print('*',end=' ')
   for j in range(1,i):
      print('*',end=' ')
   print()
         



#f

for i in range(1,6): 
    k=1
    for j in range(6-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print(j, end=' ')
        k+=1
    for j in range(1,i):
        print(k, end=' ')
        k+=1

    print()

#g

n=8
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    for j in range(i):
        print(chr(65+j),end=' ')
    print()