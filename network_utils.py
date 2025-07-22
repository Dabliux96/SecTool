import socket
import requests as re
import system_utils
import strings_utils

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
                print(f'\n{strings_utils.error_message} {target_ports[i]} is not a valid port. Try again.')
                break
        else:
            return target_ports

def get_hostname():
    target_ips = get_target_ip()

    hostnames = {}
    
    for target_ip in target_ips:

        hostname = socket.gethostbyaddr(target_ip)[0]

        hostnames[target_ip] = hostname
        
    return hostnames

def get_url():
    target_url = input("URL: ").strip().lower()

    if not target_url.startswith('http://') or not target_url.startswith('https://'):
        target_url = f'http://{target_url}'
    
    return target_url

def get_wordlist():

    #Nested functions for retrieving wordlist in different ways
    def get_wordlist_local():
        wordlist_path = input('Wordlist local path: ')
        with open (wordlist_path, 'r') as wordlist_file:
            return wordlist_file.read()



    def get_wordlist_default_online(wordlist_choice, dirbuster_wordlists):
        
        wordlist_choice = wordlist_choice - 1
        wordlist_name = dirbuster_wordlists[wordlist_choice]
        dirbuster_wordlist_url = f'https://raw.githubusercontent.com/brutalgg/dirbuster-wordlist/refs/heads/master/{wordlist_name}'

        #Wordlist request. Return error if cannot reach it.
        raw_wordlist_req = re.get(dirbuster_wordlist_url)
        
        is_request_ok = True

        if not raw_wordlist_req.status_code == 200:
            print(f"{system_utils.error_message} Cannot reach wordlist. Choose a different default wordlist or specify a local path.")
            is_request_ok = False
        

        return raw_wordlist_req.text, is_request_ok
        

    #Main function
        #wordlist names
    dirbuster_wordlists = ['apache-user-enum-1.0.txt',
    'apache-user-enum-2.0.txt',
    'directory-list-1.0.txt',
    'directory-list-2.3-big.txt',
    'directory-list-2.3-medium.txt',
    'directory-list-2.3-small.txt',
    'directory-list-lowercase-2.3-big.txt',
    'directory-list-lowercase-2.3-medium.txt',
    'directory-list-lowercase-2.3-small.txt']

    #Main function
    while True:
        for dirbuster_wordlist in dirbuster_wordlists:
            print(f'{dirbuster_wordlists.index(dirbuster_wordlist) + 1 }. {dirbuster_wordlist}')

        print('-' * 20)
        print('0. Custom local wordlist file')
        print('-' * 20)
        
        while True:
            try:
                wordlist_choice = int(input('Choose a wordlist: ').strip())

                if wordlist_choice == 0:
                    raw_wordlist = get_wordlist_local()
                    break

                else:
                    raw_wordlist, is_request_ok = get_wordlist_default_online(wordlist_choice, dirbuster_wordlists)
                    if is_request_ok == False:
                        continue
                    break

            except (IndexError, ValueError):
                print(f'\n{strings_utils.error_message} Invalid choice.\n')
                continue

        #Wordlist
        raw_wordlist = raw_wordlist.splitlines()
        break

    wordlist = []

    for word in raw_wordlist:
        if not word.startswith('#'):
            wordlist.append(word)
    
    return wordlist

def new_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)