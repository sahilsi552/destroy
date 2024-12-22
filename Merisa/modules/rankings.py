import sys  
import logging  
import random  
import unicodedata  
from typing import Dict, List, Tuple  
from pymongo import MongoClient, ASCENDING, DESCENDING  
from pyrogram import Client, filters  
from pyrogram.types import Message  
from Merisa import QuantamBot as Merisa
from config import MONGO_DATABASE_URI as MONGO_DB_URI  

# 🌟 User-Defined Variables  
IMAGES = ["https://telegra.ph/file/a6a5b78007e4ca766794a.jpg"] * 5  
QUOTES = [  
    "Keep pushing forward!",  
    "You're doing amazing work!",  
    "Stay positive and strong!",  
    "Every step counts!",  
    # Additional quotes omitted for brevity  
]  
MILESTONES = [100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000, 15000]  
BADGE_EMOJIS = {  
    100: "⛏️",  
    500: "💰",  
    1000: "🚀",  
    2000: "✨",  
    3000: "🌟",  
    4000: "🌞",  
    5000: "🌠",  
    7500: "🪐",  
    10000: "🦄",  
    15000: "🌌"  
}  
RANK_EMOJIS = ["🥇", "🥈", "🥉"] + ["🎖️"] * 7  

# 🛡️ Configure Logging  
logging.basicConfig(level=logging.INFO)  
logger = logging.getLogger(__name__)  

# 🔍 MongoDB Initialization  
try:  
    mongo_client = MongoClient(MONGO_DB_URI)  
    db = mongo_client["quantum_engagement"]  
    collections = {  
        "ranking": db["ranking"],  
        "badges": db["badges"],  
        "engagement": db["engagement"]  
    }  
    logger.info("Connected to MongoDB")  
except Exception as e:  
    logger.error(f"Failed to connect to MongoDB: {e}")  
    sys.exit(1)  

# 🎲 Helper Functions  
def get_random_image() -> str:  
    """Get a random motivational image."""  
    return random.choice(IMAGES)  

def get_random_quote() -> str:  
    """Get a random motivational quote."""  
    return random.choice(QUOTES)  

def register_user(chat_id: int, user_id: int, username: str):  
    """Register a user in the ranking system for a specific chat group."""  
    collections["ranking"].update_one(  
        {"user_id": user_id, "chat_id": chat_id},  
        {  
            "$setOnInsert": {  
                "total_messages": 0,  
                "username": username  
            }  
        },  
        upsert=True  
    )  

def update_message_count(chat_tracker: Dict[int, Dict[int, int]], chat_id: int, user_id: int):  
    """Update the message count for a user within a specific chat."""  
    if chat_id not in chat_tracker:  
        chat_tracker[chat_id] = {}  
    chat_tracker[chat_id].setdefault(user_id, 0)  
    chat_tracker[chat_id][user_id] += 1  

def award_badge(user_id: int, chat_id: int, badge: str):  
    """Award a badge to a user for a specific chat."""  
    collections["badges"].update_one(  
        {"user_id": user_id, "chat_id": chat_id},  
        {"$addToSet": {"badges": badge}},  
        upsert=True  
    )  

def get_user_badges(user_id: int, chat_id: int) -> str:  
    """Retrieve a user's badges as a string of emoji for a specific chat."""  
    user_badges = collections["badges"].find_one({"user_id": user_id, "chat_id": chat_id}, {"badges": 1})  
    if user_badges and "badges" in user_badges:  
        badges = user_badges["badges"]  
        return ' '.join(BADGE_EMOJIS.get(badge, "") for badge in badges)  
    return ""  

def check_and_award_milestones(user_id: int, chat_id: int, message_count: int) -> bool:  
    """Check if a user has reached a milestone and award a badge if so."""  
    awarded = False  
    for milestone in MILESTONES:  
        if message_count == milestone:  
            award_badge(user_id, chat_id, f"{milestone} Messages")  
            awarded = True  
    return awarded  

# 🚀 Event Handlers and Bot Commands  
@Merisa.on_message(filters.group, group=6)  
def track_messages(client, message: Message):  
    if not message.from_user:  
        return  

    user_id = message.from_user.id  
    username = message.from_user.first_name  
    chat_id = message.chat.id  

    register_user(chat_id, user_id, username)  
    update_message_count(user_data, chat_id, user_id)  

    total_messages = user_data.setdefault(chat_id, {}).setdefault(user_id, 0) + 1  
    user_data[chat_id][user_id] = total_messages  

    if check_and_award_milestones(user_id, chat_id, total_messages):  
        message.reply_text(f"🎉 Congratulations {username}, you've reached a milestone!")  

    collections["ranking"].update_one(  
        {"user_id": user_id, "chat_id": chat_id},  
        {"$inc": {"total_messages": 1}},  
        upsert=True  
    )  

@Merisa.on_message(filters.command(["daily"]))  
async def daily_challenge(_, message: Message):  
    user_id = message.from_user.id  
    chat_id = message.chat.id  
    daily_challenge = collections["engagement"].find_one({"user_id": user_id, "chat_id": chat_id}, {"daily_challenge": 1})  

    if daily_challenge and daily_challenge.get("daily_challenge", {}).get("completed", False):  
        await message.reply_text("You've already completed today's challenge!")  
    else:  
        challenge_text = get_random_quote()  
        await message.reply_text(f"🌟 Daily Challenge: {challenge_text}")  

        collections["engagement"].update_one(  
            {"user_id": user_id, "chat_id": chat_id},  
            {"$set": {"daily_challenge": {"completed": True}}},  
            upsert=True  
        )  

