import os

API_ID = API_ID = 25017900

API_HASH = os.environ.get("API_HASH", "3830600881a164826e60f2806b28e666")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8012673189:AAFyG4TRkK_N33ngPA-12DEhEW_Xfi6sBBI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER",7376514183 ))

LOG = 1,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7376514183").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


