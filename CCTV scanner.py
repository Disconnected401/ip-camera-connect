import os
import socket 
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore

G = Fore.LIGHTGREEN_EX
R = Fore.LIGHTRED_EX
W = Fore.RESET

offline_count = 0

def check_rtsp_port(ip):
    global offline_count  # Declare offline_count as global
    try:
        # Tworzenie gniazda
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)

        # Sprawdzanie połączenia z portem 554 RTSP
        result = s.connect_ex((ip, 554))
        if result == 0:
            print(f"IP-CAMMERA {ip}:554 | {G}ONLINE{W}")
        else:
            offline_count += 1  # Increment offline count
            os.system(f"Title OFFLINE: {offline_count}")

        # Zamykanie gniazda
        s.close()
    except socket.error as e:
        print(f"Wystąpił błąd podczas sprawdzania urządzenia o IP {ip}: {str(e)}")

def search_devices():
    # Prompt user for base IP
    base_ip = input("Base IP > ")
    os.system("cls")

    # Generate IP addresses to check
    ip_addresses = [f"{base_ip}.{i}" for i in range(1, 256)]

    for ip in ip_addresses:
        check_rtsp_port(ip)

# Wywołanie funkcji search_devices
with ThreadPoolExecutor(max_workers=255) as executor:
    search_devices()
