x=0
x="dsdj"
x1,x2=1,4
print(x1," ",x2)
x1=x2=2,3
def fun1():
    print(x)
    global y  
    y=100
def fun2():
    y=10
    print(y)#pint 10 not 100
def fun3():
    print(y)#print 100 not 10 refers global variable
fun1()
fun2();fun3()