import webbrowser
import time
from colorama import Fore, Style

def run_dorking():
    print(Fore.CYAN + "\n[+] Memulai Modul Google Dorking Automator...")
    target = input(Fore.YELLOW + "Masukkan Domain Target (contoh: makassarkota.go.id): ")
    
    if not target:
        print(Fore.RED + "[!] Target tidak boleh kosong!")
        return

    dorks = {
        "File Sensitif": f"site:{target} ext:pdf OR ext:xls OR ext:xlsx OR ext:doc",
        "Config Bocor": f"site:{target} ext:env OR ext:sql OR ext:bak OR ext:log",
        "Login Page": f"site:{target} inurl:admin OR inurl:login OR inurl:portal",
        "Directory Listing": f"site:{target} intitle:\"index of\""
    }

    print(Fore.GREEN + "\n[!] Membuka browser untuk pencarian...")
    for key, query in dorks.items():
        print(f"{Fore.BLUE}[>] Mencari: {key}...")
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        time.sleep(1) # Jeda agar browser tidak nge-lag
    
    print(Fore.GREEN + "\n[+] Selesai. Silakan cek tab browser Anda.")