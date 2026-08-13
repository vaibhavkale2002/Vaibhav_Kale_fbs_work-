#write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amount=int(input('enter the amount=.'))
temp=amount
no500=amount//500
amount=amount%500

no200=amount//200
amount=amount%200

no100=amount//100
amount=amount%100

no50=amount//50
amount=amount%50

no20=amount//20
amount=amount%20

no5=amount//5
amount=amount%5

no2=amount//2
amount=amount%2

no1=amount//1
amount=amount%1

print(f'{temp},500={no500},200={no200},100={no100},50={no50},20={no20},5={no5},2={no2},1={no1}')

