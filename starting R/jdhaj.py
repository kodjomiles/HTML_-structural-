# def rgb(r, g, b):
#     empty = (r,g,b)
#     char = ''
#     for number in empty:
#         a = number//16
#         b = number%16
#         if a < 0:
#             char += str(0)
#         if a <= 9:
#           char += str(a)
#         elif a == 10:
#           char += "A"
#         elif a == 11:
#           char+= "B"
#         elif a == 12:
#           char += "C"
#         elif a == 13:
#           char += "D"
#         elif a == 14:
#           char += "E"
#         else:char += "F"
#         if b < 0:
#             char +=str(0)
#         if b <= 9:
#           char += str(b)
#         elif b == 10:
#           char += "A"
#         elif b == 11:
#           char += "B"
#         elif b == 12:
#           char += "C"
#         elif b == 13:
#           char += "D"
#         elif b == 14:
#           char += "E"
#         else:char += "F"
#     return char
# print(rgb(0,255,125))
    

Numstring = "54 65 74 100 99 68 86 180 90"
divv = Numstring.split(" ")
for x in divv:
  print(sum(x))