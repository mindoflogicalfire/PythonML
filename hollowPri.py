for x in range (10):
    for y in range(10):
        if x+y==9:
            print("* ",end=" ")
        else:
            print(" ",end=" ")
        if (x==9):
            print("* ",end=" " )
    for z in range(10,20):
        if x-y==9:
            print("* ",end=" ")
        else:
            print(" ",end=" ") 
        if (x==9):
            print("* ",end=" ")
    print()