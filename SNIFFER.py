from scapy.all import sniff

class Sniffer:
    def __init__(self):
        self.packets = []

    def start_sniffing(self):
        # Start sniffing the network
        self.packets = sniff()

    def stop_sniffing(self):
        # Stop sniffing the network
        sniff(stop_filter=lambda x: True)