async def handle_leaderboard_command(chat_id: int, data: Dict[int, Dict[int, int]], duration: str, message: Message) -> None:  
    title = f"{duration} Leaderboard"  

    if chat_id not in data:  
        await message.reply_text(f"❅ No data available for {title}.")  
        return  

    users_data = [(user_id, count) for user_id, count in data[chat_id].items()]  
    sorted_users_data = sorted(users_data, key=lambda x: x[1], reverse=True)[:10]  
    total_messages_count = sum(count for count in data[chat_id].values())  

    if sorted_users_data:  
        response = await create_leaderboard_response(chat_id, title, sorted_users_data, total_messages_count)  
        await send_long_message(message, response)  
    else:  
        await message.reply_text(f"❅ No data available for {title}.")  

@Merisa.on_message(filters.command(["today"]))  
async def today_(_, message: Message):  
    await handle_leaderboard_command(message.chat.id, user_data, "Today's", message)  

@Merisa.on_message(filters.command(["weekly"]))  
async def weekly_(_, message: Message):  
    await handle_leaderboard_command(message.chat.id, user_data, "This Week's", message)  

@Merisa.on_message(filters.command(["monthly"]))  
async def monthly_(_, message: Message):  
    await handle_leaderboard_command(message.chat.id, user_data, "This Month's", message)  

@Merisa.on_message(filters.command(["ranking", "overall"]))  
async def ranking(_, message: Message):  
    chat_id = message.chat.id  
    try:  
        top_members = collections["ranking"].find({"chat_id": chat_id}).sort("total_messages", DESCENDING).limit(10)  
        users_data = [(member["user_id"], member["total_messages"]) for member in top_members]  
        total_messages_count = sum(member["total_messages"] for member in top_members)  
        response = await create_leaderboard_response(chat_id, "Overall Leaderboard", users_data, total_messages_count)  
        await send_long_message(message, response)  
    except Exception as e:  
        logger.error(f"Error fetching overall rankings for chat_id {chat_id}: {e}")  
        await message.reply_text("❅ Failed to fetch overall rankings. Please try again later.")  

async def send_long_message(message: Message, text: str, chunk_size: int = 4096):  
    for i in range(0, len(text), chunk_size):  
        await message.reply_text(text[i:i+chunk_size])  

async def create_leaderboard_response(chat_id: int, title: str, users_data: List[Tuple[int, int]], total_messages_count: int) -> str:  
    table_widths = [4, 20, 8, 10]  
    response = (  
        f"📊 **{title}**\n\n"  
        f"📈 **Total Messages:** {total_messages_count}\n\n"  
        "```\n"  
        f"{'#':<{table_widths[0]}} {'👤 Name':<{table_widths[1]}} {'✉️ Msgs':<{table_widths[2]}} {'🏆 Badges':<{table_widths[3]}}\n"  
    )  

    def sanitize_name(name):  
        sanitized = unicodedata.normalize('NFKD', name)  
        return ''.join(c for c in sanitized if c.isprintable())  

    for idx, (user_id, total_messages) in enumerate(users_data, start=1):  
        try:  
            user_info = await Merisa.get_users(user_id)  
            user_name = sanitize_name(user_info.first_name or "Unknown")  
        except Exception as e:  
            user_cached = collections["ranking"].find_one({"user_id": user_id, "chat_id": chat_id})  
            user_name = sanitize_name(user_cached.get("username", "Unknown"))  
            logger.error(f"Failed to fetch user info for user_id {user_id}: {e}")  

        if len(user_name) > table_widths[1]:  
            user_name = user_name[:table_widths[1] - 1] + "…"  

        user_name = user_name.ljust(table_widths[1])  
        badges = get_user_badges(user_id, chat_id).ljust(table_widths[3])  
        emoji = RANK_EMOJIS[idx-1] if idx <= len(RANK_EMOJIS) else "⭐"  

        response += (  
            f"{emoji} {idx:<{table_widths[0]-2}} "  
            f"{user_name:<{table_widths[1]}} "  
            f"{total_messages:<{table_widths[2]}} "  
            f"{badges:<{table_widths[3]}}\n"  
        )  

    response += "```"  # Close the monospaced block  
    return response  

@Merisa.on_message(filters.command(["rankingfaq"]))  
async def ranking_faq(client, message: Message):  
    response = (  
        "📘 **Welcome to Baba's Fun Ranking & Engagement System!**\n\n"  
        "Hey! Baba's here to track your vibes and energize our group fun! Climb the ranks and dive into excitement:\n\n"  
        "✨ **Overall Leaderboard**:\n"  
        "   Check out the top chatterboxes with /overall!\n\n"  
        "✨ **Activity Levels**:\n"  
        "   Compare daily, weekly, or monthly activity with /recent!\n\n"  
        "✨ **Message Milestones**:\n"  
        "   Hit new chat heights for cool badges! 🌟\n\n"  
        "✨ **Daily Challenges**:\n"  
        "   Dive into daily thrills with /daily for fun and rewards!\n\n"  
        "Keep it active, keep the energy up, and have a blast! 🎉🚀"  
    )  
    await message.reply_text(response)  

__MODULE__ = "Rᴀɴᴋɪɴɢs"  

__HELP__ = """  
๏ /overall *➥* Feeler lucky? Check the top discussers on the overall leaderboard!   

๏ /recent *➥* Discover activity: today, this week, or this month.  

๏ /ranking *➥* Check your user ranking score.  

๏ /daily *➥* Attempt today's challenge!  
"""  

user_data: Dict[int, Dict[int, int]] = {}
