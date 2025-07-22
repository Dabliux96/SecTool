import network_utils
import strings_utils
import requests as re
import file_utils

###########################
## URL BRUTEFORCER
## Scans for URL folders
###########################
def url_bruteforcer():
    #Functions calls
    target_url = network_utils.get_url()

    while True:
        target_ports = network_utils.get_target_ports()

        #Prompt user confirmation for large number of ports
        if len(target_ports) > 10:

            print(f'{strings_utils.warning_message} High number of ports specified ({len(target_ports)}). This will cause significant delays.')
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

    for target_port in target_ports:

        port_exists = False

        try:
            
            for word in wordlist:
                
                full_target_url = f'{target_url}:{target_port}/{word}'
                req = re.get(full_target_url)
                
                if (req.status_code == 200 and not full_target_url in scanned_directories):
                    if not port_exists:
                        print(f'\n{strings_utils.separator}\nScanning {target_url}:{target_port}...')
                        port_exists = True

                    scanned_directories.append(full_target_url)

                    print(f'    * Found: {full_target_url}')
                    

        except re.exceptions.ConnectionError:
            continue
            
###########################
## PORT SCANNER
## Scans for ports
###########################
def port_scanner():
    target_ips = network_utils.get_target_ip()
    target_ports = network_utils.get_target_ports()

    
    scanned_ips = []

    for target_ip in target_ips:
        open_ports = []
        scanned_ports = []
        

        print(f"\n{strings_utils.separator}\nScanning for open ports ({len(target_ports)} ports provided) in {target_ip}...\n")
        scanned_ips.append(target_ip)
        for target_port in target_ports:
            
            s = network_utils.new_socket()
            s_connection = s.connect_ex((target_ip, target_port))
            scanned_ports.append(target_port)

            if s_connection == 0:
                print(f'{target_port}: Open')
                open_ports.append(target_port)

            s.close()
        print(f"{len(open_ports)} open ports found in {target_ip}.")
        
    return target_ports, scanned_ips, scanned_ports, open_ports


def virustotal():
    #target_ip = network_utils.get_target_ip()
    File_hashes = file_utils.get_file()
    #hash_algorithm = file_utils.get_hash_algorithm()


    def file_upload():
        VT_API_URL = '"https://www.virustotal.com/api/v3/files"'
        

        #upload to VT
        VT_API_KEY = input('VT API KEY: ')
        headers = {
            "accept": "application/json",
            "x-apikey": VT_API_KEY,
            "content-type": "multipart/form-data; boundary=--011000010111000001101001"
        }

        files = file_utils.get_file()

        for file in files:
            response = re.post(VT_API_URL, data=file, headers=headers)

        return files

    file_upload()

def urlscan():
    pass

virustotal()

virustotal()