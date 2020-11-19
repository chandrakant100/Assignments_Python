# To find factorial of a number using recursion

def rec_fact(num):
    if num <= 1:
        return 1
    return num * rec_fact(num - 1)

num = int(input("Enter a number: "))

print("Factorial of {0} is {1}".format(num, rec_fact(num)))
