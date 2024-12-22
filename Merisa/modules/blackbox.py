# -----------CREDITS -----------
# telegram : @Mr_Sukkun
# github : noob-mukesh
from pyrogram import filters
import asyncio, time,requests
from pyrogram.types import InlineKeyboardMarkup
from .. import QuantamBot
from pyrogram.enums import ChatAction,ParseMode
from config import *
from ..utils.button_help import *
from Merisa.modules.many_extra import question
from MukeshAPI import api
from Merisa.database import is_served_user
#blackbox
@QuantamBot.on_message(filters.command(["blackbox"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def blackbox_chat(bot, message):
    x=await is_served_user(message.from_user.id)
    if x==False:
        return await message.reply("you are not verifed user start me in pm to verfiy",reply_markup=VERIFY)
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    try:
        a=await question(message)
        black=api.blackbox(a)["results"]
        if len(black)<4000:
            await message.reply_text(f"{black}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{QuantamBot.username} ",parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(IMGX),quote=True)  
        else:
            with open("blackbox.txt","r+") as e:
                e.write(black)
                await message.reply_document("blackbox.txt",caption=f"ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{QuantamBot.username}",reply_markup=InlineKeyboardMarkup(IMGX),quote=True) 
    except Exception as e:
        await bot.send_message(OWNER_ID,f"Error Occured\n{e}")
        
        
@QuantamBot.on_message(filters.command("datagpt"))
async def datagpt_api(b, message):
    await b.send_chat_action(message.chat.id, ChatAction.TYPING)
    try:
        text=await question(message)
        search_result = api.datagpt(text)["results"]
        
        await message.reply_text(f"{search_result}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{QuantamBot.username} ",parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(IMGX),quote=True)
    except Exception as e:
        await b.send_message(OWNER_ID,f"Error Occured\n{e}")  

@QuantamBot.on_edited_message(filters.command(["bard", "gemini"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"] ))
@QuantamBot.on_message(filters.command(["bard", "gemini"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]))
async def gemini_reply(b, message):
    await  b.send_chat_action(message.chat.id,ChatAction.TYPING)
    try:
        text=await question(message)
        search_result = api.gemini(text)["results"]
        await message.reply_text(f"{search_result}",reply_markup=InlineKeyboardMarkup(IMGX),parse_mode=ParseMode.MARKDOWN,quote=True)
    except Exception as e:
        await b.send_message(OWNER_ID,f"Error Occured\n{e}")
