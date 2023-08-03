import time
import sys
import instaloader
import colorama
from colorama import init, Style, Fore, Back
import pyshorteners
import requests
import os
import re

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Call clear function to clear the screen
clear()

banner = '''\033[1;36m
 
    ____           __  __          __   ____           __       
   / __ )____     / / / /_  ______/ /  /  _/___  _____/ /_____ _
  / __  / __ \   / /_/ / / / / __  /   / // __ \/ ___/ __/ __ `/
 / /_/ / /_/ /  / __  / /_/ / /_/ /  _/ // / / (__  ) /_/ /_/ / 
/_____/\____/  /_/ /_/\__, /\__,_/  /___/_/ /_/____/\__/\__,_/  
                     /____/                                     
'''
print(banner)

#animation Text
def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.1)

text = Back.RED + "Hello, Hackers my name is :  BO HAYDAR" + Style.RESET_ALL
animate_text(text)


# The rest of your program goes here

session = requests.Session()
session.proxies = {'http': 'http://10.10.1.10:3128', 'https': 'http://10.10.1.10:1080'}

# Prompt the user to enter an Instagram username
username = input('\033[1;32m\n\nEnter an Instagram username ➤ ')

# Retrieve the profile information for the given username

# Create an instance of Instaloader
L = instaloader.Instaloader()
#Banner
#profilling
profile = instaloader.Profile.from_username(L.context, username)

# Get the verification status of the user's Instagram account
is_verified = profile.is_verified

# Get profile image
profile_pic_url = profile.profile_pic_url

# Create a Shortener object
s = pyshorteners.Shortener()

# Shorten the URL using the default shortening service (TinyURL)
short_url = s.tinyurl.short(profile_pic_url)

# Get the external URL associated with the user's profile
external_url = profile.external_url

# Get the business account status of the user's Instagram account
is_business_account = profile.is_business_account

# Count the number of videos in the profile's posts
video_count = 0
for post in profile.get_posts():
    if post.is_video:
        video_count += 1

# Grab email & contact
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)

# Print the profile information
print(Fore.GREEN + '------------------------------------\n')
print('\033[36mUsername:\033[0m', profile.username)
print('\033[36mUser id:\033[0m', profile.userid)
print('\033[36mFull Name:\033[0m', profile.full_name)
print('\033[36mBio:\033[0m', profile.biography)
print('\033[36mEmails id:\033[0m', emails)
print('\033[36mFollowers:\033[0m', profile.followers)
print('\033[36mFollowing:\033[0m', profile.followees)
print('\033[36mPosts:\033[0m', profile.mediacount)
print('\033[36mNumber of videos:\033[0m', video_count)
#print(Fore.GREEN + 'Number of reel:', reel_count)
#print(Fore.GREEN + 'Number of image:', image_count)
print('\033[36mPrivacy status:\033[0m', profile.is_private)
print('\033[36mIs verified:\033[0m', is_verified)
print('\033[36mExternal URL:\033[0m', external_url)
print('\033[36mIs business account:\033[0m', profile.is_business_account)
print('\033[36mProfile picture URL:\033[0m', short_url)
#print(Fore.GREEN + 'Join recently:', profile.is_joined_recently)
#print(Fore.GREEN + 'Get Post', profile.get_posts())

print('\n\033[1;31mThis tool created by @ethicalprince \nFor stop CTRL + z\033[0m\n')

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Example usage
# Ask user if they want to restart
response = input("\033[1;33mDo you want to restart the program? (y/n)\033[0m ")

if response.lower() == "y":
    print(Fore.RED + "\033[1;31m\nRestarting program...\033[0m")
    restart_program()
else:
    print("Exiting program. Thanks for using ;")
