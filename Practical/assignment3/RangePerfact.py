import math

num1 = input("Enter Starting point:")        
num2 = input("Enter ending point:")        

if num1.isnumeric == False or num2.isnumeric() == False:
    print("Invalid Input!!!")
    exit()

num1 = int(num1)
num2 = int(num2)
sum = 0

print("The perfact numbers between {0} and {1} are:".format(num1,num2))
for j in range(num1,num2):
    for i in range(1,j):
        if j % i == 0:
            sum += i
    if sum == j:
        print(j,end = ' ')
    sum = 0         

print()
