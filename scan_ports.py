import network_utils

def scan_ports():
    scanned_ports = []

    while True:
        target_IPs = network_utils.get_target_ip()
        
        if not len(target_IPs) == 1:
            print('[ERROR] Only 1 IP per scan allowed!')
            continue

        target_ports = network_utils.get_target_ports()
        
        
        print('\n')

        for target_port in target_ports:
        
            s = network_utils.new_socket()
            s_connection = s.connect_ex((target_IPs[0], target_port))

            if s_connection == 0:
                print(f'{target_port}: Open')
                scanned_ports.append(target_port)
            s.close()

        
        print(f'\nOpen Ports: {(''.join(str(scanned_ports)))}')
        return scanned_ports
        

scan_ports()