# Very dangerous, not for use without parental supervision.

import time

def hacker():
    print("\nHacking..\n")
    time.sleep(.500)
    print("\t",target,"28% hacked.", end='\r')
    time.sleep(.900)
    print("\t",target,"61% hacked.", end='\r')
    time.sleep(.400)
    print("\t",target,"72% hacked.", end='\r')
    time.sleep(2)
    print("\t",target,"100% hacked.")
    print("\nHack successful. (took 3.8 seconds)")
    print(target, "has been pwned.")

print("Who do you want to hack?")
target = input()
hacker()