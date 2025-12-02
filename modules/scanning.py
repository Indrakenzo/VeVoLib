import socket
import time
from colorama import Fore

def run_port_scan():
    print(Fore.CYAN + "\n[+] Memulai Modul Port Scanner Sederhana...")
    target = input(Fore.YELLOW + "Masukkan IP/Domain Target: ")
    
    # Port umum yang sering dicek
    ports = [21, 22, 80, 443, 3306, 8080]
    
    print(Fore.WHITE + f"\n[*] Memindai {target}...")
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(Fore.GREEN + f"[OPEN] Port {port} Terbuka")
        else:
            print(Fore.RED + f"[CLOSED] Port {port} Tertutup")
        sock.close()
    
    print(Fore.CYAN + "\n[+] Scanning selesai.")