
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
