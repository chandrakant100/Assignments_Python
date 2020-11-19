#WAP TO PRINT ALL PERFECT NUMBERS BETWEEN TWO RANGE.
print('Enter two ranges:')
n = int(input())
m = int(input())

if n>m :
    b = n
    l = m
else:
    b = m
    l = n
su = 0
count = 0
print('The perfect numbers between {0} and {1} are:'.format(l,b))
for i in range(l,b+1):
   for div in range(1,i):
       if i%div == 0:
           su = su+div
   if (su == i):
        print(i)
        count += 1
   su = 0
if count == 0:
    print('NULL')
    
