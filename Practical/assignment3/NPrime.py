import math

num = input("Enter range number:")    

if num.isnumeric == False:
    print("Invalid Input!!!")
    exit()

num = int(num)
sum = 0
flag = 1

print("The Prime numbers upto {0} are: ".format(num))
for i in range(2,num):
        for j in range(2,i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            print(i,end = " ")    
        flag = 1

print()