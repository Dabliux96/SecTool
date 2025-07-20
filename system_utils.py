import subprocess

def generate_system_cmd():
    return '{cmd}'
    #cmd = ''
    #return cmd
    
def subprocess_command(cmd):
    
    system_cmd_base = (subprocess.run([f'{cmd}'], capture_output=True, text=True)).stdout
    return system_cmd_base




# def test_func(cmd):
    
#     full_cmd = f'testing {cmd}'
#     return full_cmd