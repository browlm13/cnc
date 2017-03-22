#python 3

"""
		modual for handling confiugration files
			- read
			- add/delete
			- change
"""

#settings
ERROR_STRING = '-1'
COMMENT_CHAR = '#'

#
# pull value from config file
#

def get_value(config_fname, key):
	setting_value = ERROR_STRING

	with open(config_fname, 'r') as f:
		default_settings = f.read()

	default_settings = default_settings.split('\n')
	for line in default_settings:
		if line[0] != COMMENT_CHAR:
			setting = line.split('=')
			if setting[0] == key:
				setting_value = setting[1]

	return setting_value

def set_value(config_fname, key, value):
	#check if attribute exists
	with open(config_fname, 'r') as f:
		default_settings = f.read()

	default_settings = default_settings.split('\n')
		for line in default_settings:
			if line[0] != COMMENT_CHAR:
				setting = line.split('=')
				if setting[0] == key:
					setting[1] = value
