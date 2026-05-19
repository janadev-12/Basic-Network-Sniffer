NETSNIFFX - BASIC NETWORK PACKET SNIFFER
========================================

NetSniffX is a Python-based terminal network packet sniffer. It captures live network packets and displays useful information such as source IP, destination IP, protocol, source port, destination port, packet length, and payload preview.

This project is created for learning cybersecurity, packet analysis, and basic network traffic monitoring.


PROJECT OBJECTIVE
-----------------

The main objective of this project is to understand how data flows through a network.

This tool captures packets from the user's own system or lab network and analyzes the packet details in a simple and readable format.


FEATURES
--------

1. Captures live network packets
2. Displays source IP address
3. Displays destination IP address
4. Detects protocol type such as TCP, UDP, and ICMP
5. Displays source port and destination port
6. Shows packet length
7. Shows payload preview
8. Saves captured packets in TXT report
9. Saves captured packets in JSON report
10. Stores logs for packet activity


PROJECT STRUCTURE
-----------------

netsniffx/
|
|-- main.py
|-- sniffer.py
|-- packet_analyzer.py
|-- logger.py
|-- config.yaml
|-- requirements.txt
|-- README.txt
|-- .gitignore
|
|-- logs/
|   |-- packets.log
|
|-- reports/
|   |-- captured_packets.txt
|   |-- captured_packets.json


FILE EXPLANATION
----------------

main.py
This is the main entry point of the project. It loads the configuration file, displays the project banner, and starts the packet sniffing process.

sniffer.py
This file contains the core packet capturing logic. It captures packets, sends them for analysis, displays the output, saves reports, and writes logs.

packet_analyzer.py
This file analyzes each captured packet. It extracts details such as source IP, destination IP, protocol, ports, packet length, and payload preview.

logger.py
This file creates a logger and stores packet activity in logs/packets.log.

config.yaml
This file contains project settings such as packet count, filter, payload limit, and report saving options.

requirements.txt
This file contains the Python libraries required for the project.

reports/
This folder stores captured packet reports in TXT and JSON formats.

logs/
This folder stores log files.


REQUIREMENTS
------------

Python 3.x

Required Python libraries:

1. scapy
2. pyyaml
3. colorama

For Windows users, Npcap must be installed for packet sniffing to work properly.


INSTALLATION
------------

Step 1: Clone or download the project.

Step 2: Open the project folder in VS Code.

Step 3: Install the required libraries:

pip install -r requirements.txt

Step 4: For Windows, install Npcap.

During Npcap installation, enable this option:

Install Npcap in WinPcap API-compatible Mode


HOW TO RUN
----------

Open terminal inside the project folder and run:

python main.py

Then type:

y

to start packet sniffing.


CONFIGURATION
-------------

The project settings can be changed in config.yaml.

Example:

packet_count: 20
interface: ""
filter: ""
save_txt: true
save_json: true
show_payload: true
payload_limit: 80

Explanation:

packet_count:
Number of packets to capture.

interface:
Network interface to use. If empty, default interface will be used.

filter:
Packet filter. If empty, all packets will be captured.

save_txt:
Saves captured packets in TXT format.

save_json:
Saves captured packets in JSON format.

show_payload:
Shows payload preview.

payload_limit:
Limits the number of payload characters shown.


EXAMPLE OUTPUT
--------------

[+] Packet Captured
=======================================================
Source IP        : 10.232.42.160
Destination IP   : 10.232.42.89
Protocol         : UDP
Source Port      : 53
Destination Port : 62293
Length           : 153 bytes
Payload Preview  : No payload
=======================================================


OUTPUT EXPLANATION
------------------

Source IP:
Shows where the packet is coming from.

Destination IP:
Shows where the packet is going.

Protocol:
Shows the network protocol used by the packet.

Source Port:
Shows the sender-side port number.

Destination Port:
Shows the receiver-side port number.

Length:
Shows the packet size in bytes.

Payload Preview:
Shows a small preview of the packet content. If the data is encrypted or unreadable, it may show symbols or "No payload".


REPORTS
-------

After packet sniffing is completed, reports are saved automatically.

TXT report:

reports/captured_packets.txt

JSON report:

reports/captured_packets.json

Log file:

logs/packets.log


USE CASES
---------

1. Learning packet sniffing basics
2. Understanding TCP, UDP, and ICMP protocols
3. Understanding DNS and HTTPS traffic
4. Basic network traffic monitoring
5. Cybersecurity learning and practice
6. GitHub portfolio project
7. Resume project for cybersecurity beginners


LIMITATIONS
-----------

1. Encrypted traffic cannot be fully read.
2. HTTPS, QUIC, and secure traffic payloads may appear as unreadable symbols.
3. Some packets may show N/A if IP details are not available.
4. This tool is for learning and authorized testing only.


LEGAL DISCLAIMER
----------------

This project is created only for educational and ethical cybersecurity learning.

Use this tool only on your own system, your own Wi-Fi, or an authorized lab network.

Do not use this tool to capture traffic from networks or devices without permission. Unauthorized packet sniffing may be illegal.


RESUME DESCRIPTION
------------------

Built NetSniffX, a Python-based terminal network packet sniffer that captures live network packets and analyzes source IP, destination IP, protocol, ports, packet length, and payload preview. The tool also saves captured traffic in TXT and JSON reports for further analysis.


AUTHOR
------

JANAVANTH R
Cybersecurity and AI/ML Enthusiast
GitHub: https://github.com/janadev-12
LinkedIn: www.linkedin.com/in/janavanth-r