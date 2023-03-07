for x in range(0,4):
    for y in range(0,4):
        if(x>=y):
            print("*",end=" ")
        else:
            print(" ",end= " ")
    for y in range(5,10):
        if x+y>=9:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for x in range(4,10):
    for y in range(0,4):
        if(x+y<=9):
            print("*",end=" ")
        else:
            print(" ",end= " ")
    for y in range(5,10):
        if x<=y:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    