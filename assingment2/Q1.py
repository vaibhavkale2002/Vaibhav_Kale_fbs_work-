# convert the time entered in hh,min and sec into seconds.
h=int(input('enter the hours'))
m=int(input('enter the minites'))
s=int(input('enter the seconds'))

s1=h*3600
s=s1+s
s2=m*60
sec=s+s1+s2
print('all second',sec)
