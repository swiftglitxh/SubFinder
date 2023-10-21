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

## Language:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
