# Create the allowed payloads for `Reflected XSS into HTML context with most tags and attributes blocked` lab from PortSwigger
> Check out lab from here: https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked

## Usage
```console
$ python3 ReflectedXSS.py --help
usage: ReflectedXSS.py [-h] -u URL -c COOKIE -tf TAGS_FILE -ef EVENTS_FILE [-o OUTPUT]

Create allowed payloads for PortSwigger lab of "Reflected XSS into HTML context with most tags and attributes blocked"

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     The target URL
  -c COOKIE, --cookie COOKIE
                        The HTTP cookie header value
  -tf TAGS_FILE, --tags-file TAGS_FILE
                        Pass tags file
  -ef EVENTS_FILE, --events-file EVENTS_FILE
                        Pass events file
  -o OUTPUT, --output OUTPUT
                        Save the results in normal file

Example: python3 ReflectedXSS.py --url https://web-security-academy.net --tags-file /path/tags.txt --events-file
/path/events.txt --cookie "session=tCZxFr4rWGGBatEbpilZ34OAFUsrzkI9"
```
#### The results:

![Output.png](https://github.com/Sec0gh/python-scripts/blob/main/XSS/Reflected%20XSS/Output.png)

#### Save the results into file:
```console
python3 ReflectedXSS.py --url https://0a2200fd0499edb3c00f9511003b0083.web-security-academy.net/ --tags-file tags.txt --events-file events.txt --cookie "session=TsWbozlou7WPLavzjdNeUu8Xb663RGmR" -o payloads.txt
```
