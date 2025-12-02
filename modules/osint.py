import json
import requests
import time
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from colorama import Fore, Style

# --- FUNGSI 1: IP TRACKER ---
def ip_tracker():
    print(Fore.CYAN + "\n[+] Memulai IP Tracker...")
    ip = input(Fore.YELLOW + "Masukkan IP Target : ")
    
    print(Fore.WHITE + "\n[*] Mengambil data dari server...")
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = json.loads(req_api.text)
        
        if not ip_data.get("success", True):
            print(Fore.RED + f"[!] Gagal: {ip_data.get('message', 'IP Invalid')}")
            return

        print(Fore.GREEN + "=" * 40)
        print(f" IP Target      : {ip_data.get('ip')}")
        print(f" Tipe           : {ip_data.get('type')}")
        print(f" Negara         : {ip_data.get('country')} ({ip_data.get('country_code')})")
        print(f" Kota           : {ip_data.get('city')}")
        print(f" ISP            : {ip_data['connection'].get('isp')}")
        print(f" Organisasi     : {ip_data['connection'].get('org')}")
        print(f" Koordinat      : {ip_data.get('latitude')}, {ip_data.get('longitude')}")
        print(f" Google Maps    : https://www.google.com/maps/@{ip_data.get('latitude')},{ip_data.get('longitude')},15z")
        print(Fore.GREEN + "=" * 40)
        
    except Exception as e:
        print(Fore.RED + f"[!] Terjadi kesalahan koneksi: {e}")

# --- FUNGSI 2: PHONE TRACKER ---
def phone_tracker():
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
        time_zones = timezone.time_zones_for_number(parsed_number)
        
        print(Fore.GREEN + "=" * 40)
        print(f" Lokasi         : {location}")
        print(f" Region Code    : {region_code}")
        print(f" Timezone       : {', '.join(time_zones)}")
        print(f" Provider       : {provider}")
        print(f" Format Valid   : {phonenumbers.is_valid_number(parsed_number)}")
        print(Fore.GREEN + "=" * 40)

    except Exception as e:
        print(Fore.RED + f"[!] Error parsing nomor: {e}")

# --- FUNGSI 3: USERNAME TRACKER ---
def username_tracker():
    print(Fore.CYAN + "\n[+] Memulai Username Tracker...")
    username = input(Fore.YELLOW + "Masukkan Username Target : ")
    
    # Daftar website populer untuk dicek
    social_media = [
        {"url": "https://www.facebook.com/{}", "name": "Facebook"},
        {"url": "https://www.twitter.com/{}", "name": "Twitter"},
        {"url": "https://www.instagram.com/{}", "name": "Instagram"},
        {"url": "https://www.github.com/{}", "name": "GitHub"},
        {"url": "https://www.tiktok.com/@{}", "name": "TikTok"},
        {"url": "https://www.linkedin.com/in/{}", "name": "LinkedIn"},
        {"url": "https://www.pinterest.com/{}", "name": "Pinterest"}
    ]
    
    print(Fore.WHITE + "\n[*] Memindai jejak digital...")
    
    found_count = 0
    for site in social_media:
        url = site['url'].format(username)
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[FOUND] {site['name']} : {url}")
                found_count += 1
            else:
                print(Fore.RED + f"[404] {site['name']} : Tidak Ditemukan")
        except:
            print(Fore.YELLOW + f"[ERR] {site['name']} : Koneksi Gagal")
            
    if found_count == 0:
        print(Fore.RED + "\n[!] Tidak ditemukan jejak pada daftar target.")
    else:
        print(Fore.CYAN + f"\n[+] Ditemukan {found_count} akun potensial.")

# --- FUNGSI 4: SHOW MY IP ---
def show_my_ip():
    try:
        response = requests.get('https://api.ipify.org/')
        print(Fore.GREEN + f"\n[+] IP Publik Anda : {response.text}")
    except:
        print(Fore.RED + "[!] Gagal mengambil IP.")
