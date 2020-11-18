#wap to print sine series
n = input('Enter the range:')
if n.isnumeric() == 0:
    print('Please enter a numeric value!!!')
    exit()
else:
    n = int(n)
x = input('Please enter a value for x:')
if x.isnumeric() == 0:
    print('Please enter a numeric value!!!')
    exit()
else:
    x = int(x)
x = (3.14/180)*x
k = 1
sinx = 0
flag = 0
print('value of x(in radian):',x)
print('Terms are:')
for i in range(1,n+1):
    p = k
    fact = 1
    while p>0:
        fact = fact*p
        p -= 1
    term = (float)(pow(x,k)/fact)
    if(flag>0):
        term = term*(-1)
    print('%0.7f' %(term))
    if flag==0:
        flag = 1
    else:
        flag = 0
    sinx += (float)(term)
    k += 2
print('sinx = %0.7f' % (sinx))
    
