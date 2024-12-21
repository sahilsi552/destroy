from pyrogram.enums import ChatAction, ParseMode
import asyncio,requests
import random
from pyrogram.types import InputMediaPhoto, CallbackQuery
from .. import  QuantamBot
from ..utils.button_help import M
from pyrogram import filters, Client
from io import BytesIO
from base64 import b64decode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import urllib.request
import json
@QuantamBot.on_message(filters.command("advice"))
async def advice(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        response= requests.get("https://api.safone.dev/advice").json()["advice"]
        await message.reply(f"{response} {message.from_user.mention}" )
    except Exception as e:
        return await message.reply("#Error {e}")
@QuantamBot.on_message(filters.command("bully"))
async def bully(bot,message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        response= requests.get("https://api.safone.dev/bully").json()["bully"]
        await message.reply(f"{response} {message.from_user.mention}" ) 
    except Exception as e:
        return await message.reply("#Error {e}")
@QuantamBot.on_message(filters.command("fact"))
async def fact(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        response= requests.get("https://api.safone.dev/fact").json()["fact"]
        await message.reply(f"{response} {message.from_user.mention}" )
    except Exception as e:
        return await message.reply("#Error {e}")
     
@QuantamBot.on_message(filters.command("meme"))
async def meme(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response= requests.get(f"https://api.safone.dev/meme?page={random.randint(1,200)}").json()["image"]
        photo=BytesIO(b64decode(response.encode("utf-8")))
        await message.reply_photo(photo,reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Rᴇғʀᴇsʜ", callback_data="meme")
                                
                            ]
                        ]
                    ))
    except Exception as e:
        return await message.reply(f"#Error {e}")

@QuantamBot.on_callback_query(filters.regex("^meme"))
async def callback_handler(_: Client, query: CallbackQuery):
    if query.data == "meme":
        #await query.answer("deleted")
        response= requests.get(f"https://api.safone.dev/meme?page={random.randint(1,200)}").json()["image"]
        photo=BytesIO(b64decode(response.encode("utf-8")))
        await query.edit_message_media(media=InputMediaPhoto(photo),
                reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Rᴇғʀᴇsʜ", callback_data="meme")
                                
                            ]
                        ]
                    ))
        
@QuantamBot.on_message(filters.command("mahadev"))
async def meme(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        url=f"https://mukesh-api.vercel.app/mahadev"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            out = json.loads(data)
            photo=out["results"]
            await message.reply_photo(photo,reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Rᴇғʀᴇsʜ", callback_data="mahadev")
                                
                            ]
                        ]
                    ))
    except Exception as e:
        return await message.reply(f"#Error {e}")

@QuantamBot.on_callback_query(filters.regex("^mahadev"))
async def callback_handler(_: Client, query: CallbackQuery):
    if query.data == "mahadev":
        #await query.answer("deleted")
        url=f"https://mukesh-api.vercel.app/mahadev"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            out = json.loads(data)
            photo=out["results"]
            await query.edit_message_media(media=InputMediaPhoto(photo),
                reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Rᴇғʀᴇsʜ", callback_data="mahadev")
                                
                            ]
                        ]
                    ))    
# ___help__="""
# ᴍᴀᴋᴇ ʏᴏᴜʀ ᴄʜᴀᴛꜱ ꜰᴜɴɴʏ ᴡɪᴛʜ ʟᴏᴛ'ꜱ ꜰᴜɴ ᴍᴏᴅᴜʟᴇ!

# ᴜꜱᴀɢᴇ:
# ❍ /joke - Tell you a jokes.
# ❍ /fact - Know unknown facts.
# ❍ /dare - Play truth or dare.
# ❍ /truth - Play truth or dare.
# ❍ /bully - Insult someone in chat.
# ❍ /meme - Awesome memes everytime.
# ❍ /quotes - Awesome quotes everytime.
# ❍ /couple - Choose couple group of the day.
# ❍ /quote - ᴡʀɪᴛᴇ ǫᴜᴏᴛᴇs
# ❍ /animequotes  - ᴡʀɪᴛᴇ ᴀɴɪᴍᴇǫᴜᴏᴛᴇs
# ❍ /runs *:* ʀᴇᴘʟʏ ᴀ ʀᴀɴᴅᴏᴍ sᴛʀɪɴɢ ғʀᴏᴍ ᴀɴ ᴀʀʀᴀʏ ᴏғ ʀᴇᴘʟɪᴇs
# ❍ /slap *:* sʟᴀᴘ ᴀ ᴜsᴇʀ, ᴏʀ ɢᴇᴛ sʟᴀᴘᴘᴇᴅ ɪғ ɴᴏᴛ ᴀ ʀᴇᴘʟʏ
# ❍ /shrug *:* ɢᴇᴛ sʜʀᴜɢ xᴅ
# ❍ /table *:* ɢᴇᴛ ғʟɪᴘ/ᴜɴғʟɪᴘ :ᴠ
# ❍ /decide *:* ʀᴀɴᴅᴏᴍʟʏ ᴀɴsᴡᴇʀs ʏᴇs/ɴᴏ/ᴍᴀʏʙᴇ
# ❍ /toss *:* ᴛᴏssᴇs ᴀ ᴄᴏɪɴ
# ❍ /bluetext *:* ᴄʜᴇᴄᴋ ᴜʀsᴇʟғ :ᴠ
# ❍ /roll *:* ʀᴏʟʟ ᴀ ᴅɪᴄᴇ
# ❍ /rlg *:* ᴊᴏɪɴ ᴇᴀʀs,ɴᴏsᴇ,ᴍᴏᴜᴛʜ ᴀɴᴅ ᴄʀᴇᴀᴛᴇ ᴀɴ ᴇᴍᴏ ;-;
# ❍ /shout  <ᴋᴇʏᴡᴏʀᴅ>*:* ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢɪᴠᴇ ʟᴏᴜᴅ sʜᴏᴜᴛ
# ❍ /weebify  <ᴛᴇxᴛ>*:* ʀᴇᴛᴜʀɴs ᴀ ᴡᴇᴇʙɪғɪᴇᴅ ᴛᴇxᴛ
# ❍ /sanitize *:* ᴀʟᴡᴀʏs ᴜsᴇ ᴛʜɪs ʙᴇғᴏʀᴇ /ᴘᴀᴛ ᴏʀ ᴀɴʏ ᴄᴏɴᴛᴀᴄᴛ
# ❍ /pat *:* ᴘᴀᴛs ᴀ ᴜsᴇʀ, ᴏʀ ɢᴇᴛ ᴘᴀᴛᴛᴇᴅ
# ❍ /8ball *:* ᴘʀᴇᴅɪᴄᴛs ᴜsɪɴɢ 8ʙᴀʟʟ ᴍᴇᴛʜᴏᴅ """
# __mod_name__=" ꜰᴜɴ "
