import sys,time
import os
os.system("clear")
s = """
\033[1;32m
    _   __                 __      ____             _
   / | / /___ __________  / /__   / __ \____  _____/ /______
  /  |/ / __ `/ ___/ __ \/ //_/  / /_/ / __ \/ ___/ __/ ___/
 / /|  / /_/ / /  / /_/ / ,<    / ____/ /_/ / /  / /_(__  )
/_/ |_/\__, /_/   \____/_/|_|  /_/    \____/_/   \__/____/
      /____/

\033[0;35m
 ___________________________________________________________
|___________________________________________________________|
\033[1;36m

               [1]==> http 8080
               [2]==> http 4444
               [3]==> http 80
               [4]==> tcp 8080
               [5]==> tcp 4444
               [6]==> tcp 80

               [00]==> Exit Tool
\033[0;35m
 ___________________________________________________________
|___________________________________________________________|
"""
for i in s:
     time.sleep(0.01)
     sys.stdout.write(i)
     sys.stdout.flush()
vvvv = input('''\033[1;34m


            Enter Number\033[1;35m ==> √  \033[1;36m:    ''')

if vvvv =='' :
   os.system("python Dragon-Tool.py")
elif vvvv =="00" :
   os.system("python Dragon-Tool.py")
elif vvvv =="1" :
   os.system("ngrok http 8080")
elif vvvv =="2" :
   os.system("ngrok http 4444")
elif vvvv =="3" :
   os.system("ngrok tcp 8080")
elif vvvv =="4" :
   os.system("ngrok tcp 4444")
elif vvvv =="5" :
   os.system("ngrok tcp 80")
