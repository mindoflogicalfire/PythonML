flag=False
b=int(input("enter a number"))
if b<1:
    print("not a prime number")
elif b>1:
    for i in range(2,b):
        if b%i==0:
            flag=True
            break
    if flag:
        print("Not a prime Number")
    else:
        print("It is prime")