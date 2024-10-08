import re
from os import environ, getenv
from Script import script
from pymongo import MongoClient

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '23271365'))
API_HASH = environ.get('API_HASH', '59a8393f1c17083798b42333d16ff224')
BOT_TOKEN = environ.get('BOT_TOKEN', "8190411902:AAEbw3ctiihWVTDDOSs8Wv4ExubznyjNH8M")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', "True"), True)

# Sample images
PICS = environ.get('PICS', 'https://telegra.ph/file/sample.jpg').split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/sample.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/sample.mp4")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split() if admin]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split() if ch]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://kisakc079:QbZkAsk0oXhBJOIB@cluster0.nznop.mongodb.net")
DATABASE_NAME = environ.get('DATABASE_NAME', "kisakc079")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Verification settings
VERIFY = is_enabled(environ.get('VERIFY', "False"), False)
HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://t.me/')

# Miscellaneous settings
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'instantearn.in')
IS_SHORTLINK = is_enabled(environ.get('IS_SHORTLINK', "False"), False)

# Example log channel
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))

# Online stream settings
STREAM_SITE = environ.get('STREAM_SITE', 'ziplinker.net')
STREAM_API = environ.get('STREAM_API', 'default_stream_api_key')

# IMDB Settings
IMDB = is_enabled(environ.get('IMDB', "False"), False)

# Other configurations...
