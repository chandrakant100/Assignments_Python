import math

num = input("Enter a number:")
if num.isnumeric() == 0:
    print("Its is string")
    exit()
num = int(num)

for i in range(num):
    for j in range(num,i,-1):
        print(" ",end = '')
    for k in range(1,i+2):
        if k % 2 == 0:
            print("1",end = ' ')
        else:
            print("0",end = ' ')
    print()