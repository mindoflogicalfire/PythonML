def myfunc(n):
  print(n)
  return lambda a : a * n


print(mydoubler(11))
print(mytripler(11))