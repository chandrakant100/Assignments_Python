num = input("Enter the the poition of the fibbonacci term: ")

if num.isnumeric() == False:
    print("It is a string!!!")
    exit()

num = int(num)
def fibbo(num):
    if num < 0:
        print("Invalid input")
        exit()
    elif num == 0:
        return 0
    elif num == 1:
        return 1    
    return fibbo(num-1) + fibbo(num-2)
    

print(fibbo(num-1))
