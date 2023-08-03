#!/bin/dash
# Developed by Err0r_HB ~ HackBoyz Team 

echo "\033[1;92m Updating and Upgrading First..."
echo ""
sleep 1
apt update && upgrade -y
apt install -y wget
clear
k='\033[1;92m'
echo "\033[1;90m
         ░░░░░░███████]▄▄▄▄▄▄▄▄▃
         ▂▄▅█████████▅▄▃▂
        |███████████████████].
         ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤

    \033[0;32m ░▒▓\033[1;92m██████████►\033[1;95m╬\033[1;92m◄██████████\033[0;32m▓▒░
    \033[0;32m ░▒▓\033[1;92m██►\033[1;91m╔╦╦╦═╦╗╔═╦═╦══╦═╗\033[1;92m◄██\033[0;32m▓▒░
    \033[0;32m ░▒▓\033[1;92m██►\033[1;91m║║║║╩╣╚╣═╣║║║║║╩╣\033[1;92m◄██\033[0;32m▓▒░
    \033[0;32m ░▒▓\033[1;92m██►\033[1;91m╚══╩═╩═╩═╩═╩╩╩╩═╝\033[1;92m◄██\033[0;32m▓▒░
    \033[0;32m ░▒▓\033[1;92m██████████►\033[1;95m╬\033[1;92m◄██████████\033[0;32m▓▒░";
echo
echo "\033[1;96mDo You Want to Install Ngrok? [Y/n]"
read opcao
case $opcao in
y)
echo ""
echo "\033[1;93mDownloading Termux-ngrok..."
sleep 1
case `dpkg --print-architecture` in
aarch64)
    architectureURL="arm64" ;;
arm)
    architectureURL="arm" ;;
armhf)
    architectureURL="armhf" ;;
amd64)
    architectureURL="amd64" ;;
i*86)
    architectureURL="i386" ;;
x86_64)
    architectureURL="amd64" ;;
*)
    echo "\033[1;91mUnknown Architecture"
esac

wget "https://github.com/tchelospy/NgrokTest/blob/master/ngrok-stable-linux-${architectureURL}.zip?raw=true" -O ngrok.zip
unzip ngrok.zip
cat ngrok > /data/data/com.termux/files/usr/bin/ngrok
chmod 700 /data/data/com.termux/files/usr/bin/ngrok
rm ngrok ngrok.zip
clear
echo "${k}███╗   ██╗ ██████╗ ██████╗  ██████╗ ██╗  ██╗";
echo "${k}████╗  ██║██╔════╝ ██╔══██╗██╔═══██╗██║ ██╔╝";
echo "${k}██╔██╗ ██║██║  ███╗██████╔╝██║   ██║█████╔╝ ";
echo "${k}██║╚██╗██║██║   ██║██╔══██╗██║   ██║██╔═██╗ ";
echo "${k}██║ ╚████║╚██████╔╝██║  ██║╚██████╔╝██║  ██╗";
echo "${k}╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝";
sleep 1
echo "
……………..  ^v^
⋱ ⋮ ⋰
⋯ ◯ ⋯¨. ︵ ……………………………………….     ^v^
¨︵¸︵( ░░ )︵.︵.︵………….. ^v^
(´░░░░░░ ‘) ░░░’ )  )
`´︶´¯`︶´`︶´︶´`︶…..^v^………   . ^v^
……………………………………..   ︵.︵
…….………………………………. (˛. *˛.)…….. ^v^
………………………………….. (˛˛. *。 )
……….…………. (˛* ˛*˛* )


      ˛_Π_____.
……………./______/~＼…………\..|.|
˛╬╬╬╬╬˛°.｜田田 ｜門｜╬╬╬╬╬—╬╬╬╬╬
╔═══'•'๑۩۞۩๑•══•๑۩۞۩๑•══•๑۩۞۩๑•══•๑۩۞۩๑'•'═══╗";
echo ""
echo ""
echo "\033[1;92mSuccesfully Done !!"
echo ""
sleep 1
echo "\033[1;97mCommand Example (\033[1;95mngrok http 80\033[1;97m) \n\nOr ngrok For Help" 
echo ""

;;

n)
clear
echo "\033[1;91mCan't be Able to Install Ngrok Properly:("
echo ""
esac



