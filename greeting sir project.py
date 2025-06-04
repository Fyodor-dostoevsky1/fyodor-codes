import time
a = input('enter your name :')
print('Hello',a)

timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = time.strftime('%H')
print(hour)
minute = time.strftime('%M')
print(minute)
second = time.strftime('%S')
print(second)

if int(hour) < 12:
 print('GOODMORNING ', a)
 
elif int(hour)<= 18:
    print('GOODEVENING ', a)
else:

   print('GOODNINGHT', a)



   