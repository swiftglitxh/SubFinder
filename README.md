![sub](https://user-images.githubusercontent.com/72777943/194553599-f5117435-6475-46d7-a859-984ba3abf3b1.png)


## 📓 SubFinder {v 0.3}
SubFinder is a dictionary attack tool to find websites subdomains

## ⌨️ Commands
```
Usage:
  subfinder[flags]

Flags:
  -h, --help               Help for arguments
  -w, --website string     Choose a website to target
  -l, --wordlist           Choose a wordlist to use    
  -v, --version            Show what version of SubFinder you have
  -t, --threads            Number of threads to use for scanning (default: 10)
```
## 🕵🏼‍♂️ How to run SubFinder?
```
python3 subfinder.py -w https://www.google.com -l /usr/share/wordlists/rockyou.txt -v --threads 30
```
##  🔨 Updates
**Version 0.1** 
- SubFinder now lets users choose their own file to use when preforming their attack
**Version 0.2**
- Bug Fixes 
**Version 0.3**
- Threads have been added into Subfinder
- Version argument has been added to allow you to check which version of SubFinder you have
- SubFinder is now `x5` faster then previous versions 

##Example Code
```
 ____  _  _  ____  ____  __  __ _  ____  ____  ____ 
/ ___)/ )( \(  _ \(  __)(  )(  ( \(    \(  __)(  _ \
\___ \) \/ ( ) _ ( ) _)  )( /    / ) D ( ) _)  )   /
(____/\____/(____/(__)  (__)\_)__)(____/(____)(__\_) Version: 0.3
=====================================================
    *** SubFinder is still under development ***


[=] Discovering Subdomains for google.com


[+] Discovered Subdomain: http://www.images.google.com 
[+] Discovered Subdomain: http://www.news.google.com 
[+] Discovered Subdomain: https://www.news.google.com 
[+] Discovered Subdomain: http://www.photos.google.com 
[+] Discovered Subdomain: https://www.photos.google.com 
[+] Discovered Subdomain: https://www.docs.google.com 
[+] Discovered Subdomain: http://www.docs.google.com 
...
[!] Scan Complete
[+] Scan Took: 3 seconds to finish
[=] Discovered: 31

*** Please Note Some Results May Not Be 100% ***
```
## Language:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
