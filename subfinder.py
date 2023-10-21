import requests
import time
import argparse
import concurrent.futures
import threading
import subprocess

subprocess.call(['clear'])
red = '\033[1;31m'
blue = '\033[1;32m'
yellow = '\033[1;33m'
reset = '\033[0;27m'
version = "0.3"
print(f'''
 ____  _  _  ____  ____  __  __ _  ____  ____  ____ 
/ ___)/ )( \(  _ \(  __)(  )(  ( \(    \(  __)(  _ \

\\___ \) \\/ ( ) _ ( ) _)  )( /    / ) D ( ) _)  )   /
(____/\\____/(____/(__)  (__)\\_)__)(____/(____)(__\\_) \033[1;33mVersion: {version}\033[0;37m
=====================================================
    {blue}*** SubFinder is still under development ***{reset}
''')

# Constants
HTTP_PREFIXES = ["https://www.", "http://www."]

def discover_subdomain(url, verbose=False):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTP error if response status code indicates an error
        print(f"{blue}[+] Discovered Subdomain: {reset}{url} ")
        return url

    except requests.exceptions.RequestException:
        if verbose:
            print(f"{red}[x] Undiscovered Subdomain:{reset} {url}")
        return None

def scan_subdomains(subdomains, domain, verbose, num_threads):
    found = 0
    undiscovered = 0

    def scanning_message():
        print()
        while not done_scanning[0]:
            print("Scanning...", end="\r")
            time.sleep(1)

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        future_to_url = {executor.submit(discover_subdomain, f"{prefix}{subdomain}.{domain}", verbose): subdomain for subdomain in subdomains for prefix in HTTP_PREFIXES}
        
        done_scanning = [False]
        scanning_thread = threading.Thread(target=scanning_message)
        scanning_thread.start()

        for future in concurrent.futures.as_completed(future_to_url):
            subdomain = future_to_url[future]
            result = future.result()
            if result:
                found += 1
            else:
                undiscovered += 1

        done_scanning[0] = True
        scanning_thread.join()

    return found, undiscovered

def discover_subdomains(domain, wordlist_path, verbose=False, num_threads=10):
    found = 0
    undiscovered = 0

    # Read wordlist
    with open(wordlist_path, mode="r", encoding="ISO-8859-1") as file:
        subdomains = file.read().splitlines()

    domain = domain.replace("https://", "").replace("http://", "")  # Remove http:// or https:// prefixes

    print(f"\n{yellow}[=] Discovering Subdomains for {domain}{reset}\n")

    start_time = time.time()
    
    found, undiscovered = scan_subdomains(subdomains, domain, verbose, num_threads)

    end_time = time.time()
    elapsed_time = int(end_time - start_time)

    print("\n[!] Scan Complete")
    print(f"[+] Scan Took: {elapsed_time} seconds to finish")
    print(f"[=] Discovered: {found}")
    if verbose:
        print(f"[=] Undiscovered: {undiscovered}")
    print("*** Please Note Some Results May Not Be 100% ***")

    return found, undiscovered

def main():
    parser = argparse.ArgumentParser(description='Discover subdomains for a website using a wordlist.')
    parser.add_argument('-w', '--website', dest="website", help='Choose a website to target', required=True)
    parser.add_argument('-l', '--wordlist', dest="wordlist", help='Choose a wordlist to use', required=True)
    parser.add_argument('-v', '--verbose', dest="verbose", action="store_true", help='Show both discovered and undiscovered subdomains')
    parser.add_argument('-t', '--threads', dest="threads", type=int, default=10, help='Number of threads to use for scanning (default: 10)')

    args = parser.parse_args()

    if not args.website or not args.wordlist:
        print("\033[0;31m[WARNING] Both website and wordlist are required [WARNING]\033[1;37m")
        parser.print_help()
        return

    discover_subdomains(args.website, args.wordlist, args.verbose, args.threads)

if __name__ == '__main__':
    main()
