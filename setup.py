#python 3

"""
		should be only commands run for hooking up new device...
 $ ssh pi@?.?.?.?
 $ sudo apt install git
 $ git clone https://github.com/kinson/networks_project_scripts.git
 $ python /networks_project_scripts/setup.py


# easy of network config
"""

#
#	imports
#

# standard
import os

#internal
import config_handler

#
#config settings
#

#client
client_cfg_fname = "client/client_config.cfg"
client_name_key = "DEVICE_NAME"

#
#	install dependencies
#

os.system('sudo apt-get update')
os.system('sudo apt-get install tmux')
os.system('sudo apt-get install nmap')
os.system('sudo pip install python-libnmap')

#
#	capture device name
#

#set permisions
os.system('sudo chmod 755 ' + client_cfg_fname)

device_name = input('Enter your device name: ')
config_handler.set_value(client_cfg_fname, client_name_key, device_name)


