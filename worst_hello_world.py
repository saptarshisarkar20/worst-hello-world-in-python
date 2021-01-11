 
import random
import time
import os
def printLine(memory,expectedChar):
    #print (memory, end=' ')
    tempChar = random.randint(32,127)
    while True:
        print("\r"+"\033[1;"+str(random.randint(30,38))+";"+str(random.randint(40,49))+"m"+memory+chr(tempChar) , end='')
        if chr(tempChar) == expectedChar:
            break
        else:
            tempChar = random.randint(32,127)
        time.sleep(0.005)
    return 1
##Main
ourString = "Hello World !  "
memory = ""
print("Presenting to you the worst way to print Hello World.......")
time.sleep(2)
for c in ourString:
    printLine(memory,c)
    print()
    memory += c
time.sleep(1)
print("Good Bye......")