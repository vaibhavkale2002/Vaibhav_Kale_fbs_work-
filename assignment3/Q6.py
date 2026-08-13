#write a program to calculate profit or loss.

cp=float(input('enter cost prise'))
sp=float(input('enter selling prise'))

if sp>cp:
    profit=sp-cp
    print('profit =',profit)
elif cp>sp:
    loss=cp-sp
    print('loss =',loss)
else:
    print('no profit,no loss')