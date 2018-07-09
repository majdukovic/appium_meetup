global desired_caps
'''
    Desired capabilities used for installing the app and starting desired emulator
'''

desired_caps = {
    'google_nexus_7_0': {
        'app': '/Users/majdukovic/Documents/MB_4_1_1_app.apk',
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'Google Nexus 7.0',
        'avd': 'Galaxy_Nexus_7.0',
        'appWaitPackage': 'com.matchbook.client',
        'appWaitActivity': 'com.android.xanadu.matchbook.MainActivity',
        'autoGrantPermissions' : True
    }
