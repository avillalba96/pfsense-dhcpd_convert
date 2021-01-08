import re

REGEX_HOSTNAME = r"(^|^#)host (.*?)(?:\{|\n\{)"
REGEX_MAC = r"hardware ethernet (.*?);"
REGEX_IP = r"fixed-address (.*?);"

def main():

    config = fetch_config()
    hostnames = get_hostnames(config)
    mac = get_mac_addresses(config)
    ip = get_fixed_ips(config)

    template = get_template()

    if (len(hostnames) == len(mac) and len(mac) == len(ip)):
        print(f"OK, got {len(hostnames)} hosts")

        f_out = open('out.xml', 'a')

        for i in range(0, len(hostnames)):
            curr_hostname = hostnames[i]
            curr_mac = mac[i]
            curr_ip = ip[i]

            if curr_hostname.startswith("#"):
                # Commented line, ignore
                continue
                
            f_out.write(f"{template.replace('[MACADDRESS_HERE]',curr_mac).replace('[IPADDRESS_HERE]',curr_ip).replace('[HOSTNAME_HERE]', curr_hostname)}\n")

        f_out.close()
        print("Done!")

    return


def get_template():

    f = open('template.xml', 'r')
    template = f.read()
    f.close()

    return template

def remove_commented(hostnames, mac, ip, commented_ids):

    for commented_id in commented_ids:
        hostnames.pop(commented_id)
        mac.pop(commented_id)
        ip.pop(commented_id)
    
    return hostnames, mac, ip


def get_hostnames(config):

    hostnames = []
    hostnames_found = re.compile(REGEX_HOSTNAME, re.MULTILINE)

    for match in hostnames_found.finditer(config):
        hostnames.append(f"{match.group(1)}{match.group(2)}")

    return hostnames

def get_mac_addresses(config):

    mac_addresses = []
    mac_addresses_found = re.compile(REGEX_MAC, re.MULTILINE)

    for match in mac_addresses_found.finditer(config):
        mac_addresses.append(match.group(1))

    return mac_addresses

def get_fixed_ips(config):

    ip_addresses = []
    ip_addresses_found = re.compile(REGEX_IP, re.MULTILINE)

    for match in ip_addresses_found.finditer(config):
        ip_addresses.append(match.group(1))

    return ip_addresses


def fetch_config():

    f = open('dhcpd.conf', 'r')
    conf = f.read()
    f.close()

    return conf
    

if __name__ == '__main__':
    main()