import yaml
from colorama import Fore, Style, init
from sniffer import start_sniffing


init(autoreset=True)


def load_config():
    """
    config.yaml file la iruka settings load pannum.
    """

    try:
        with open("config.yaml", "r") as file:
            config = yaml.safe_load(file)

            if config is None:
                return {}

            return config

    except FileNotFoundError:
        print(Fore.RED + "[ERROR] config.yaml file not found.")
        return {}

    except Exception as e:
        print(Fore.RED + "[ERROR] Failed to load config file.")
        print(e)
        return {}


def show_banner():
    """
    NetSniffX terminal banner.
    """

    print(Fore.CYAN + Style.BRIGHT + r"""
 _   _      _   ____        _  __  __ __  __
| \ | | ___| |_/ ___| _ __ (_)/ _|/ _|\ \/ /
|  \| |/ _ \ __\___ \| '_ \| | |_| |_  \  / 
| |\  |  __/ |_ ___) | | | | |  _|  _| /  \ 
|_| \_|\___|\__|____/|_| |_|_|_| |_|  /_/\_\
    """)

    print(Fore.YELLOW + "Basic Network Packet Sniffer")
    print(Fore.YELLOW + "Use only on your own system / lab network")
    print("-" * 55)


def main():
    """
    Project main entry point.
    """

    show_banner()

    config = load_config()

    print(Fore.GREEN + "[+] Configuration Loaded")
    print(Fore.GREEN + f"[+] Packet Count : {config.get('packet_count', 20)}")
    print(Fore.GREEN + f"[+] Interface    : {config.get('interface', 'Default') or 'Default'}")
    print(Fore.GREEN + f"[+] Filter       : {config.get('filter', 'All Packets') or 'All Packets'}")
    print("-" * 55)

    choice = input(Fore.CYAN + "Start packet sniffing? (y/n): ").lower()

    if choice == "y":
        start_sniffing(config)
    else:
        print(Fore.RED + "[-] Sniffing cancelled.")


if __name__ == "__main__":
    main()