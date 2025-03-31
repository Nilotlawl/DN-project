import dpkt

def check_pcap(filename):
    try:
        with open(filename, 'rb') as f:
            pcap = dpkt.pcap.Reader(f)
            for i, (ts, buf) in enumerate(pcap):
                print(f"Packet {i+1}: {len(buf)} bytes")
                if i == 5:
                    break
        print("PCAP file read successfully!")
    except Exception as e:
        print(f"Error reading PCAP file: {e}")

check_pcap('wire.pcap')
