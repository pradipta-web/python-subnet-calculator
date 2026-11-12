# Python Subnet Calculator

A Python-based subnet calculator that provides IPv4 network information using CIDR notation.

## Features

- IPv4 address validation.
- CIDR prefix identification.
- Subnet mask calculation.
- Wildcard mask calculation.
- Network address calculation.
- Broadcast address calculation.
- First and last usable host addresses.
- Total IP address calculation.
- Usable host calculation.
- Support for `/31` and `/32` networks.

## Technologies

- Python 3
- ipaddress (Python Standard Library)

## Installation

Clone this repository:

```bash
git clone https://github.com/pradipta-web/python-subnet-calculator.git
```

Navigate to the project directory:

```bash
cd python-subnet-calculator
```

Run the program:

```bash
py main.py
```

## Usage

Enter an IPv4 address followed by its CIDR prefix.

Example:

```text
Enter IPv4 address with CIDR: 192.168.10.25/24
```

## Example Output

```text
IP Address       : 192.168.10.25
CIDR             : /24
Subnet Mask      : 255.255.255.0
Wildcard Mask    : 0.0.0.255
Network Address  : 192.168.10.0
Broadcast Address: 192.168.10.255
First Host       : 192.168.10.1
Last Host        : 192.168.10.254
Total Addresses  : 256
Usable Hosts     : 254
```

## Learning Objectives

- Understanding IPv4 addressing.
- Learning CIDR notation.
- Understanding subnet masks.
- Learning network and broadcast addresses.
- Practicing Python programming.
- Using Python's ipaddress module.

## Disclaimer

This project is intended for educational purposes and networking practice.

## Author

**Pradipta Raditya**