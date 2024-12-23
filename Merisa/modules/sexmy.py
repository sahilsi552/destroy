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
    # Check if the query is non-empty
    if query:
        # Remove extra spaces and extract the target name
        target_name = query.strip()  
        mention = f"[{target_name}](tg://user?id={user_id})"
    else:
        # Default to the user who sent the query
        mention = f"[{user_name}](tg://user?id={user_id})"  
    
    return mention

# Inline query handler
@app.on_inline_query()
async def handle_inline_query(client, inline_query: InlineQuery):
    query = inline_query.query.strip()
    user_id = inline_query.from_user.id
    user_name = inline_query.from_user.first_name
    
    # Extract mention using the function
    mention = extract_mention(query, user_id, user_name)
    
    # User who invoked the query
    print(f"Received inline query: '{query}' with mention '{mention}'")

    # Check if the query is in the form of @botusername <someone name>
    if query.startswith("@") and " " in query:
        parts = query.split(" ", 1)
        query_name = parts[1].strip()  # The name after @botusername
    else:
        query_name = query  # Fallback to the original query if no name is given

    # Debugging the received query
    print(f"Received inline query: '{query}' with name '{query_name}'")

    # Whisper functionality
    if query.startswith("@") or query.isdigit():
        user, message = parse_user_message(query)
        if len(message) > 200:
            await inline_query.answer([], cache_time=1, is_personal=True)
            return

        user_type = "username" if user.startswith("@") else "id"

        # Fetch chat details for IDs
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

        # Add whisper to the database
        Whispers.add_whisper(whisper_id, whisper_data)

        # Create Whisper Inline Result
        answers = [
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
            )
        ]
        await client.answer_inline_query(inline_query.id, answers, cache_time=1, is_personal=True)
    else:
        # Random Inline Responses with Horny Level and Cuteness Level
        results = generate_random_responses(mention, user_name, query_name)  # Use query_name for responses
        if not results:
            await inline_query.answer([], cache_time=1, is_personal=True)
            return
        await inline_query.answer(results, cache_time=1, is_personal=True)

# Generate random inline responses including Cuteness Level
def generate_random_responses(mention, user_name, query_name):
    mm = random.randint(1, 100)
    cm = random.randint(5, 30)
    name_start = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    random_responses = [
        {
            "title": "Horny Level",
            "description": "Check how horny you are!",
            "text": f"🔥 {mention} is {mm}% horny!",
        },
        {
            "title": "Cuteness Level",
            "description": "Check how cute you are!",
            "text": f"🌸 {mention} is {mm}% cute!",
        },
        {
            "title": "Gayness Level",
            "description": "Check how gay you are!",
            "text": f"🍷 {mention} is {mm}% gay!",
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
            title=response["title"],
            description=response["description"],
            input_message_content=InputTextMessageContent(
                response["text"], disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(BUTTON),
            thumb_url=THUMB_URL,
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
