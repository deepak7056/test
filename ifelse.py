a = int (input("Enter the value of a : "))

if(a<0) :
    print("A is negative")
elif(a>0) :
     if(a<=10):
      print("A is btw 1-10")
     elif(a>10 and a<=20) :
      print("A is btw 10-20")
     else:
      print("A is greater than 20")
else:
    print("A is zero")
