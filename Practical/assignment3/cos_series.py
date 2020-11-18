#wap to compute cos series
n = input('Enter the range:')
if n.isnumeric() == 0:
    print('Please enter a numeric value!!!')
    exit()
else:
    n = int(n)
x = input('Enter a value for x:')
if x.isnumeric() == 0:
    print('Please enter a numeric value!!!')
    exit()
else:
    x = int(x)
x = (3.14/180)*x
k = 2
flag = 0
cosx = 0
term = 1
for i in range(1,n+1):
    print('%0.7f' %term)
    cosx += term
    p = k
    fact = 1
    while p!=0:
        fact  = fact*p
        p -= 1
    term = pow(x,k)/fact
    if flag==0:
        term = term*(-1)
   
    if flag==0:
        flag = 1
    else:
        flag = 0
    k += 2
print('cosx=%0.7f' %cosx)
