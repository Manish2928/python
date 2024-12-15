import time

timespane = time.strftime('%H:%M:%S')
print (timespane)
hr = int(time.strftime('%H'))
hr = 22
if hr > 7 and hr< 12:
    print ("Good Morning. ")
elif hr > 12 and hr< 17:
    print ("Good Afternon. ")
elif hr > 17 and hr< 20:
    print ("Good Evning. ")
elif hr > 20 and hr< 22 :
    print ("Good Night. ")
else :
    print("Soja ")
    
