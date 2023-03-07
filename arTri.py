import math
'''----------------area of triangle-------------------'''
print("sides of triangle")
A=float(input("A:"))
B=float(input("B:"))
C=float(input("C:"))
semiPeri=(A+B+C)/2

ar=math.sqrt(semiPeri*(semiPeri-A)*(semiPeri-B)*(semiPeri-C))
print("area ",ar)
