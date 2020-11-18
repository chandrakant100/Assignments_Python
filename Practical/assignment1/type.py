data = input("Enter any data:")

if data.isnumeric() == False:
    print("The data {0} is string type.".format(data))

data = float(data)    

if data % 1 == 0:
    print("The data {0} is integer type.".format(data))
else:
    print("The data {0} is float type.".format(data))


        
        