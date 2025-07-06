import time
Today= time.strftime('%H:%M:%S')
print(Today)
h=time.strftime('%H')
print(h)
time_hour =int(time.strftime('%H')) 
#while(i==1):
if(0<time_hour<12):
   print("good morning")
elif(12<=time_hour<=4 ):
   print("good afternoon")
else:
   print("good night")   

 

    