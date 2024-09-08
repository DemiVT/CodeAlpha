from scapy.all import sniff

def packet_callback(packet):
    print(f"Packet: {packet.summary()}")

def start_sniffing(interface):
    print(f"Sniffing on interface {interface}...")
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python sniffer.py <interface>")
        sys.exit(1)
    interface = sys.argv[1]
    start_sniffing(interface)
