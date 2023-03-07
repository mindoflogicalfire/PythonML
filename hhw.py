# import module as md
# # md.sum(3,5)
# import datetime as dt
# x=dt.datetime.now()
# print(x)
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.hour)
# print(x.min)
# print(x.second)

try:
    6
except NameError:
    print("not defined")
except SyntaxError:
    print("Syntax error")
except InterruptedError:
    print(InterruptedError)

except:
    print("not defines   uu")
else:
    print("sucess!!!!!!!!")