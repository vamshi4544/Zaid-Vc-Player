## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AQAPFogdX37BzRnkvFS98CdxLm6HhL_DFMe9oijrcPyy3kBk7rdkD81-tzS95m5mBvY22M6Ou99NiRxIHLnCYN_fI3yKzkOUVqhUn2w89fIU2m5inydVuNA10K6nY-6SfD2Y0qsjbrknIl1ZEiZSvqnz9Nyk_KLK-f1L31UDiciPukSxfl-13HMIUx4qAxVz93ZEReg2HfkKs6UCquX1xtsvA2DjjW0NBwpoGh95O5r8WjZ-yKQWKmE81MjJqlxx8ywheFEAaJ9WNxsclOBsCB4ssn_gM7UyxaE_vy51WAZ8A01wtk6_6ufen3kN4T2-Btbw4gjVXTgLY0U0VdTJnvfQAAAAAWGUmcgA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5984321053:AAFM2IAgSqqz0sgmC9IGaBUN-xKduR6H7lM")
BOT_NAME = getenv("BOT_NAME", "jessicabottt")

API_ID = int(getenv("API_ID", "9189428"))
API_HASH = getenv("API_HASH", "d32b0f09f79d791db51064966f3e6709")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Vamshi")
OWNER_USERNAME = getenv("OWNER_USERNAME", "jessicabottt")
ALIVE_NAME = getenv("ALIVE_NAME", "Vamshi")
BOT_USERNAME = getenv("BOT_USERNAME", "jessicabottt")
OWNER_ID = getenv("OWNER_ID", "5932095944")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "vamshi")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "vamshiqspiders")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "vamshiqspiders")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5932095944").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
