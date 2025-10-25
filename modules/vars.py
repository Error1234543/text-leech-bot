import os

API_ID    = os.environ.get("API_ID", "20619533")
API_HASH  = os.environ.get("API_HASH", "5893568858a096b7373c1970ba05e296")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8483889672:AAHF218gaOzYjnoarBrJhNylBmw2C2H65CE") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
