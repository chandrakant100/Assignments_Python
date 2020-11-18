num = int(input("Enter the number: "))
fact = 1
temp = num
if num ==1:
    print ("Factoiral is 1")
elif num < 1:
    print("Factorial does'nt exist!!!")
else:        
    while num!=1:
        fact *= num
        num -= 1
    print ("The Fcatorial of number ",temp," is ",fact)