
#PROGRAM - WAP TO FIND GCD OF TWO NUMBERS USING FUNCTION.


def find_gcd(a,b):
    i = 1
    while i==1:
        if a==b:
            return a
            break
        elif a>b:
            a = a-b
        elif b>a:
            b = b-a
#start of main()
print('Enter two integers:')
num1 = int(input())
num2 = int(input())
gcd = find_gcd(num1,num2)
print('GCD of {0} and {1} is {2}'.format(num1,num2,gcd))
