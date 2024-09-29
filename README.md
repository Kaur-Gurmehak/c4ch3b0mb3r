
# C4ch3 B0mb3r -> CPDOS Automation Tool

Cache-Poisoned Denial-of-Service (CPDoS) is a new class of web cache poisoning attacks aimed at disabling web resources and websites.
Three variants of CP-DOS are:
1. HTTP Meta Character (HMC):
In this method, attackers exploit special characters (metacharacters) in HTTP requests to cause server-side processing delays. By injecting these characters strategically into the request, they can disrupt the parsing process and induce excessive resource consumption on the server.

2. HTTP Header Oversize (HHO):
This attack involves sending HTTP requests with abnormally large headers. When the server receives such requests, it may allocate significant resources to process and parse the oversized headers, leading to resource exhaustion and denial of service for legitimate users.

3. HTTP Method Override (HMO):
Attackers exploit HTTP method override mechanisms to send requests that mimic legitimate HTTP methods (e.g., GET, POST, PUT) but are actually designed to overload server resources. By manipulating headers or request parameters, attackers trick the server into performing unintended and resource-intensive operations.

Some other methodologies include-

1. HTTP Header Fragmentation:
Here, attackers send fragmented HTTP headers across multiple packets. This fragmentation can confuse the server's parsing logic and cause it to allocate excessive resources trying to reconstruct and process the fragmented headers. As a result, the server becomes overwhelmed and unable to respond to legitimate requests.

2. HTTP Request Smuggling:
HTTP request smuggling attacks involve manipulating the interpretation of HTTP requests by proxy servers or other intermediaries. Attackers exploit inconsistencies in how different components interpret HTTP request headers and body content to smuggle malicious requests past security controls. This can lead to resource exhaustion or other forms of denial of service.


C4ch3 B0mb3r is a Python-based HTTP request generator that can be used for various purposes, such as testing web application security, load testing, and network performance testing. It allows users to send HTTP requests with custom headers, payloads, and parameters, and supports multiple payload types, including HTTP Metachar Header, Oversized HTTP Header, HTTP Method Override, HTTP Header Fragmentation & HTTP Request Smuggling.

The tool is designed to be easy to use and customizable, with options for setting the number of threads, timeout, and cachebomber mode with color-coded output for better readability.

Some Important Points:

* The tool uses a hit & trial approach, so please try a few times as it may give false negatives.
* If a payload doesn't works, try refreshing the page and trying the tool again.
* As it is difficult to pentest the vulnerability on real-time websites or content-delivery-networks so, for demonstration purposes, a vulnerable web server {app.py} is provided and it simulates how the tool will work.
* If a 200 OK response is not obtained, visit the URL to see if the response is actually cached. Try refreshing a few times.
* A website may / maynot be vulnerable to all the payloads.
* The tool is a prototype & is currently in development phase, It is an atempt to simulate CPDOS attack, but still more research is needed.






## Installation

To install the tool using git clone, follow these steps:

1. Open a terminal window.
2. Navigate to the directory where you want to install the tool.
3. Clone the repository using the following command:
```bash
git clone https://github.com/Kaur-Gurmehak/c4ch3b0mb3r.git
```
4. Navigate to the cloned directory using cd command.
5. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
 
```
6. First run the target server to demonstrate the attack.
```bash
python3 ./app.py
```
6. Use the command to run the tool in another terminal on the url of the app {or} url of the target.
```bash
python3 c4ch3b0mb3r.py -h
```

## Usage/Examples

For detailed information about options, run the command:

```python
python3 c4ch3b0mb3r.py -h
```

To use the tool, simply run the script using python with the desired options and parameters. 

For example, to send a payload with the HTTP Metachar Header payload type to a target URL, you can use the following command:

```python
python3 c4ch3b0mb3r.py -u http://127.0.0.1:5000 -p 3 
```


## Directory Map

```bash
c4ch3b0mb3r/
├── tool.py
├── requirements.txt
├── README.md
|__ app.py
```

##POC

Usage of the tool, 

![Screenshot 2024-05-03 220245](https://github.com/Kaur-Gurmehak/c4ch3b0mb3r/assets/91598188/aab8c719-50cf-43c7-b83c-8e619f754bc8)

Accessing the vulnerable server on browser,

![Screenshot 2024-05-03 211723](https://github.com/Kaur-Gurmehak/c4ch3b0mb3r/assets/91598188/7da4d9c1-df9d-436f-9b07-ef1c744a7be0)

Default command,

![Screenshot 2024-05-03 211831](https://github.com/Kaur-Gurmehak/c4ch3b0mb3r/assets/91598188/67a5d68e-df0b-4b36-9a96-634c289a5abc)

After refreshing the browser,

![Screenshot 2024-05-03 211859](https://github.com/Kaur-Gurmehak/c4ch3b0mb3r/assets/91598188/52e22469-210d-475f-90cc-cf6d5a614f24)

Some other payload examples,

![Screenshot 2024-05-03 213604](https://github.com/Kaur-Gurmehak/c4ch3b0mb3r/assets/91598188/a4efb34c-14f8-4ce9-b093-f59fa88ee8f7)
![Screenshot 2024-05-03 211629](https://github.com/Kaur-Gurmehak/c4ch3b0mb3r/assets/91598188/f985e39a-c9fe-469a-8b09-284ab091de1e)
![Screenshot 2024-05-03 213508](https://github.com/Kaur-Gurmehak/c4ch3b0mb3r/assets/91598188/bd80387b-7ab0-43a6-b0d6-f16b7212b314)
-6b6bd91e1b70)



## References

1. https://cpdos.org/
2. https://www.acunetix.com/blog/web-security-zone/cache-poisoning-dos-attack-techniques/
3. https://securityaffairs.com/92859/hacking/cpdos-attack-cdns.html
4. https://www.bleepingcomputer.com/news/security/new-cpdos-web-cache-poisoning-attacks-impact-sites-using-popular-cdns/
5. https://gbhackers.com/cpdos/
6. https://www.reblaze.com/wiki/ddos/cpdos-attack/
7. https://cpdos.org/paper/Your_Cache_Has_Fallen__Cache_Poisoned_Denial_of_Service_Attack__Preprint_.pdf
