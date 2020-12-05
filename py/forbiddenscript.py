#!/usr/bin/env python3
# Very dangerous, not for use without parental supervision.

import time
target=[]
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def splashscreen():
    for i in range(1,15):
        time.sleep(.020)
        print("")
    time.sleep(.200)
    print(bcolors.WARNING+"                        ..")
    time.sleep(.050)
    print("                      .oK0l")
    time.sleep(.050)
    print("                     :0KKKKd.")
    time.sleep(.050)
    print("                   .xKO0KKKKd")
    time.sleep(.050)
    print("                  ,Od' .d0000l")
    time.sleep(.050)
    print("                 .c;.   .'''...           ..'.")
    time.sleep(.050)
    print("    .,:cloddxxxkkkkOOOOkkkkkkkkxxxxxxxxxkkkx:")
    time.sleep(.050)
    print("    ;kOOOOOOOkxOkc'...',;;;;,,,'',;;:cllc:,.")
    time.sleep(.050)
    print("     .okkkkd,.lko  .......',;:cllc:;,,'''''.")
    time.sleep(.050)
    print("       .cdo. :xd' cd:.  ..';'',,,'',,;;;,'.")
    time.sleep(.050)
    print("          . .ddl.;doooc'..;oc;'..';::;,'.")
    time.sleep(.050)
    print("            coo;.oooolllllllcccc:'.  .")
    time.sleep(.050)
    print("           .ool''lllllccccccc:::::;.")
    time.sleep(.050)
    print("           ;lll. .':cccc:::::::;;;;'")
    time.sleep(.050)
    print("           :lcc:'',..';::::;;;;;;;,,.")
    time.sleep(.050)
    print("           :cccc::::;...';;;;;,,,,,,.")
    time.sleep(.050)
    print("           ,::::::;;;,'.  ..',,,,'''.")
    time.sleep(.050)
    print("            ........          ......")
    time.sleep(.050)
    print("            ```\n"+bcolors.ENDC)
    time.sleep(.400)
    print(" ▄  █ ██   ▄█▄    █  █▀ ▄███▄   █▄▄▄▄ █▀▄▀█ ██      ▄   TM")
    print("█   █ █ █  █▀ ▀▄  █▄█   █▀   ▀  █  ▄▀ █ █ █ █ █      █  ")
    print("██▀▀█ █▄▄█ █   ▀  █▀▄   ██▄▄    █▀▀▌  █ ▄ █ █▄▄█ ██   █ ")
    print("█   █ █  █ █▄  ▄▀ █  █  █▄   ▄▀ █  █  █   █ █  █ █ █  █ ")
    print("   █     █ ▀███▀    █   ▀███▀     █      █     █ █  █ █ ")
    print("  ▀     █          ▀             ▀      ▀     █  █   ██ ")
    print("       ▀                                     ▀          ")
    time.sleep(.100)
    print(bcolors.HEADER+bcolors.BOLD+"\nThank you for your ongoing support, welcome to HACKERMANtm.")
    print("Who would you like to hack today?"+bcolors.ENDC)
    time.sleep(.300)
    try:
        target.append(input(bcolors.FAIL+"Awaiting target... > "+bcolors.OKCYAN))
    except:
        exit()

def credits():
    print(bcolors.HEADER+bcolors.BOLD+"\nThank you for hacking with HACKERMANtm today.")
    print("You have successfully hacked",len(target)-1,"people!")
    print(bcolors.OKCYAN+"\nHave a nice day!"+bcolors.ENDC)
    time.sleep(0.950)
    for i in range(1,10):
        print("")
        time.sleep(0.020)

def hacker():
    try:
        print(bcolors.ENDC+"\nHacking..")
        time.sleep(.500)
        print(bcolors.WARNING+target[-1],"28% hacked.", end='\r')
        time.sleep(.900)
        print(target[-1],"61% hacked.", end='\r')
        time.sleep(.400)
        print(target[-1],"72% hacked.", end='\r')
        time.sleep(1.700)
        print(bcolors.OKGREEN+target[-1],"100% hacked.")
        time.sleep(.200)
        print(bcolors.ENDC+"Hack successful.")
        time.sleep(1.0)
    except:
        exit()

def hackdos():
    while True:
        try:
            print("\nWho else do you want to hack? (Leave blank for none)")
            time.sleep(.300)
            target.append(input(bcolors.FAIL+"Awaiting target... > "+bcolors.OKCYAN))
            if target[-1] != "":
                hacker()
            else:
                break
        except:
            break


def main():
    splashscreen()
    hacker()
    hackdos()
    credits()

if __name__ == "__main__":
    main()