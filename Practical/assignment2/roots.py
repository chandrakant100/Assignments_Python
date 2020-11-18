'To find the roots of the quadratic eqation'

import math

print ("Eqation format:\nax^2 + bx +c")

print ("Enter a,b,c respectively:\n")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = (b * b) - (4 * a * c)

if (d == 0):
    print ("The eqauation has only one root:\n")
    root = (-b + math.sqrt(d)) / 2*a
    print ("Root: ",root)  

elif (d > 0):
        root1 = (-b + math.sqrt(d)) / 2*a
        root2 = (-b - math.sqrt(d)) / 2*a
        print("The Equation has two roots:\n")
        print("Root 1:",round(root1,1),"\nRoot 2",round(root2,1))

else:
    print ("The equation has two imaginary roots!!!")  

    
    

