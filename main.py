
import random
import sys
import time

#checks whether you have a name, and if not, prompts you to input one
a=open("info.txt","a")
a.close()
with open("info.txt","r") as f:
    global named
    if(f.readline()==""):
        named=False
    else:
        named=True
if(named==False):
    with open("info.txt","w") as f:
        name=input("please input a name: ")
        f.write(name)
else:
    pass

roomCount = 0

def genRoom():
    global roomCount
    roomCount += 1
    i = random.randint(1,4)
    if(roomCount==5):
        print("You found a portal!")
    elif(i==1):
        print("you found an enemy!")
    elif(i==2):
        print("you found a treasure chest!")
    elif(i==3):
        print("you found a campfire")
    elif(i==4):
        print("you found a strange event")
    else:
        print("something went wrong.")
    
while True:
    genRoom()
    time.sleep(3)
