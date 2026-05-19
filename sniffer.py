from scapy.all import sniff
from packet_analyzer import analyze_packet
from logger import setup_logger
import json
import os


captured_packets = []
logger = setup_logger()


def print_packet(packet_info):
    """
    Packet details terminal la clean ah display pannum.
    """

    print("\n" + "=" * 55)
    print("[+] Packet Captured")
    print("=" * 55)
    print(f"Source IP        : {packet_info['source_ip']}")
    print(f"Destination IP   : {packet_info['destination_ip']}")
    print(f"Protocol         : {packet_info['protocol']}")
    print(f"Source Port      : {packet_info['source_port']}")
    print(f"Destination Port : {packet_info['destination_port']}")
    print(f"Length           : {packet_info['length']} bytes")
    print(f"Payload Preview  : {packet_info['payload']}")
    print("=" * 55)


def save_txt_report(packet_info):
    """
    Captured packet details txt report la save pannum.
    """

    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open("reports/captured_packets.txt", "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 55 + "\n")
        file.write("[+] Packet Captured\n")
        file.write("=" * 55 + "\n")
        file.write(f"Source IP        : {packet_info['source_ip']}\n")
        file.write(f"Destination IP   : {packet_info['destination_ip']}\n")
        file.write(f"Protocol         : {packet_info['protocol']}\n")
        file.write(f"Source Port      : {packet_info['source_port']}\n")
        file.write(f"Destination Port : {packet_info['destination_port']}\n")
        file.write(f"Length           : {packet_info['length']} bytes\n")
        file.write(f"Payload Preview  : {packet_info['payload']}\n")
        file.write("=" * 55 + "\n")


def save_json_report():
    """
    Captured packets list ah JSON file la save pannum.
    """

    if not os.path.exists("reports"):
        os.makedirs("reports")

    with open("reports/captured_packets.json", "w", encoding="utf-8") as file:
        json.dump(captured_packets, file, indent=4)


def process_packet(packet, config):
    """
    Every captured packet ku analysis + display + save + log pannum.
    """

    packet_info = analyze_packet(
        packet,
        payload_limit=config.get("payload_limit", 80)
    )

    captured_packets.append(packet_info)

    print_packet(packet_info)

    if config.get("save_txt", True):
        save_txt_report(packet_info)

    if config.get("save_json", True):
        save_json_report()

    logger.info(
        f"{packet_info['protocol']} Packet | "
        f"{packet_info['source_ip']} -> {packet_info['destination_ip']} | "
        f"Length: {packet_info['length']} bytes"
    )


def start_sniffing(config):
    """
    Packet sniffing start pannum main function.
    """

    packet_count = config.get("packet_count", 20)
    interface = config.get("interface", "")
    packet_filter = config.get("filter", "")

    print("\n[+] NetSniffX Started...")
    print("[+] Capturing packets...")
    print("[!] Use this only on your own system / lab network.")
    print("-" * 55)

    sniff_options = {
        "prn": lambda packet: process_packet(packet, config),
        "count": packet_count,
        "store": False
    }

    if interface:
        sniff_options["iface"] = interface

    if packet_filter:
        sniff_options["filter"] = packet_filter

    try:
        sniff(**sniff_options)

        print("\n[+] Sniffing Completed")
        print(f"[+] Total Packets Captured: {len(captured_packets)}")
        print("[+] TXT Report saved: reports/captured_packets.txt")
        print("[+] JSON Report saved: reports/captured_packets.json")
        print("[+] Logs saved: logs/packets.log")

    except PermissionError:
        print("\n[ERROR] Permission denied.")
        print("Run terminal as Administrator and try again.")

    except Exception as e:
        print("\n[ERROR] Something went wrong:")
        print(e)