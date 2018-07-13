global desired_caps
'''
    Desired capabilities used for installing the app and starting desired emulator
'''

desired_caps = {
    'google_nexus_7_0': {
        'app': 'bs://01a8c30b4030c925153f690b12c5f02f6b033718',
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'Samsung Galaxy S8',
        'browserstack.idleTimeout': '10',
        'browserstack.local': True,
        'appWaitPackage': 'com.matchbook.client',
        'appWaitActivity': 'com.android.xanadu.matchbook.MainActivity',
        'autoGrantPermissions' : True
    }
}
