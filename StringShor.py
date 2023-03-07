# x=input("some comma seprates value")
# y=x.split(",")
# print(y)
# print(tuple(y))
# print(set(y))

fiName=input("enter file name")
fex=fiName.split(".")
print(fex[-1])
flag=False
for i in fiName: 
    if(fiName.islower()):
        flag =True
