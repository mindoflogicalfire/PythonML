str=input("enter a string")
vo='aeiouAEIOU'
# for x in str:
#     if x.isalpha():
#         if x=='a'or x=='A'or x=='e'or x=='E'or x=='i'or x=='I'or x=='o'or x=='O'or x=='u'or x=='U':
#             print (x,"=vowel")
#         else:
#             print(x,"=consonant")
#     else:
#         print(x ,"is numeric or white space")
for x in str:
    if x.isalpha():
        if x in vo:
            print("2")
            print ("{} is a vowel".format(x))
        else:
            print("{} is consonant".format(x))
    else:
        print("{} is not a alphabet".format(x))
