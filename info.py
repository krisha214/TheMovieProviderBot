import re
from os import environ, getenv
from Script import script

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
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/sample1.jpg https://telegra.ph/file/sample2.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/sample.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/sample.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/sample.jpg")
SUBSCRIPTION = environ.get('SUBSCRIPTION', 'https://telegra.ph/file/sample.jpg')
CODE = environ.get('CODE', 'https://telegra.ph/file/sample.jpg')

# Stream link shortener
STREAM_SITE = environ.get('STREAM_SITE', 'ziplinker.net')
STREAM_API = environ.get('STREAM_API', 'your-stream-api')
STREAMHTO = environ.get('STREAMHTO', 'https://t.me/samplelink')

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in environ.get('AUTH_GROUP', '').split()] if environ.get('AUTH_GROUP') else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://kisakc079:QbZkAsk0oXhBJOIB@cluster0.nznop.mongodb.net")
DATABASE_NAME = environ.get('DATABASE_NAME', "kisakc079")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Verification
VERIFY = bool(environ.get('VERIFY', False))
HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://t.me/')  # Verification tutorial link

# Shortlink service
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'instantearn.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'your-shortlink-api')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))

# Channels and Logs
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SUPPORT_CHAT_ID = int(environ.get('SUPPORT_CHAT_ID', '')) if environ.get('SUPPORT_CHAT_ID', '').isdigit() else None
REQST_CHANNEL = int(environ.get('REQST_CHANNEL_ID', '')) if environ.get('REQST_CHANNEL_ID', '').isdigit() else None

# Others
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'Maintained by: HP')

# Premium
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '')) if environ.get('PREMIUM_LOGS', '').isdigit() else None

# Button settings
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled(environ.get('MAX_BTN', "True"), True)

# Streaming settings
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False

BIND_ADDRESS = getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0')
FQDN = getenv('FQDN', BIND_ADDRESS) if not ON_HEROKU or getenv('FQDN') else APP_NAME + '.herokuapp.com'
URL = f"https://{FQDN}/" if ON_HEROKU or NO_PORT else f"https://{FQDN}:{PORT}/"
HAS_SSL = bool(getenv('HAS_SSL', True))

# IMDb settings
IMDB = is_enabled(environ.get("IMDB", "False"), False)
AUTO_FFILTER = is_enabled(environ.get('AUTO_FFILTER', "True"), True)
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", script.CAPTION)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE_TXT)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# Online streaming
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "True"), True)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

# Stats
async def log_config():
    LOG_STR = "Current Customized Configurations are:-\n"
    LOG_STR += ("IMDB Results are enabled, showing IMDb details for your queries.\n" if IMDB else "IMDb Results are disabled.\n")
    LOG_STR += ("SINGLE_BUTTON enabled: filename and file size will be shown in a single button.\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled.\n")
    LOG_STR += (f"CUSTOM_FILE_CAPTION enabled: {CUSTOM_FILE_CAPTION}\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found.\n")
    LOG_STR += ("Long IMDb storyline enabled." if LONG_IMDB_DESCRIPTION else "Short IMDb plot enabled.\n")
    LOG_STR += ("Spell Check Mode is enabled.\n" if SPELL_CHECK_REPLY else "Spell Check Mode is disabled.\n")
    LOG_STR += (f"MAX_LIST_ELM enabled: Showing first {MAX_LIST_ELM} elements in IMDb cast list.\n" if MAX_LIST_ELM else "Showing full IMDb cast list.\n")
    return LOG_STR
