import os
from pyrogram import filters
API_ID = os.environ.get("API_ID", 20892750)
API_HASH = os.environ.get("API_HASH", "b0241677a3a2958667e93fa9a632c350")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7369768633:AAEqkFbPqID4eLCdn34rjj9MaQzDvvwMsSI")
UPDATE_CHNL = os.environ.get("UPDATE_CHNL", "sonamsupport")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP", "sonamsupport")
LOG_GROUP_ID=os.environ.get("LOG_GROUP_ID",-1002421019887)
START_IMG = os.environ.get(
    "START_IMG", "https://graph.org/file/d4412c7b411ca8da9e177.jpg"
)
STKR = os.environ.get(
    "STKR",
    "CAACAgUAAx0CaYuwqgACyjVkV5IgG7ufiEHNHvpO38W5S-yKUwACKQgAAh7QuFb43XOj0Mt-yy8E",
)
BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
MONGO_DATABASE_URI = os.environ.get("MONGO_DATABASE_URI","mongodb+srv://Mukesh01:mstboy@cluster0.8jwzl.mongodb.net/myFirstDatabase?retryWrites=true
&w=majority")
OWNER_ID=os.environ.get("OWNER_ID",7785947978)
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()
# directories
LOAD = []
NO_LOAD = []
BANNED_USERS = filters.user()
SUDOERS=filters.user()
SUDOERS.add(OWNER_ID) 
