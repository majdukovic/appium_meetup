from config.devices_local import desired_caps
global config

'''
   Local configuration file for Android device (Samsung Galaxy Nexus, OS v7.0)
'''

config = {}

######################
##      SERVER     ##
######################

config['server_url'] = 'http://localhost:4723/wd/hub'


######################
##      CLIENT      ##
######################

DEVICE_NAME = 'google_nexus_7_0'
PLATFORM = 'Android'

config['device_name'] = DEVICE_NAME
config['device_config'] = desired_caps[DEVICE_NAME]
config['platform'] = PLATFORM
