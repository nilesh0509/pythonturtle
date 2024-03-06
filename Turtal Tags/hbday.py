import time
from random import randint

for i in range (1,1000):
    print("")
space =""

for i in range(1,10000):
    count=randint(1,1000)
    while(count>0):
        space+=''
        count-=1

    if(i%100==0):
        print(space +'HAPPY BIRTHDAY!🎂.')
    elif(i%90==0):
        print(space +'RAKSHU ! 🎂. ')
    elif(i%80==0):
        print(space +" 🎂. ")
    elif(i%50==0):
        print(space +" 🧡. ")
    elif(i%120==0):
        print(space +" ✨. ")
    elif(i%60==0):
        print(space +" 🎉. ")
    elif(i%40==0):
        print(space +" 🍫. ")
    elif(i%110==0):
        print(space +" 🥳. ")
    elif(i%70==0):
        print(space +" HAPPY BIRTHDAY RAKSHU !💖. ")
    else:
        print(space +" ⭐. ")
    
    space =""
    time.sleep(0.2)
        
