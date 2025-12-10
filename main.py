import os
import sys
import platform
import time

# --- IMPORT MODULES ---
# Struktur folder wajib:
# folder_proyek/
# ├── main.py
# ├── requirements.txt
# └── modules/
#     ├── __init__.py
#     ├── recon.py
#     ├── scanning.py
#     └── osint.py

try:
    from modules import recon, scanning, osint
except ImportError as e:
    print(f"Warning: Modul tidak ditemukan ({e}). Pastikan folder 'modules' ada.")
    pass 

# Pengecekan Library Eksternal
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    print("Error: Library 'colorama' belum terinstall.")
    print("Silakan jalankan: pip install -r requirements.txt")
    sys.exit()

class VeVoLib:
    def __init__(self):
        # Deteksi Sistem Operasi
        self.os_type = platform.system()
    
    def clear_screen(self):
        """Membersihkan layar terminal."""
        if self.os_type == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def banner(self):
        """Menampilkan Identitas VeVoLib."""
        self.clear_screen()
        
        # ASCII Art
        print(Fore.CYAN + Style.BRIGHT + """
   _    __       _    __       __    _ __    
  | |  / /___   | |  / /___   / /   (_) /_   
  | | / / _ \\   | | / / __ \\ / /   / / __ \\  
  | |/ /  __/   | |/ / /_/ // /___/ / /_/ /  
  |___/\\___/    |___/\\____//_____/_/_.___/   
        """)
        
        print(Fore.YELLOW + Style.BRIGHT + "      VERITAS VOS LIBERABIT")
        print(Fore.WHITE + " 'Kebenaran itu menyakitkan di awal tapi melegakan di akhir'")
        print(Fore.RED + "\n  [ Tools by Indra ]" + Fore.BLUE + " [ Didukung oleh Gemini AI ]")
        print(Fore.GREEN + "=" * 60 + "\n")

    # --- FUNGSI SUBMENU OSINT (UPDATED) ---
    def submenu_osint(self):
        """Menampilkan Sub-Menu Khusus OSINT."""
        while True:
            self.clear_screen()
            print(Fore.MAGENTA + Style.BRIGHT + "=== OSINT TOOLKIT MENU ===")
            print(Fore.WHITE + "[1] " + Fore.MAGENTA + "IP Address Lookup")
            print(Fore.WHITE + "[2] " + Fore.MAGENTA + "Username Checker (Sherlock Style)")
            print(Fore.WHITE + "[3] " + Fore.MAGENTA + "Phone Number Info")
            # [BARU] Menambahkan opsi Subdomain Scanner
            print(Fore.WHITE + "[4] " + Fore.MAGENTA + "Subdomain Scanner (crt.sh)") 
            print(Fore.WHITE + "[0] " + Fore.YELLOW + "Kembali ke Menu Utama")
            
            try:
                choice = input(Fore.MAGENTA + "\n[OSINT] > ")
                
                if choice == '1':
                    if 'osint' in sys.modules:
                        osint.run_ip_lookup()
                    else:
                        print("Modul OSINT belum dimuat.")
                    input(Fore.WHITE + "\n[ENTER] Lanjut...")
                    
                elif choice == '2':
                    if 'osint' in sys.modules:
                        osint.run_username_check()
                    else:
                        print("Modul OSINT belum dimuat.")
                    input(Fore.WHITE + "\n[ENTER] Lanjut...")

                elif choice == '3':
                    if 'osint' in sys.modules:
                        osint.run_phone_info()
                    else:
                        print("Modul OSINT belum dimuat.")
                    input(Fore.WHITE + "\n[ENTER] Lanjut...")

                # [BARU] Logika untuk Subdomain Scanner
                elif choice == '4':
                    if 'osint' in sys.modules:
                        # Pastikan fungsi ini ada di osint.py Anda
                        osint.run_subdomain_check() 
                    else:
                        print("Modul OSINT belum dimuat.")
                    input(Fore.WHITE + "\n[ENTER] Lanjut...")

                elif choice == '0':
                    break 
                else:
                    print(Fore.RED + "Pilihan tidak valid.")
                    time.sleep(1)
            except AttributeError:
                print(Fore.RED + "[!] Fungsi belum tersedia di modul osint.py.")
                print("Pastikan Anda sudah update kode osint.py dengan fitur Subdomain.")
                input("Tekan Enter...")
            except Exception as e:
                print(Fore.RED + f"Error di modul OSINT: {e}")
                input("Tekan Enter...")

    def main_menu(self):
        """Menu Utama Program."""
        while True:
            self.banner()
            # Tampilan Menu
            print(Fore.WHITE + "[1] " + Fore.CYAN + "Reconnaissance (Google Dorking)")
            print(Fore.WHITE + "[2] " + Fore.CYAN + "Scanning (Port Check)")
            print(Fore.WHITE + "[3] " + Fore.MAGENTA + "OSINT Toolkit (IP/Phone/User/Subdomain)") 
            print(Fore.WHITE + "[4] " + Fore.CYAN + "About VeVoLib")
            print(Fore.WHITE + "[0] " + Fore.RED + "Keluar / Exit")
            
            try:
                choice = input(Fore.YELLOW + "\n[VeVoLib] > ")
                
                # --- LOGIKA PENGARAH (ROUTING) ---
                
                if choice == '1':
                    recon.run_dorking()
                    input(Fore.WHITE + "\n[ENTER] Kembali ke menu...")
                
                elif choice == '2':
                    scanning.run_port_scan()
                    input(Fore.WHITE + "\n[ENTER] Kembali ke menu...")
                
                elif choice == '3':
                    self.submenu_osint()
                
                elif choice == '4':
                    print(Fore.GREEN + "\nVeVoLib adalah alat bantu untuk Legal Penetration Testing.")
                    print("Dibuat untuk membantu mencari kebenaran dalam keamanan sistem.")
                    input(Fore.WHITE + "\n[ENTER] Kembali ke menu...")

                elif choice == '0':
                    print(Fore.RED + "\n[!] Menutup VeVoLib. Stay Safe, Indra!")
                    sys.exit()
                
                else:
                    print(Fore.RED + "\n[!] Pilihan tidak valid!")
                    time.sleep(1)
            
            except KeyboardInterrupt:
                print(Fore.RED + "\n\n[!] Operasi dibatalkan oleh pengguna.")
                sys.exit()
            except Exception as e:
                print(Fore.RED + f"\n[!] Terjadi Error: {e}")
                input("Tekan Enter...")

if __name__ == "__main__":
    app = VeVoLib()
    app.main_menu()
