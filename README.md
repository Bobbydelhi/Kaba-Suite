# KABA Pentest Suite v1.0
**Developed by BobbyDelhi**

A high-performance, native Python automation suite for professional Red Team engagements. This tool specializes in stealth reconnaissance, security header auditing, and advanced XML-RPC exploitation while maintaining a zero-footprint policy on the local system.



##  Key Features
- **Ghost Mode**: Native integration with Tor for automated IP rotation every 25 seconds.
- **WAF Evasion**: Dynamic User-Agent switching and randomized Jitter delays to break behavioral analysis.
- **Multithreaded Performance**: Asynchronous execution for port scanning and large-scale brute forcing.
- **Native Logic**: Built with standard Python libraries (requests/socket/ftplib) to avoid binary detection.
- **Anti-Forensics**: Automated bash history wiping and script self-destruction upon completion.

---

## Installation & Setup

## 1. Clone the Repository
First, clone the project from GitHub to your local machine:
```bash
git clone [https://github.com/BobbyDelhi/Kaba-Suite.git](https://github.com/BobbyDelhi/Kaba-Suite.git)
cd KABA-Suite
```

## 2. Install dependencies

```bash
sudo apt update && sudo apt install tor python3-pip -y
pip3 install -r requirements.txt --break-system-packages
```

## 3. Grant Permissions

```bash
chmod +x kaba.py

```


### RECOMMENDATIONS & INFO

1. Start Tor Service: sudo service tor start

2. Run with Identity Masquerading: Launch the script with a leading space to prevent it from being recorded in your .bash_history: python3 kaba.py

3. Input Data: Follow the on-screen menu to set your target URL, IP, and Wordlists.
```bash
Default Target: https://example.com

Default User List: /usr/share/seclists/Usernames/Names/names.txt

Default Pass List: /usr/share/seclists/Passwords/Leaked-Databases/rockyou-75.txt
```


### LEGAL DISCLAIMER

Legal Disclaimer
This tool is strictly for educational purposes and authorized security auditing. Unauthorized access to computer systems is illegal. **_BobbyDelhi_** is not responsible for any damage caused by the misuse of this tool. Use it only on systems you own or have explicit permission to test.



##  Author
```text
  ____        _     _           ____       _ _     _ 
 | __ )  ___ | |__ | |__  _   _|  _ \  ___| | |__ (_)
 |  _ \ / _ \| '_ \| '_ \| | | | | | |/ _ \ | '_ \| |
 | |_) | (_) | |_) | |_) | |_| | |_| |  __/ | | | | |
 |____/ \___/|_.__/|_.__/ \__, |____/ \___|_|_| |_|_|
                          |___/
