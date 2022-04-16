import requests,time,argparse

# Arguments/ --flags
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('-w',dest="website", help='an integer for the accumulator')
parser.add_argument('-s',dest="silent",action="store_true", help='an integer for the accumulator')
parser.add_argument('-l',dest="list", help='an integer for the accumulator')

args = parser.parse_args()

print('''
 ____  _  _  ____  ____  __  __ _  ____  ____  ____ 
/ ___)/ )( \\(  _ \\(  __)(  )(  ( \\(    \\(  __)(  _ \

\\___ \\) \\/ ( ) _ ( ) _)  )( /    / ) D ( ) _)  )   /
(____/\\____/(____/(__)  (__)\\_)__)(____/(____)(__\\_) \033[1;33m{Version: 0.1}\033[0;37m
=====================================================
    *** SubFinder is still under development ***
''')
if args.website == None:
    print("\033[0;31m[WARNING] Can not proceed without a website being given [WARNING]\033[1;37m")
    exit()
# the domain to scan for subdomains
domain = args.website
if "https://www." in domain:
    domain = domain[12:]
elif "http://www." in domain:
    domain = domain[11:]
found = 0
undiscovered = 0
# read all subdomains
wordlist = args.list
file = open(wordlist,mode="r",encoding="ISO-8859-1")
# read all content
content = file.read()

# split by new lines
subdomains = content.splitlines()

# a list of discovered subdomains
discovered_subdomains = []
print('\033[1;36m[=] Discovering Subdomains\n')
start = time.time()
for subdomain in subdomains:
    # construct the url
    url = f"https://{subdomain}.{domain}"
    try:
        # if this raises an ERROR, that means the subdomain does not exist
        requests.get(url)

    except requests.ConnectionError:
        # if the subdomain does not exist, just pass, print nothing
        print("\033[1;33m[x] Undiscovered Subdomain:\033[0;37m", url)
        undiscovered += 1
    except requests.exceptions.ConnectionError as e:
        print(f'''
\033[0;31m X
 │
 ╰> \033[0;37m{e}
            ''')
        pass
    else:
        print(f"\033[1;32m[+] Discovered   Subdomain: \033[0;37m{url}" )
        found += 1
        # append the discovered subdomain to our list
        discovered_subdomains.append(url)
finished = time.time()
done = int(finished - start)
print("\n\033[1;37m[!] Scan Complete\033[0;37m")
print(f"\033[1;37m[+] Scan Took: \033[0;37m{done} seconds to finish")
print(f"\033[1;37m[=] Discovered:\033[0;37m {found}")
print(f"\033[1;37m[=] Undiscovered:\033[0;37m {undiscovered}")
print("\n *** Please Note Some Results May Not Be 100% ***")