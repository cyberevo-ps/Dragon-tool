#import os
#os.system('clear')
from __future__ import print_function
try:
    from googlesearch import search

except ImportError:
    print("")

import sys
import time
import os

# Dorks Eye v1.0
os.system('clear')

if sys.version[0] in "2":
    print ("\n[x] ..n00b.. BO HAYDAR DORKS Is Not Supported For python 2.x Use Python 3.x \n")
    print ("\n\n\tBO HAYDAR DORKS\033[1;91mI 7T NAJMA LA AL ADAA\033[0m😃\n\n")
    exit()


class colors:
    CRED2 = "\033[0;35m"
    CBLUE2 = "\033[1;33m"
    ENDC = "\033[1;32m"


banner = ("""
       ____           __  __                __
      / __ )____     / / / /___ ___  ______/ /___ ______
     / __  / __ \   / /_/ / __ `/ / / / __  / __ `/ ___/
    / /_/ / /_/ /  / __  / /_/ / /_/ / /_/ / /_/ / /
   /_____/\____/  /_/ /_/\__,_/\__, /\__,_/\__,_/_/
                              /____/
""")

for col in banner:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

x = ("""
       _____________________________________________
       |Youtube:https://youtube.com/@BO_HAYDAR_HK  |
       |Tele:https://t.me/txrtm                    |
       |Tele Team:https://t.me/+EHo65POl1yA2ZjA0   |
       |___________________________________________|""")
for col in x:
    print(colors.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

y = "\n\t\tTOOL BY BO HAYDAR - BLACK EGO \n"
for col in y:
    print(colors.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)

z = "\n"
for col in z:
    print(colors.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


try:
    data = input("\033[1;32m[+] Do You Like To Save The Output In A File? (Y/N) ").strip()
    l0g = ("")

except KeyboardInterrupt:
        print ("\n")
        print ("\033[1;91m[!] User Interruption Detected..!\033[0")
        time.sleep(0.5)
        print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
        time.sleep(0.5)
        sys.exit(1)


def logger(data):
    file = open((l0g) + ".txt", "a")
    file.write(str(data))
    file.write("\n")
    file.close()


if data.startswith("y" or "Y"):
    l0g = input("[~] Give The File a Name: ")
    print ("\n" + "  " + "»" * 78 + "\n")
    logger(data)
else:
    print ("[!] Saving is Skipped...")
    print ("\n" + "  " + "»" * 78 + "\n")


def dorks():
    try:
        dork = input("\n[+] Enter The Dork Search Query: ")
        amount = input("[+] Enter The Number Of Websites To Display: ")
        print ("\n ")

        requ = 0
        counter = 0

        for results in search(dork, tld="com", lang="en", num=int(amount), start=0, stop=None, pause=2):
            counter = counter + 1
            print ("[+] ", counter, results)
            time.sleep(0.1)
            requ += 1
            if requ >= int(amount):
                break

            data = (counter, results)

            logger(data)
            time.sleep(0.1)

    except KeyboardInterrupt:
            print ("\n")
            print ("\033[1;91m[!] User Interruption Detected..!\033[0")
            time.sleep(0.5)
            print ("\n\n\t\033[1;91m[!] I like to See Ya, Hacking \033[0m😃\n\n")
            time.sleep(0.5)
            sys.exit(1)

    print ("[•] Done... Exiting...")
    print ("\n\t\t\t\t\033[34mHYDAR DORK\033[0m")
    print ("\t\t\033[1;91m[!] Good luck, go hack the site  \033[0m😃\n\n")
    sys.exit()


# =====# Main #===== #
if __name__ == "__main__":
    dorks()
