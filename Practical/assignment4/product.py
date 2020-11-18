import math

count = input("Enter total numbers want to multiply(max = 4):")

if count.isnumeric() == 0:
    print("It is a string!!!")
    exit()

count = int(count)
countNum = 1

def multiply(num1 = 1, num2 = 1, num3 = 1, num4 = 1):
    return num1*num2*num3*num4

if count > 4:
    print("Maximux intput is 4")
    exit()

for i in range(count):
    num = input("Enter number {0}:".format(i+1))

    if num.isnumeric == False:
        print("It is a string!!!")
        exit()
    num = int(num)
    countNum *= multiply(num)
print(countNum)    