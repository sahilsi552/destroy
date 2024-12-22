import shortuuid
from pymongo import MongoClient
from pyrogram import filters
from config import MONGO_DATABASE_URI
from Merisa import QuantamBot as app
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQuery,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InputTextMessageContent,
)
import requests,json
from pyrogram.enums import  ParseMode
from bs4 import BeautifulSoup

keywords_list = ["google", "pypi", "github","whisper"]
PRVT_MSGS = {}
client = MongoClient(MONGO_DATABASE_URI)
db = client["whisperdb"]
collection = db["whisper"]

# Whispers Class
class Whispers:
    @staticmethod
    def add_whisper(whisper_id, whisper_data):
        whisper = {"WhisperId": whisper_id, "whisperData": whisper_data}
        collection.insert_one(whisper)

    @staticmethod
    def del_whisper(whisper_id):
        collection.delete_one({"WhisperId": whisper_id})

    @staticmethod
    def get_whisper(whisper_id):
        whisper = collection.find_one({"WhisperId": whisper_id})
        return whisper["whisperData"] if whisper else None

  # Make sure to configure your bot token

# Inline query handler
@app.on_inline_query()
def main_whisper(client, inline_query):
    query = inline_query.query
    if not query:
        return inline_query.answer(
            [],
            switch_pm_text="Give me a username or ID!",
            switch_pm_parameter="ghelp_whisper",
        )

    user, message = parse_user_message(query)  # Implement this function
    if len(message) > 200:
        return

    user_type = "username" if user.startswith("@") else "id"

    if user.isdigit():
        try:
            chat = client.get_chat(int(user))
            user = f"@{chat.username}" if chat.username else chat.first_name
        except Exception:
            pass

    whisper_data = {
        "user": inline_query.from_user.id,
        "withuser": user,
        "usertype": user_type,
        "type": "inline",
        "message": message,
    }
    whisper_id = shortuuid.uuid()

    # Add the whisper to the database
    Whispers.add_whisper(whisper_id, whisper_data)

    answers = [
        InlineQueryResultArticle(
            id=whisper_id,
            title=f"👤 Send a whisper message to {user}!",
            description="Only they can see it!",
            input_message_content=f"🔐 A Whisper Message For {user}\nOnly they can see it!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "📩 𝗦𝗵𝗼𝘄 𝗪𝗵𝗶𝘀𝗽𝗲𝗿 📩",
                            callback_data=f"whisper_{whisper_id}",
                        )
                    ]
                ]
            ),
        )
    ]

    client.answer_inline_query(inline_query.id, answers)

# Callback query handler
@app.on_callback_query(filters.regex(r"^whisper_"))
def show_whisper(client, callback_query):
    whisper_id = callback_query.data.split("_")[-1]
    whisper = Whispers.get_whisper(whisper_id)

    if not whisper:
        client.answer_callback_query(callback_query.id, "This whisper is not valid anymore!")
        return

    user_type = whisper["usertype"]
    from_user_id = callback_query.from_user.id

    if from_user_id == whisper["user"]:
        client.answer_callback_query(callback_query.id, whisper["message"], show_alert=True)
    elif (user_type == "username" and callback_query.from_user.username and 
          callback_query.from_user.username.lower() == whisper["withuser"].replace("@", "").lower()):
        client.answer_callback_query(callback_query.id, whisper["message"], show_alert=True)
    elif user_type == "id" and from_user_id == int(whisper["withuser"]):
        client.answer_callback_query(callback_query.id, whisper["message"], show_alert=True)
    else:
        client.answer_callback_query(callback_query.id, "Not your Whisper!", show_alert=True)
def parse_user_message(query_text):
    text = query_text.split(" ")
    user = text[0] if text[0].startswith("@") or text[0].isdigit() else text[-1]

    # Extract message while ensuring user is at a valid index
    message = " ".join(text[1:] if user == text[0] else text[:-1])

    # Return username and message
    return user, message.strip()

