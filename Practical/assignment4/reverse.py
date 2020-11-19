# To reverse a number

def reverse(num):
    result = 0
    
    while num != 0:
        rem = num % 10
        result = result * 10 + rem
        num //= 10
    
    return result


num = int(input("Enter a number:"))

print("Reverse of {0} is {1}".format(num, reverse(num)))
