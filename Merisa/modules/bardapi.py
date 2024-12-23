# bard
# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters
import asyncio, random, requests, time
from pyrogram.enums import ChatAction, ParseMode, ChatType
from pyrogram.types import InputMediaPhoto, InlineKeyboardMarkup
from .. import QuantamBot
from config import *
from MukeshAPI import api
from Merisa.modules.many_extra import question
from Merisa.utils.button_help import *
from Merisa.database import is_served_user
@QuantamBot.on_edited_message(
    filters.command(
        ["bard", "gemini"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]
    )
)
@QuantamBot.on_message(
    filters.command(
        ["bard", "gemini"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]
    )
)
async def gemini_reply(b, message):
    await  b.send_chat_action(message.chat.id,ChatAction.TYPING)
    
    text=await question(message)
    search_result = api.gemini(text)["results"]
    await message.reply_text(search_result,reply_markup=InlineKeyboardMarkup(IMGX),parse_mode=ParseMode.MARKDOWN,quote=True,disable_web_page_preview =True)
