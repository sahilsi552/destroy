# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters

from .. import QuantamBot
from Merisa.database import is_served_user
from Merisa.utils.button_help import *
from pyrogram.enums import ParseMode,ChatType,ChatAction
from pyrogram.types import InlineKeyboardButton,Message,InlineKeyboardMarkup,CallbackQuery
from pyrogram.enums import ChatMemberStatus as CMS
from pymongo import MongoClient
from config import MONGO_DATABASE_URI
import random,requests
from MukeshAPI import api
client = MongoClient(MONGO_DATABASE_URI)
db = client.chatbot
users_collection = db['users']

@QuantamBot.on_message(filters.command("chatbot"))
async def CHAT_BOT(_,m):

    msg = "• ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ"
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data="add_chat"),
                InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data="rm_chat"),
            ],
        ]
    )
    await m.reply_text(
        text=msg,
        reply_markup=keyboard
    )


@QuantamBot.on_callback_query(filters.regex("chat$"))
async def button_click_handler(client, callback_query):
    user_id = callback_query.from_user.id
    data = callback_query.data
    chat_id = callback_query.message.chat.id
    

    if callback_query.message.chat.type == ChatType.PRIVATE:

        if data == 'add_chat':
            existing_user= users_collection.find_one({"user_id": user_id})

            if existing_user:
                await callback_query.answer("chatbot already enabled", show_alert=True)
            else:
                users_collection.insert_one({"user_id": user_id})
                await callback_query.answer("chatbot enable", show_alert=True)

        elif data == 'rm_chat':
            users_collection.delete_one({"user_id": user_id})
            await callback_query.answer("chatbot disable", show_alert=True)
        await callback_query.message.delete()

    else:
        user_id = callback_query.from_user.id
        user_status = (await callback_query.message.chat.get_member(user_id)).status
        if user_status not in [CMS.OWNER, CMS.ADMINISTRATOR]:
            await callback_query.answer(
                "ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴇᴠᴇɴ ᴀɴ ᴀᴅᴍɪɴ, ᴅᴏɴ'ᴛ ᴛʀʏ ᴛʜɪs ᴇxᴘʟᴏsɪᴠᴇ sʜɪᴛ!",
                    show_alert=True,
                )
            return
        
        if data == 'add_chat':
            
            existing_group = users_collection.find_one({"chat_id": chat_id})

            if existing_group:
                await callback_query.answer("chatbot already enabled", show_alert=True)
            else:
                users_collection.insert_one({"chat_id": chat_id})
                await callback_query.answer("chatbot enable ", show_alert=True)
        elif data == 'rm_chat':
            users_collection.delete_one({"chat_id": chat_id})
            await callback_query.answer("chatbot disable", show_alert=True)
        await callback_query.message.delete()
        
        
@QuantamBot.on_message(filters.text, group=7)
async def bot_Send_msg(_, message):
    reactions = random.choice(['👍', '❤️', '🔥', '🥰', '👏', '😁', '🤔', '😱', '🎉', '🤩', '🙏', '👌', '🕊', '🤡', '🥴', '😍', '🐳', '❤️‍🔥', '🌚', '💯', '🤣', '🤗', '🫡', '✍️', '🤝', '🙈', '😇', '👀', '👨‍💻', '👻', '💋', '💔', '🤨', '😐', '⚡️', '🏆', '😢', '🍾', '🍓', '😈', '😴', '🤓', '🎃', '🎅', '🎄', '☃️', '💅', '🤪', '🆒', '🗿', '💘', '😘', '💊', '🦄', '🙉', '🙊', '😎', '👾', '🤷‍♂️', '🤷', '🤷‍♀️', '😡', '🥱'])
    
    try:
        if (
            message.text.startswith("!")
            or message.text.startswith("/")
            or message.text.startswith("?")
            or message.text.startswith("@")
            or message.text.startswith("#")
        ):
            return
        if message.chat.type==ChatType.SUPERGROUP and message.reply_to_message.from_user.id==QuantamBot.id:
        
            existing_group = users_collection.find_one({"chat_id": message.chat.id})
            
            if existing_group:
                await message.react(reactions,big=True)
                await _.send_chat_action(message.chat.id, ChatAction.TYPING)
                output=requests.get("https://sugoi-api.vercel.app/chat?msg="+message.text).json()["response"]
                
                await message.reply_text(text=output["results"],quote=True)
    except:
        pass
    try:
        if message.chat.type==ChatType.PRIVATE and message.reply_to_message.from_user.id ==QuantamBot.id:
            user_ids =  users_collection.find_one({"user_id": message.from_user.id})
        
            if user_ids and message.text:
                try:
                    await message.react(reactions,big=True)
                except:
                    pass
                await _.send_chat_action(message.chat.id, ChatAction.TYPING)
                output=requests.get("https://sugoi-api.vercel.app/chat?msg="+message.text).json()["response"]
                await message.reply_text(text=output,quote=True)
        
    except:
        pass
