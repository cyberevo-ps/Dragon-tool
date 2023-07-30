import socket
import os
os.system("clear")

print ("""\033[1;33m

          _   _                          _____
         | \ | |                        / ____|
         |  \| |_ __ ___   __ _ _ __   | (___   ___ __ _ _ __
         | . ` | '_ ` _ \ / _` | '_ \   \___ \ / __/ _` | '_ \ 
         | |\  | | | | | | (_| | |_) |  ____) | (_| (_| | | | |
         |_| \_|_| |_| |_|\__,_| .__/  |_____/ \___\__,_|_| |_|
                               | |
                               |_|
""")
def scan_ports(target, ports):

    print("\033[1;35mTARGET===> :\033[1;36m",target)


    open_ports = []
    closed_ports = []


    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)
        sock.close()


    if len(open_ports) > 0:
        print("""\033[1;32mOpen ports:
________________________""")
        for port in open_ports:
            print("\033[1;35mPort {} is \033[1;32mopen ● ".format(port))
    else:
        print("\033[1;34mNo open ports found")

    if len(closed_ports) > 0:
        print("""\033[1;31mClosed ports:
________________________""")
        for port in closed_ports:
            print("\033[1;35mPort {} is \033[1;31mclosed ● ".format(port))
    else:
        print("No closed ports found")



target = input("Enter IP address or website URL:\033[1;31m ")
ports = [80, 443, 21, 22, 23, 25, 53, 110, 143, 993, 995] 

scan_ports(target, ports)
