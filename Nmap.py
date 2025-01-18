import socket

def port_scan(host, baslangic_portu, bitis_portu):
    print(f"Port Scanning will start: {host}")
    
    for port in range(baslangic_portu, bitis_portu + 1):
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(1)
        
        netice = soket.connect_ex((host, port))
        
        if netice == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        
        soket.close()

# Kullanıcıdan girdi alma
destination_host = input("Destination IP or domain: ")
baslangic_portu = int(input("First port: "))
bitis_portu = int(input("Last port: "))

# Port tarama işlemi
port_scan(destination_host, baslangic_portu, bitis_portu)