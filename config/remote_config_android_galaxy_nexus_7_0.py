from config.devices_local import desired_caps
global config

'''
   Remote configuration file for Android device (Samsung Galaxy S8, OS v7.0)
'''

config = {}

######################
##      SERVER     ##
######################

config['server_url'] = 'https://sharedqaaccount1:o4xZw3chZPaMFMMxy2iB@hub-cloud.browserstack.com/wd/hub'


######################
##      CLIENT      ##
######################

DEVICE_NAME = 'google_nexus_7_0'
PLATFORM = 'Android'

config['device_name'] = DEVICE_NAME
config['device_config'] = desired_caps[DEVICE_NAME]
config['platform'] = PLATFORM
