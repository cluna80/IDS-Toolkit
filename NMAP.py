import os

class NMAP:
    def __init__(self):
        pass

    def scan(self, ip):
        # Perform a simple NMAP scan on a given IP
        command = f"nmap {ip}"
        os.system(command)

    def scan_range(self, ip_range):
        # Perform a simple NMAP scan on a given range of IPs
        command = f"nmap {ip_range}"
        os.system(command)
