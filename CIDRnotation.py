import ipaddress

# Prompt user for IP address range
ip_range = input("Enter IP address range in CIDR notation (e.g. 192.68.7.32/28): ")

# Create an IPv4Network object from the input
network = ipaddress.IPv4Network(ip_range)

# Loop through all IP addresses in the network and print in the required format
with open('range.txt', 'w') as f:
    for ip in network:
        f.write(str(ip) + '\n')
        print(ip)

