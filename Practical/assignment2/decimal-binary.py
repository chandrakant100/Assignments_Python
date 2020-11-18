num = input("Enter the decimal number:")

if num.isnumeric() == 0:
    print("Its is string")
    exit()

num = int(num)
num1 = num

def binary(num,num1,temp):
  if num1 == 0:
    print ("The binary of {0} is:".format(num))
    return
  else:  
    temp = num1 % 2
    num1 //= 2
    binary(num,num1,temp)  
  print(temp,end = " ")
binary(num,num1,0)
print()        
