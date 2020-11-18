num1 = float(input("mark 1:" ))
num2 = float(input("mark 2:" ))
num3 = float(input("mark 3:" ))
num4 = float(input("mark 4:" ))
num5 = float(input("mark 5:" ))

avg = ((num1 + num2 + num3 +num4 + num5) / 500 ) * 100

if avg >= 90:
    print ("\nGrade O")

elif avg >= 80 and avg <90:
    print ("\nGrade E")
elif avg >= 70 and avg < 80:
    print ("\nGrade A")
elif avg >= 60 and avg < 70:
    print ("\nGrade B")
else:
    print ("\nGrade C")    
