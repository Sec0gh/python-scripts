# Automated script to exploit the logic flaw in the `Infinite money logic flaw` Lab from `PortSwigger`
## Check out the [Infinite money logic flaw lab](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-infinite-money)#

## Usage
```
$ python3 ExploitLogicFlaw.py -h
usage: ExploitLogicFlaw.py [-h] [-c COOKIES] [-k CSRF_TOKEN] URL

Example: python3 ExploitLogicFlaw.py URL -c "r8Gy0Re1rWhd3oThg5Doe5s3g2LTpmM3" -k "mWrQTthUTmZJAcZN1lhm11hz6OPKc2Y1"

positional arguments:
  URL                   The target URL

options:
  -h, --help            show this help message and exit
  -c COOKIES, --cookies COOKIES
                        The session value in the cookie header of the request
  -k CSRF_TOKEN, --csrf-token CSRF_TOKEN
                        CSRF token of the request body
```

## Example
```
python3 ExploitLogicFlaw.py "https://0a98002d0427372dc0693b9f00a6008e.web-security-academy.net" -c "ntGcf13obpSj9NBlGtEFGZUqRjv4dC0W" -k "WripMDGS5mX6TFJI9KLhzUj6JzPckMtN"
```

## Output
- The output will look like that and you will find there is an increase in the credit store:

![ScriptOutput](https://github.com/Sec0gh/python-scripts/blob/main/Infinite%20money%20logic%20flaw/Lab13_ScriptOuptut.png)
