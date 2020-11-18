import math

num = input("Enter the square root of the number:")
if num.isnumeric() == 0:
    print("Its is string")
    exit()
result = math.sqrt(float(num))

if result % 2 == 0 or result % 2 == 1:
    print("The number {0} is a perfact square number".format(num))
else:
    print("The number {0} is not a perfact square number".format(num))

