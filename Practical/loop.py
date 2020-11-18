num = int(input("Enter the range:"))

for i in range(num):
    for j in range(i+1):
        print(i+1,end = " ")
    print()