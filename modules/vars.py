import os

API_ID    = os.environ.get("API_ID", "20619533")
API_HASH  = os.environ.get("API_HASH", "5893568858a096b7373c1970ba05e296")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8176277339:AAFwc7xY8cTWyUNVm3Q3_HkyJXTWRyH_kkM") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
