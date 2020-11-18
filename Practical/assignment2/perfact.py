import math

num = input("Enter any number:")    

if num.isnumeric == False:
    print("Invalid Input!!!")
    exit()

num = int(num)
sum = 0

for i in range(1,num):
    if num % i == 0:
        sum += i

if sum == num:
    print("The number {0} is perfact number".format(num))
else:
    print("The number {0} is not a perfact number".format(num))
