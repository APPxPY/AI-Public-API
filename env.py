import os

################ Network settings ################
HOST = 'localhost'
PORT = 8080
##################################################

##################### Limits #####################
PHOTO_PROCESSING = 5 # Per minute
AUDIO_PROCESSING = 5 # Per minute
##################################################

################## AI Settings ###################
TRAIN_MODE = False
DEBUG = True # Do not use in production
INFO_PAGE = False
##################################################

# ###################### SSL #######################
# ENABLE_HTTPS = False
# CERT_FILE = "appxpy.crt"
# KEY_FILE = "appxpy.key"
# CERT_DIR = os.path.dirname(os.path.realpath(__file__))

# COUNTRY = 'US'
# STATE = 'New York'
# CITY = 'New York City'
# ORGANIZATION_NAME = 'Appxpy Inc.'
# ORGANIZATION_UNIT_NAME = 'Development unit'
# EMAIL = 'appxpy@appxpy.com'
# ##################################################