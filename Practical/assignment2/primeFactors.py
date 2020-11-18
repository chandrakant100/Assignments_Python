import math

num = input("Enter any number:")    

if num.isnumeric == False:
    print("Invalid Input!!!")
    exit()

num = int(num)
sum = 0
flag = 1

print("The Prime factors are: ")
for i in range(2,num):
    if num % i == 0:
        for j in range(2,i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            print(i,end = " ")    
        flag = 1

print()