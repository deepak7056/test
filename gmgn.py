import time
t = time.strftime('%H:%M:%S')
hour = int (time.strftime('%H'))
hour = int (input("Enter hour"))

if(hour>0 and hour<=12):
  print("Good morning")
elif(hour>=12 and hour<=18):
  print("Good afternoon")
else:
  print("Good night")
