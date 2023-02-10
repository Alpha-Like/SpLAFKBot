
from os import getenv

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "")

# Database to save your chats and stats...
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

# SUDO USERS
SUDO_USER = list(
    map(int, getenv("SUDO_USER", "").split())
)  # Input type must be interger

# VARS BELOW ARE NON MANDATORY !

# START IMAGE 
START_IMAGE = getenv("START_IMAGE", "")

# WELCOME IMAGE
WELCOME_IMAGE = getenv("WELCOME_IMAGE", "")

# SETTINGS IMAGE
SETTINGS_IMAGE = getenv("SETTINGS_IMAGE", "")
