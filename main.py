import os
import sys
import platform
import time

# Import modul buatan kita sendiri
try:
    from modules import recon, scanning, osint
except ImportError:
    # Fallback jika folder modules belum ada/salah struktur
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

    def main_menu(self):
        """Menu Utama Program."""
        while True:
            self.banner()
            # Tampilan Menu
            print(Fore.WHITE + "[1] " + Fore.CYAN + "Reconnaissance (Google Dorking)")
            print(Fore.WHITE + "[2] " + Fore.CYAN + "Scanning (Port Check)")
            print(Fore.WHITE + "[3] " + Fore.MAGENTA + "OSINT Toolkit (IP/Phone/User)") # <-- Menu Baru
            print(Fore.WHITE + "[4] " + Fore.CYAN + "About VeVoLib")
            print(Fore.WHITE + "[0] " + Fore.RED + "Keluar / Exit")
            
            try:
                choice = input(Fore.YELLOW + "\n[VeVoLib] > ")
                
                # --- LOGIKA PENGARAH (ROUTING) ---
                
                if choice == '1':
                    # PANGGIL MODUL RECON
                    recon.run_dorking()
                    input(Fore.WHITE + "\n[ENTER] Kembali ke menu...")
                
                elif choice == '2':
                    # PANGGIL MODUL SCANNING
                    scanning.run_port_scan()
                    input(Fore.WHITE + "\n[ENTER] Kembali ke menu...")
                
                elif choice == '3':
                    # PANGGIL SUB-MENU OSINT (Ini yang kita perbaiki)
                    # Kita arahkan ke fungsi submenu_osint yang ada di bawah
                    self.submenu_osint()
                
                elif choice == '4':
                    # TAMPILKAN INFO
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
                # Tangkap error jika modul belum siap
                print(Fore.RED + f"\n[!] Terjadi Error: {e}")
                input("Tekan Enter...")

if __name__ == "__main__":
    app = VeVoLib()

    app.main_menu()
