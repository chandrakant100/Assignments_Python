num = input("Enter the Range  the fibonacci series:")

if num.isnumeric() == 0:
    print("Its is string")
    exit()
num = int(num)

num1 = 0 
num2 = 1

print (num1,num2,end = ' ')
for i in range(1,num-1):
    temp = num1 + num2
    num1 = num2
    num2 = temp    
    print(temp,end = ' ')
print()    
