import math

num = input("Enter any number:")    

if num.isnumeric == False:
    print("Invalid Input!!!")
    exit()

num = int(num)
temp = num
sum = 0
while temp:
    val = temp % 10
    sum += math.factorial(val)
    temp //= 10

if sum == num:
    print("The number {0} is strong number".format(num))
else:
    print("The number {0} is not a strong number".format(num))
