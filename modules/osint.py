import json
import requests
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from colorama import Fore

# --- FUNGSI 1: IP TRACKER (Fixed Nested Dictionary Error) ---
def run_ip_lookup():
    print(Fore.CYAN + "\n[+] Memulai IP Tracker...")
    ip = input(Fore.YELLOW + "Masukkan IP Target (Kosongkan untuk IP sendiri): ")
    
    url = f"http://ipwho.is/{ip}" if ip else "http://ipwho.is/"

    print(Fore.WHITE + "\n[*] Mengambil data dari server...")
    try:
        req_api = requests.get(url)
        ip_data = json.loads(req_api.text)
        
        if not ip_data.get("success", True):
            print(Fore.RED + f"[!] Gagal: {ip_data.get('message', 'IP Invalid')}")
            return

        # Menggunakan .get() dengan aman untuk nested dictionary
        connection = ip_data.get('connection', {})
        
        print(Fore.GREEN + "=" * 40)
        print(f" IP Target        : {ip_data.get('ip')}")
        print(f" Tipe             : {ip_data.get('type')}")
        print(f" Negara           : {ip_data.get('country')} ({ip_data.get('country_code')})")
        print(f" Kota             : {ip_data.get('city')}")
        print(f" ISP              : {connection.get('isp', 'N/A')}")
        print(f" Organisasi       : {connection.get('org', 'N/A')}")
        print(f" Koordinat        : {ip_data.get('latitude')}, {ip_data.get('longitude')}")
        print(Fore.GREEN + "=" * 40)
        
    except Exception as e:
        print(Fore.RED + f"[!] Terjadi kesalahan: {e}")

# --- FUNGSI 2: PHONE TRACKER (Sama seperti sebelumnya) ---
def run_phone_info():
    print(Fore.CYAN + "\n[+] Memulai Phone Number Tracker...")
    user_phone = input(Fore.YELLOW + "Masukkan No HP (Ex: +6281xxx): ")
    try:
        parsed_number = phonenumbers.parse(user_phone, "ID")
        if not phonenumbers.is_valid_number(parsed_number):
            print(Fore.RED + "[!] Nomor tidak valid!")
            return

        region_code = phonenumbers.region_code_for_number(parsed_number)
        provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        
        print(Fore.GREEN + "=" * 40)
        print(f" Lokasi           : {location}")
        print(f" Region           : {region_code}")
        print(f" Provider         : {provider}")
        print(Fore.GREEN + "=" * 40)
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")

# --- FUNGSI 3: USERNAME TRACKER (Improved Headers) ---
def run_username_check():
    print(Fore.CYAN + "\n[+] Memulai Username Tracker...")
    username = input(Fore.YELLOW + "Masukkan Username Target : ")
    
    social_media = [
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://twitter.com/{}", "name": "Twitter"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        {"url": "https://github.com/{}", "name": "GitHub"},
        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"}
    ]
    
    print(Fore.WHITE + "\n[*] Memindai jejak digital (Mungkin ada False Positive)...")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    found_count = 0
    for site in social_media:
        url = site['url'].format(username)
        try:
            r = requests.get(url, headers=headers, timeout=5)
            # Logika deteksi sederhana
            if r.status_code == 200:
                print(Fore.GREEN + f"[FOUND] {site['name']} : {url}")
                found_count += 1
            else:
                print(Fore.RED + f"[404] {site['name']}")
        except:
            print(Fore.YELLOW + f"[ERR] {site['name']} : Timeout")
            
    if found_count > 0:
        print(Fore.CYAN + f"\n[+] Ditemukan {found_count} akun potensial.")
    else:
        print(Fore.RED + "\n[!] Tidak ditemukan.")

# --- FUNGSI 4: SUBDOMAIN SCANNER (CRT.SH) - NEW ADDITION ---
# WAJIB DITAMBAHKAN di Main Menu choice 3 -> sub-menu 4
def run_subdomain_check():
    print(Fore.CYAN + "\n[+] Memulai Subdomain Enumeration (crt.sh)...")
    domain = input(Fore.YELLOW + "Masukkan Domain (cth: makassarkota.go.id): ").replace("https://", "").replace("http://", "")
    
    print(Fore.WHITE + "[*] Mengambil data sertifikat SSL publik...")
    
    url = f"https://crt.sh/?q={domain}&output=json"
    
    try:
        req = requests.get(url, timeout=10)
        if req.status_code != 200:
            print(Fore.RED + "[!] Gagal terhubung ke database crt.sh")
            return
            
        data = json.loads(req.text)
        subdomains = set() # Gunakan set untuk hapus duplikat
        
        for entry in data:
            name_value = entry['name_value']
            # Pisahkan jika ada multiple domains dalam satu sertifikat
            for sub in name_value.split('\n'):
                if "*" not in sub: # Hapus wildcard
                    subdomains.add(sub)
        
        print(Fore.GREEN + f"\n[SUCCESS] Ditemukan {len(subdomains)} Subdomain unik:\n")
        
        for sub in sorted(subdomains):
            print(Fore.GREEN + f" -> {sub}")
            
    except Exception as e:
        print(Fore.RED + f"[!] Error parsing JSON: {e}")
