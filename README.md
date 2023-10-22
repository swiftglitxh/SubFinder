🚀 **SubFinder v0.3: Discover Hidden Subdirectories**

SubFinder is a powerful and versatile subdirectory discovery tool designed for web security and penetration testing. With a focus on efficiency and customization, this Python-based tool empowers ethical hackers, security professionals, and researchers to reveal concealed subdirectories on websites, enabling a comprehensive analysis of target domains.

📋 **Key Features**

- **User-Friendly Commands**: SubFinder offers a straightforward command-line interface with customizable flags, allowing you to tailor your scans.

- **Website Targeting**: Choose the website you want to target and define the wordlist to use for scanning.

- **Version Check**: Easily check the version of SubFinder you're using to stay up-to-date with the latest improvements.

- **Multi-threading Support**: Enhance scanning speed with multi-threading, making SubFinder up to x5 faster than previous versions.

🚀 **SubFinder Commands**
```python3
Usage:
  subfinder [flags]

Flags:
  -h, --help               Help for arguments
  -w, --website string     Choose a website to target
  -l, --wordlist           Choose a wordlist to use    
  -v, --version            Show what version of SubFinder you have
  -t, --threads            Number of threads to use for scanning (default: 10)
```
📌 **How to Run SubFinder?**

```bash
python3 subfinder.py -w https://www.google.com -l /usr/share/wordlists/rockyou.txt -v --threads 30
```

🛠️ **Updates**

- **Version 0.1**
  - SubFinder now allows users to choose their own file for performing attacks.

- **Version 0.2**
  - Bug fixes and improvements.

- **Version 0.3**
  - Added multi-threading support.
  - Introduced a version argument to check the tool's version.
  - SubFinder is now x5 faster than previous versions.

🚀 **Example Code**

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

🧩 **Language**: Python

📢 **Important Note**: SubFinder is continually under development, and contributions are welcome.

---
[![SubFinder Version](https://img.shields.io/badge/Language-Python-yellow?style=for-the-badge&logo=github)](https://github.com/swiftglitxh/SubFinder/releases/tag/v0.3) &nbsp; [![SubFinder Version](https://img.shields.io/badge/version-0.3-blue?style=for-the-badge&logo=github)](https://github.com/swiftglitxh/SubFinder/releases/tag/v0.3)

