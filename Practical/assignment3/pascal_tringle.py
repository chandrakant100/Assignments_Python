'''
    PROGRAM - WAP TO PRINT PASCAL TRINGLE
    FILE    - pascal_tringle.py
    CRATED BY - Lasani Prusty
    DATED - 30.09.20
'''
line = int(input('Enter the line numbers:'))
for i in range(0,line):
    for j in reversed(range(i,line)):
        print(" ",end = '')
    temp = 1
    for j1 in range(0,i+1):
        print(temp,end=' ')
        temp = temp * (i-j)//(j+1)
    print()
        
