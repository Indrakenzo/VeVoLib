import json
import requests
import time
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from colorama import Fore, Style

# --- FUNGSI 1: IP TRACKER ---
# Di main.py dipanggil sebagai: run_ip_lookup
def run_ip_lookup():
    print(Fore.CYAN + "\n[+] Memulai IP Tracker...")
    ip = input(Fore.YELLOW + "Masukkan IP Target (Kosongkan untuk IP sendiri): ")
    
    # Jika input kosong, gunakan API tanpa parameter untuk cek IP sendiri
    url = f"http://ipwho.is/{ip}" if ip else "http://ipwho.is/"

    print(Fore.WHITE + "\n[*] Mengambil data dari server...")
    try:
        req_api = requests.get(url)
        ip_data = json.loads(req_api.text)
        
        if not ip_data.get("success", True):
            print(Fore.RED + f"[!] Gagal: {ip_data.get('message', 'IP Invalid')}")
            return

        print(Fore.GREEN + "=" * 40)
        print(f" IP Target       : {ip_data.get('ip')}")
        print(f" Tipe            : {ip_data.get('type')}")
        print(f" Negara          : {ip_data.get('country')} ({ip_data.get('country_code')})")
        print(f" Kota            : {ip_data.get('city')}")
        print(f" ISP             : {ip_data['connection'].get('isp')}")
        print(f" Organisasi      : {ip_data['connection'].get('org')}")
        print(f" Koordinat       : {ip_data.get('latitude')}, {ip_data.get('longitude')}")
        print(f" Google Maps     : https://www.google.com/maps?q={ip_data.get('latitude')},{ip_data.get('longitude')}")
        print(Fore.GREEN + "=" * 40)
        
    except Exception as e:
        print(Fore.RED + f"[!] Terjadi kesalahan koneksi: {e}")

# --- FUNGSI 2: PHONE TRACKER ---
# Di main.py dipanggil sebagai: run_phone_info
def run_phone_info():
    print(Fore.CYAN + "\n[+] Memulai Phone Number Tracker...")
    user_phone = input(Fore.YELLOW + "Masukkan No HP (Ex: +6281xxx): ")
    
    try:
        # Default region ID (Indonesia) jika user lupa pakai +62
        parsed_number = phonenumbers.parse(user_phone, "ID")
        
        if not phonenumbers.is_valid_number(parsed_number):
            print(Fore.RED + "[!] Nomor tidak valid!")
            return

        region_code = phonenumbers.region_code_for_number(parsed_number)
        provider = carrier.name_for_number(parsed_number, "en")
        location = geocoder.description_for_number(parsed_number, "id")
        time_zones = timezone.time_zones_for_number(parsed_number)
        
        print(Fore.GREEN + "=" * 40)
        print(f" Lokasi          : {location}")
        print(f" Region Code     : {region_code}")
        print(f" Timezone        : {', '.join(time_zones)}")
        print(f" Provider        : {provider}")
        print(f" Format Valid    : {phonenumbers.is_valid_number(parsed_number)}")
        print(Fore.GREEN + "=" * 40)

    except Exception as e:
        print(Fore.RED + f"[!] Error parsing nomor: {e}")

# --- FUNGSI 3: USERNAME TRACKER ---
# Di main.py dipanggil sebagai: run_username_check
def run_username_check():
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
    # Headers agar tidak dianggap bot oleh beberapa website
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    for site in social_media:
        url = site['url'].format(username)
        try:
            response = requests.get(url, headers=headers, timeout=5)
            # Beberapa website me-redirect ke login page (200 OK) meski user tidak ada
            # Jadi kita cek logic sederhana status code dulu
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
