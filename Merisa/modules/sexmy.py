import shortuuid
from pymongo import MongoClient
from config import MONGO_DATABASE_URI
from Merisa import QuantamBot as app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
import random
from pyrogram.enums import ParseMode

# MongoDB setup
client = MongoClient(MONGO_DATABASE_URI)
db = client["whisperdb"]
collection = db["whisper"]

# Constants
THUMB_URL = "https://i.ibb.co/Dgd586R/file-5790.jpg"
WHISPER_THUMB_URL = "https://i.ibb.co/YkCmFJ4/whisper-thumb.jpg"  # Custom thumbnail for whispers
BUTTON = [[InlineKeyboardButton("🔍 Check Your Result", switch_inline_query_current_chat="")]]

# Whispers class for database operations
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

# Function to extract mention based on query
def extract_mention(query, user_id, user_name):
    if query:
        target_name = query.strip()
        mention = f"[{target_name}](tg://user?id={user_id})"
    else:
        mention = f"[{user_name}](tg://user?id={user_id})"
    return mention

# Inline query handler
@app.on_inline_query()
async def handle_inline_query(client, inline_query: InlineQuery):
    query = inline_query.query.strip()
    user_id = inline_query.from_user.id
    user_name = inline_query.from_user.first_name
    
    mention = extract_mention(query, user_id, user_name)
    results = []

    if query.startswith("@") or query.isdigit():
        user, message = parse_user_message(query)
        if len(message) > 200:
            await inline_query.answer([], cache_time=1, is_personal=True)
            return

        user_type = "username" if user.startswith("@") else "id"

        if user.isdigit():
            try:
                chat = await client.get_chat(int(user))
                user = f"@{chat.username}" if chat.username else chat.first_name
            except Exception as e:
                print(f"Error fetching chat details: {e}")

        whisper_data = {
            "user": inline_query.from_user.id,
            "withuser": user,
            "usertype": user_type,
            "type": "inline",
            "message": message,
        }
        whisper_id = shortuuid.uuid()

        Whispers.add_whisper(whisper_id, whisper_data)

        results.append(
            InlineQueryResultArticle(
                id=whisper_id,
                title=f"👤 Send a whisper message to {user}!",
                description="Only they can see it!",
                input_message_content=InputTextMessageContent(
                    message_text=f"🔐 A Whisper Message For {user}\nOnly they can see it!"
                ),
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
                thumb_url=WHISPER_THUMB_URL,  # Custom image for whispers
            )
        )
    else:
        random_responses = generate_random_responses(mention, user_name, query)
        results.extend(random_responses)

    if results:
        await inline_query.answer(results, cache_time=1, is_personal=True)
    else:
        await inline_query.answer([], cache_time=1, is_personal=True)

# Generate random inline responses including marriage probability
def generate_random_responses(mention, user_name, query_name):
    mm = random.randint(1, 100)
    cm = random.randint(5, 30)
    marriage_prob = random.randint(1, 100)
    name_start = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    marriage_message = (
        f"💍 Marriage probability of {mention} with [{query_name}](tg://user?id={inline_query.from_user.id}) is {marriage_prob}%."
        if query_name else f"💍 Marriage probability of {mention} is {marriage_prob}%."
    )

    random_responses = [
        {
            "title": "Horny Level",
            "description": "Check how horny you are!",
            "text": f"🔥 {mention} is {mm}% horny!",
        },
        {
            "title": "Gayness Level",
            "description": "Check how gay you are!",
            "text": f"🍷 {mention} is {mm}% gay!",
        },
        {
            "title": "Marriage Probability",
            "description": "Check your marriage probability with someone!",
            "text": marriage_message,
        },
        {
            "title": "Name Starts With",
            "description": "Find out which letter your name starts with!",
            "text": f"🔠 Your name starts with the letter '{name_start}'.",
        },
        {
            "title": "Dick Size",
            "description": "Check the size of your dick!",
            "text": f"🍌 {mention}'s dick size is {cm} cm!",
        },
        {
            "title": "Vagina Depth",
            "description": "Check the depth of your vagina!",
            "text": f"🌹 {mention}'s vagina depth is {cm} cm!",
        },
        {
            "title": "Hotness Level",
            "description": "Check how hot you are!",
            "text": f"🔥 {mention} is {mm}% hot!",
        },
        {
            "title": "MC Level",
            "description": "Check your MC level!",
            "text": f"⚡ {mention} is {mm}% MC!",
        },
        {
            "title": "BC Level",
            "description": "Check your BC level!",
            "text": f"⚡ {mention} is {mm}% BC!",
        },
    ]

    return [
        InlineQueryResultArticle(
            id=shortuuid.uuid(),
            title=response["title"],
            description=response["description"],
            input_message_content=InputTextMessageContent(
                response["text"], disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(BUTTON),
            thumb_url=THUMB_URL,  # Thumbnail for random responses
        )
        for response in random_responses
    ]

def parse_user_message(query_text):
    text = query_text.split(" ")
    user = text[0] if text[0].startswith("@") or text[0].isdigit() else text[-1]
    message = " ".join(text[1:] if user == text[0] else text[:-1])
    return user, message.strip()

# Callback query handler for whispers
@app.on_callback_query(filters.regex(r"^whisper_"))
async def show_whisper(client, callback_query):
    whisper_id = callback_query.data.split("_")[-1]
    whisper = Whispers.get_whisper(whisper_id)

    if not whisper:
        await client.answer_callback_query(callback_query.id, "This whisper is not valid anymore!")
        return

    user_type = whisper["usertype"]
    from_user_id = callback_query.from_user.id

    if from_user_id == whisper["user"]:
        await client.answer_callback_query(callback_query.id, whisper["message"], show_alert=True)
    elif (user_type == "username" and callback_query.from_user.username and 
          callback_query.from_user.username.lower() == whisper["withuser"].replace("@", "").lower()):
        await client.answer_callback_query(callback_query.id, whisper["message"], show_alert=True)
    elif user_type == "id" and from_user_id == int(whisper["withuser"]):
        await client.answer_callback_query(callback_query.id, whisper["message"], show_alert=True)
    else:
        await client.answer_callback_query(callback_query.id, "Not your Whisper!", show_alert=True)
