import subprocess
def bash_cmd(cmd):
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if output:
        print(output.decode("utf-8") )
    if error:
        print(error.decode("utf-8") )


# Trying to set kernelname...
#try:
#    import toml
#    CONFIG = toml.load('./config.toml')
#    kernel_name = CONFIG['kernel_name']
#except:
#    try:
#        bash_cmd("pipenv install toml")
#        import toml
#        CONFIG = toml.load('./config.toml')
#        kernel_name = CONFIG['kernel_name']
#    except:
#        # Open TOML without package
#        with open('./config.toml', 'r') as config_file:
#            kernel_name = ''
#            for line in config_file.readlines():
#                if 'kernel_name' in line:
#                    kernel_name = line.rstrip().split("=")[-1].lstrip().replace("'", "").replace('"',"")
#                    break
#        if not kernel_name:
#            kernel_name = 'pipenvtest1'
#print(f'Setting kernel name to {kernel_name}')
        
    
#import pandas as pd
#import numpy as np
#import dapla as dp