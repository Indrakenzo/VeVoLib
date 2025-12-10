import socket
import threading
from queue import Queue
from colorama import Fore

# Kunci agar output thread tidak berantakan
print_lock = threading.Lock()

def port_scan(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Timeout dipercepat
        result = s.connect_ex((target, port))
        
        if result == 0:
            # Mencoba mengambil Banner (Service Version)
            try:
                s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner = s.recv(1024).decode().strip().split('\n')[0]
            except:
                banner = "Unknown Service"

            with print_lock:
                print(Fore.GREEN + f"[OPEN] Port {port:<5} : {banner}")
        s.close()
    except:
        pass

def threader(target, q):
    while True:
        worker = q.get()
        port_scan(target, worker)
        q.task_done()

def run_port_scan():
    print(Fore.CYAN + "\n[+] Memulai Advanced Port Scanner (Multi-threaded)...")
    target_input = input(Fore.YELLOW + "Masukkan Domain/IP Target: ")
    
    # Resolusi Domain ke IP
    try:
        target_ip = socket.gethostbyname(target_input)
        print(Fore.WHITE + f"[*] Target IP: {target_ip}")
    except socket.gaierror:
        print(Fore.RED + "[!] Hostname tidak dapat diselesaikan.")
        return

    print(Fore.WHITE + "[?] Pilih Mode Scan:")
    print("    [1] Fast Scan (Top Ports only)")
    print("    [2] Full Range (1 - 1024)")
    mode = input(Fore.YELLOW + "Pilihan > ")

    q = Queue()

    # Menentukan range port
    if mode == '2':
        ports_to_scan = range(1, 1025)
    else:
        # Common ports list
        ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 993, 995, 3306, 3389, 8080, 8443]

    print(Fore.CYAN + f"\n[*] Memindai {len(ports_to_scan)} ports dengan 50 threads...")
    print(Fore.WHITE + "-" * 40)

    # Membuat 50 Threads (Workers)
    for x in range(50):
        t = threading.Thread(target=threader, args=(target_ip, q))
        t.daemon = True
        t.start()

    # Mengisi antrian pekerjaan
    for worker in ports_to_scan:
        q.put(worker)

    q.join()
    print(Fore.CYAN + "\n[+] Scanning selesai.")
