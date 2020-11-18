num1 = input("Enter the number1: ")
num2 = input("Enter the number2: ")
num3 = input("Enter the number3: ")

if num1.isnumeric() == 0 or num2.isnumeric() == 0 or num3.isnumeric() == 0:
    print("Input is not numeric!!!")
    exit()

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

if num1 > num2 and num1 > num3:
    print("{0} is greater than {1} and {2}".format(num1,num2,num3))

elif num2 > num1 and num2 > num3:
    print("{0} is greater than {1} and {2}".format(num2,num1,num3))

else:
    print("{0} is greater than {1} and {2}".format(num3,num1,num2))
    
