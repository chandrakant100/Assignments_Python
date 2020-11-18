num1 = input("Enter the number1: ")
num2 = input("Enter the number2: ")

if num1.isnumeric() == False and num2.isnumeric() == False:
    print("Numbers are not numeric!!!")
    exit()

num1 = float(num1)
num2 = float(num2)

print("Smaller is {0}".format(num1)) if num1 < num2 else print("Smaller is {0}".format(num2))


