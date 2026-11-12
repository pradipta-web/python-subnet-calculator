import ipaddress


def calculate_subnet(ip_input):
    try:
        interface = ipaddress.IPv4Interface(ip_input)
        network = interface.network

        total_addresses = network.num_addresses

        if network.prefixlen <= 30:
            usable_hosts = total_addresses - 2
            first_host = network.network_address + 1
            last_host = network.broadcast_address - 1

        elif network.prefixlen == 31:
            usable_hosts = 2
            first_host = network.network_address
            last_host = network.broadcast_address

        else:
            usable_hosts = 1
            first_host = network.network_address
            last_host = network.network_address

        print("\n" + "=" * 50)
        print("             SUBNET CALCULATOR")
        print("=" * 50)

        print(f"IP Address       : {interface.ip}")
        print(f"CIDR             : /{network.prefixlen}")
        print(f"Subnet Mask      : {network.netmask}")
        print(f"Wildcard Mask    : {network.hostmask}")
        print(f"Network Address  : {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"First Host       : {first_host}")
        print(f"Last Host        : {last_host}")
        print(f"Total Addresses  : {total_addresses}")
        print(f"Usable Hosts     : {usable_hosts}")

        print("=" * 50)

    except ValueError:
        print("\nInvalid IPv4 address or CIDR notation!")


def main():
    print("=" * 50)
    print("             PYTHON SUBNET CALCULATOR")
    print("=" * 50)

    ip_input = input("Enter IPv4 address with CIDR: ")

    calculate_subnet(ip_input)


if __name__ == "__main__":
    main()