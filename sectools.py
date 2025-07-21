import network_utils
import requests as re

def url_bruteforcer():
    #Functions calls
    target_url = network_utils.get_url()

    while True:
        target_ports = network_utils.get_target_ports()

        #Prompt user confirmation for large number of ports
        if len(target_ports) > 10:

            print(f'[WARNING]: High number of ports specified ({len(target_ports)}). This will cause significant delays.')
            input_confirm_operation = input('Are you sure? (y/n)').lower().strip()

            if input_confirm_operation == 'n':
                continue
            elif input_confirm_operation == 'y' or input_confirm_operation == '':
                break
            else:
                print('Invalid choice. Please type "y" or simply press enter to confirm, or type "n" to quit.')
                continue
        break


    wordlist = network_utils.get_wordlist()
    

    #Bruteforcer
    scanned_directories = []

    for word in wordlist:
        for target_port in target_ports:
            full_target_url = f'{target_url}:{target_port}/{word}'
            req = re.get(full_target_url)
            
            if (req.status_code == 200 and not full_target_url in scanned_directories):
                print(f'Found: {full_target_url}')
                scanned_directories.append(full_target_url)

def port_scanner():
    target_ips = network_utils.get_target_ip()
    target_ports = network_utils.get_target_ports()

    
    open_ports = []
    scanned_ports = []
    scanned_ips = []

    for target_ip in target_ips:
        print(f"Scanning for open ports ({len(target_ports)} ports provided) in {target_ip}...\n")
        scanned_ips.append(target_ip)
        for target_port in target_ports:
            
            s = network_utils.new_socket()
            s_connection = s.connect_ex((target_ip, target_port))
            scanned_ports.append(target_port)

            if s_connection == 0:
                print(f'{target_port}: Open')
                open_ports.append(target_port)

            s.close()
        
    
   
        

    return target_ports, scanned_ips, scanned_ports, open_ports