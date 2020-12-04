# Very dangerous, not for use without parental supervision.
#!/usr/bin/env python
import time
target=[]

def hacker():
    print("\nHacking..")
    time.sleep(.500)
    print(target[-1],"28% hacked.", end='\r')
    time.sleep(.900)
    print(target[-1],"61% hacked.", end='\r')
    time.sleep(.400)
    print(target[-1],"72% hacked.", end='\r')
    time.sleep(2)
    print(target[-1],"100% hacked.")
    print("Hack successful.")

print("\nWho do you want to hack?")
target.append(input())
hacker()

while True:
    try:
        print("\nWho else do you want to hack? (Leave blank for none)")
        target.append(input())
        if target[-1] != "":
            hacker()
        else:
            break
    except:
        break

print("Thank you for hacking today.")
print("You have successfully pwned",len(target)-1,"people.")
print("Have a nice day!")