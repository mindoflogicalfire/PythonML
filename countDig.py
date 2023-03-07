n=int (input())
count=0
while n!=0:
    if(n%10==0):
        break
    else:
        count+=1
        n//=10
print(count)
# n= input("enterr a number")
# for x  in n:
#     if(x!=)