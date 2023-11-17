tup = (1,54,8,2,"Blue",True)
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[-2])

if 84946 in tup:
  print("yes it's in tuple")
else:
  print("it's not in tuple")

tup2 = tup[1:5]
print(tup2)
