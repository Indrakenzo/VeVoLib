import webbrowser
import time
from colorama import Fore, Style

# Di main.py dipanggil sebagai: run_dorking
def run_dorking():
    print(Fore.CYAN + "\n[+] Memulai Modul Google Dorking (Passive Recon)...")
    print(Fore.WHITE + "Modul ini akan membuka browser default Anda secara otomatis.")
    
    target = input(Fore.YELLOW + "Masukkan Domain Target (contoh: makassarkota.go.id): ")
    
    if not target:
        print(Fore.RED + "[!] Target tidak boleh kosong.")
        return

    # Dictionary berisi teknik Dorking umum
    dorks = {
        "1": {"desc": "Public Exposed Documents (PDF, DOC, XLS)", 
              "query": "site:{} ext:pdf | ext:docx | ext:xlsx | ext:pptx | ext:txt"},
        
        "2": {"desc": "Directory Listing Vulnerabilities", 
              "query": "site:{} intitle:index.of"},
        
        "3": {"desc": "Configuration / Log Files", 
              "query": "site:{} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ini | ext:log"},
        
        "4": {"desc": "Database Files", 
              "query": "site:{} ext:sql | ext:dbf | ext:mdb"},
        
        "5": {"desc": "Login Pages / Admin Portals", 
              "query": "site:{} inurl:login | inurl:admin | intitle:login | intitle:admin"},
        
        "6": {"desc": "PHP Errors / Warnings", 
              "query": "site:{} \"PHP Parse error\" | \"PHP Warning\" | \"Fatal error\""},
              
        "7": {"desc": "Wordpress Entries", 
              "query": "site:{} inurl:wp-content | inurl:wp-includes"}
    }

    while True:
        print(Fore.MAGENTA + "\n--- PILIH TIPE DORK ---")
        for key, value in dorks.items():
            print(f"[{key}] {value['desc']}")
        print("[0] Kembali ke Menu Utama")
        
        pilihan = input(Fore.YELLOW + "Pilih Dork > ")

        if pilihan == '0':
            break
        
        if pilihan in dorks:
            query = dorks[pilihan]['query'].format(target)
            # Encode URL agar spasi dan karakter khusus terbaca browser
            final_url = f"https://www.google.com/search?q={query}"
            
            print(Fore.GREEN + f"[*] Membuka browser untuk query: {query}")
            webbrowser.open(final_url)
            time.sleep(1) # Jeda sedikit agar tidak spam browser
        else:
            print(Fore.RED + "[!] Pilihan tidak valid.")

    print(Fore.CYAN + "[+] Sesi Dorking selesai.")
