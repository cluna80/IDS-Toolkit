from NMAP import NMAP
from SNIFFER import Sniffer

class IDS_toolkit:
    def __init__(self):
        self.nmap = NMAP()
        self.sniffer = Sniffer()

    def start_intrusion_detection(self, ip):
        # Start the intrusion detection process
        self.nmap.scan(ip)
        self.sniffer.start_sniffing()

    def stop_intrusion_detection(self):
        # Stop the intrusion detection process
        self.sniffer.stop_sniffing()
