import sys
import os
import argparse
from urllib.parse import urlparse
from requests import post

os.system('clear')
banner2 ="""
         ___________________________________________
        |Youtube:https://youtube.com/@BO_HAYDAR_HK  |
        |Tele:https://t.me/txrtm                    |
        |Tele Team:https://t.me/+EHo65POl1yA2ZjA0   |
        |___________________________________________|
"""
banner3 ='   THE TOOL BY BO HAYDAR FOR CAT LINK FOR THE PHISHING'


banner = r"""

     ___        _  _              _             ___      _
    | _ ) ___  | || |__ _ _  _ __| |__ _ _ _   / __|__ _| |_
    | _ \/ _ \ | __ / _` | || / _` / _` | '_| | (__/ _` |  _|
    |___/\___/ |_||_\__,_|\_, \__,_\__,_|_|    \___\__,_|\__|
                          |__/
"""

def Shortner(big_url: str) -> str:
    """
    Function short the big urls to short
    """
    return post(f"https://is.gd/create.php?format=json&url={big_url}").json()['shorturl']


def MaskUrl(target_url: str, mask_domain: str, keyword: str) -> str:
    """
    Function mask the url with given domain and keyword
    """
    url = Shortner(target_url)
    return f"{mask_domain}-{keyword}@{urlparse(url).netloc + urlparse(url).path}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mask the URL behind the another URL")

    parser.add_argument(
        "--target",
        type=str,
        help="Enter link:",
        required=True,
    )
    parser.add_argument(
        "--mask",
        type=str,
        help="Mask URL (With http or https)",
        required=True,
    )
    parser.add_argument(
        "--keywords",
        type=str,
        help="Keywords (Use (-) instead of whitespace)",
        required=True,
    )

    print(f"\033[1;35m {banner}\033[1;33m")
    print(f"\033[1;36m {banner2}\033[1;36m")
    print(f"\033[1;32m {banner3}\033[1;32m")

    if len(sys.argv) == 1:
        print("\n")
        target = input("\033[1;33m [+] Enter the link =====>  : ")
        mask = input("\033[1;33m [+] Enter the link mask ====>  : ")
        keyword = input("\033[1;33m [+] Enter the ENTER in the keyboard ==> : ")
        print("\n")
    else:
        args = parser.parse_args()
        target = args.target
        mask = args.mask
        keyword = args.keywords

    print(f"\033[1;35m the link ==>\033[0;32m  {MaskUrl(target, mask, keyword)} \033[1;35m")

