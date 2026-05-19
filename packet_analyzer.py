from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.packet import Raw


def get_protocol(packet):
    """
    Packet protocol identify pannum.
    """

    if packet.haslayer(TCP):
        return "TCP"

    elif packet.haslayer(UDP):
        return "UDP"

    elif packet.haslayer(ICMP):
        return "ICMP"

    else:
        return "OTHER"


def get_payload(packet, payload_limit=80):
    """
    Packet payload preview edukkum.
    Payload readable illa na proper message return pannum.
    """

    if packet.haslayer(Raw):
        try:
            payload = packet[Raw].load
            payload_text = payload.decode(errors="ignore")

            if payload_text.strip() == "":
                return "Encrypted / No readable payload"

            return payload_text[:payload_limit]

        except Exception:
            return "Unable to decode payload"

    return "No payload"


def analyze_packet(packet, payload_limit=80):
    """
    Captured packet ah analyze panni dictionary format la return pannum.
    """

    packet_info = {
        "source_ip": "N/A",
        "destination_ip": "N/A",
        "protocol": "OTHER",
        "source_port": "N/A",
        "destination_port": "N/A",
        "length": len(packet),
        "payload": "No payload"
    }

    if packet.haslayer(IP):
        packet_info["source_ip"] = packet[IP].src
        packet_info["destination_ip"] = packet[IP].dst

    protocol = get_protocol(packet)
    packet_info["protocol"] = protocol

    if packet.haslayer(TCP):
        packet_info["source_port"] = packet[TCP].sport
        packet_info["destination_port"] = packet[TCP].dport

    elif packet.haslayer(UDP):
        packet_info["source_port"] = packet[UDP].sport
        packet_info["destination_port"] = packet[UDP].dport

    packet_info["payload"] = get_payload(packet, payload_limit)

    return packet_info