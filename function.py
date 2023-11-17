def calculation(a,b):
  mean = (a*b)/(a+b)
  print(mean)

def greater(a,b):
  if(a>b):
    print("1st number is greater ")
  else:
    print("2nd number is greater or equal")
def Lesser(a,b):
  pass
  
    

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
calculation(a,b)
greater(a,b)

c = int(input("Enter value of c: "))
d = int(input("Enter value of d: "))
calculation(c,d)
greater(c,d)
