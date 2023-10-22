
![New Project](https://github.com/swiftglitxh/SubFinder/assets/72777943/c73b9581-d3fd-4ead-9130-77d0db8ae3a9)

## 📓 SubFinder {v 0.3}
SubFinder is a versatile and efficient subdirectory discovery tool designed for web security and penetration testing. This Python-based tool empowers ethical hackers, security professionals, and researchers to uncover hidden subdirectories on websites, allowing for a more comprehensive analysis of a target domain.

## ⌨️ Commands
```python3
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
```python3
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
```python3
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
<br/>

[![SubFinder Version](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=github)](https://github.com/swiftglitxh/SubFinder/releases/tag/v0.3) &nbsp; [![SubFinder Version](https://img.shields.io/badge/version-0.3-blue?style=for-the-badge&logo=github)](https://github.com/swiftglitxh/SubFinder/releases/tag/v0.3)

