"""
======================================================================================================================
Author:                         {root@lonedevwolf}
Language:                       Python
Modules:
Description:
======================================================================================================================
[!]:

"""
# Firewall simulation program in python
import random


# Generate Random Ip addresses
def generate_random_ip():
    return f"192.168.1.{random.randint(0, 20)}"


# Declaring firewalls rules
def check_firewall_rules(ip, rules):
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"


# Main firewall rules
def main():
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }

    for _ in range(12):
        ip_address = generate_random_ip()
        action = check_firewall_rules(ip_address, firewall_rules)
        random_number = random.randint(0, 9999)
        print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")


# Execute the firewall simulation program
if __name__ == "__main__":
    main()
