# day = int(input("Enter the day number"))

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case _:
#         print("Invalid day")

# if(day == 1):
#     print("Monday")
# elif(day==2):
#     print("Tuesday")
# elif(day==3):
#     print("Wednesday")
# else:
#     print("Invalid Day")
print('''
1.English
2.Hindi
3.Gujrati
''')
language = int(input("Press number for language: "))

match language:
    case 1:
        print("English langauge Selected")
    case 2:
        print("Hindi langague selected")
    case 3:
        print("Gujrati Langague selected")
    case _:
        print("Invalid language selection")
