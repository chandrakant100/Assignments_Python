print("---To find the gcd and lcm of two numbers---")
num1 = input("Enter number1:")
num2 = input("Enter number2:")

if num1.isnumeric() == 0 and num2.isnumeric() == 0:
    print("Its is string")
    exit()
num1 = int(num1)
num2 = int(num2)

temp1 = num1
temp2 = num2
while(temp1!=temp2):
	if(temp1 > temp2):
		temp1 = temp1-temp2
	else:	
		temp2 = temp2-temp1
gcd=temp1

print("The gcd of {0} and {1} is {2}".format(num1,num2,gcd))


    