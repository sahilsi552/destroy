import os
from pyrogram import filters

API_ID = os.environ.get("API_ID", 25488022)
API_HASH = os.environ.get("API_HASH", "0c999a454fddd79251213be7944811e8")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6985264082:AAH2CYZfVBj9YGce7chLUehZR7b_nQHgcHQ")
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "mr_sukkun")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "the_support_chat")
LOG_GROUP_ID=os.environ.get("LOG_GROUP_ID",-1002155001851)
START_IMG = os.environ.get(
    
    "START_IMG", "https://graph.org/file/d4412c7b411ca8da9e177.jpg"
)
STKR = os.environ.get(
    "STKR",
    "CAACAgUAAx0CaYuwqgACyjVkV5IgG7ufiEHNHvpO38W5S-yKUwACKQgAAh7QuFb43XOj0Mt-yy8E",
)
BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
MONGO_DATABASE_URI = os.environ.get("MONGO_DATABASE_URI","mongodb+srv://Mukesh01:mstboy@cluster0.8jwzl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER_ID=os.environ.get("OWNER_ID",6728038801)
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()


# directories
LOAD = []

NO_LOAD = []
BANNED_USERS = filters.user()
SUDOERS=filters.user()
SUDOERS.add(OWNER_ID)