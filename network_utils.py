import socket
import requests as re
import system_utils

def get_own_ip_private():

    #ifconfig_base_cmd = system_utils.generate_system_cmd().replace('', 'ifconfig')
    ifconfig_base_cmd = system_utils.generate_system_cmd().format(cmd='ifconfig')
    cmd = ifconfig_base_cmd

    ifconfig_full_cmd = system_utils.subprocess_command(cmd).splitlines()

    for line in ifconfig_full_cmd:
        if line.startswith('eth'):
            interface = line.split(':')[0]
            ip = ifconfig_full_cmd[ifconfig_full_cmd.index(line) + 1].strip().split(' ')[1]
            interface_ip = dict(interface = interface, ip = ip)

    return interface_ip['ip']

def get_own_ip_public():
    public_ip = re.get('https://api.ipify.org?format=json').json()['ip']
    return public_ip
    #user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    #headers = {'user-agent': user_agent}
    #req = re.get('https://whatismyipaddress.com/', headers=headers, allow_redirects=True).text
    #req = re.get('https://api.ipify.org?format=json').text
    #public_ip = req.split(':"')[1].strip().replace('"}', '')

def get_target_ip():
    target_IPs = input("Target IP(s): ").replace(' ', '').split(',')
    return target_IPs

def get_target_ports():
    valid_ports = range(1, 65536)

    while True:
        target_ports = input("Target port(s): ").replace(' ', '').split(',')

        if target_ports == ['']:
            return list(valid_ports)

        for i in range(len(target_ports)):
            target_ports[i] = int(target_ports[i])
            if target_ports[i] not in valid_ports:
                print(f'\n[!] ERROR: {target_ports[i]} is not a valid port. Try again.')
                break
        else:
            return target_ports




# def get_target_ports():
#     valid_ports = range(1,65536)

#     while True:
#         target_ports = input("Target port(s): ").replace(' ', '').split(',')

#         for target_port in target_ports:
#             target_port = int(target_port)
#             if not target_port in valid_ports:
#                 print(f'\n[!] ERROR: {target_port} is not a valid port. Try again.')
#                 break
#         else: # tied to for loop, ensures that the return only runs if for loop was not broken. As if "for [...] if not break [...]"
#             return target_ports

def new_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)