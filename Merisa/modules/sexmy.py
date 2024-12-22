import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Merisa import QuantamBot as app
from config import SUPPORT_GRP as SUPPORT_CHAT

BUTTON = [[InlineKeyboardButton("🍒 ꜱᴜᴘᴘᴏʀᴛ 🍒", url=f"https://t.me/{SUPPORT_CHAT}")]]
HOT = "https://telegra.ph/file/daad931db960ea40c0fca.gif"
SMEXY = "https://telegra.ph/file/a23e9fd851fb6bc771686.gif"
LEZBIAN = "https://telegra.ph/file/5609b87f0bd461fc36acb.gif"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANG = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"


@app.on_message(filters.command("horny"))
async def horny(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    HORNY = f"🔥 {mention} ɪꜱ {mm}% ʜᴏʀɴʏ!"
    await message.reply(HORNY, reply_markup=InlineKeyboardMarkup(BUTTON), photo=HOT)

@app.on_message(filters.command("gay"))
async def gay(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    GAY = f"🍷 {mention} ɪꜱ {mm}% ɢᴀʏ!"
    await message.reply(GAY, reply_markup=InlineKeyboardMarkup(BUTTON), photo=SMEXY)

@app.on_message(filters.command("lesbian"))
async def lezbian(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    FEK = f"💜 {mention} ɪꜱ {mm}% ʟᴇᴢʙɪᴀɴ!"
    await message.reply(FEK, reply_markup=InlineKeyboardMarkup(BUTTON), photo=LEZBIAN)

@app.on_message(filters.command("boob"))
async def boob(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    BOOBS = f"🍒 {mention}'ꜱ ʙᴏᴏʙꜱ ꜱɪᴢᴇ ɪᴢ {mm}!"
    await message.reply(BOOBS, reply_markup=InlineKeyboardMarkup(BUTTON), photo=BIGBALL)

@app.on_message(filters.command("cock"))
async def cock(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    COCK = f"🍆 {mention}'ꜱ ᴄᴏᴄᴋ ꜱɪᴢᴇ ɪᴢ {mm}ᴄᴍ"
    await message.reply(COCK, reply_markup=InlineKeyboardMarkup(BUTTON), photo=LANG)

@app.on_message(filters.command("cute"))
async def cute(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    CUTE = f"🍑 {mention} {mm}% ᴄᴜᴛᴇ"
    await message.reply(CUTE, reply_markup=InlineKeyboardMarkup(BUTTON), photo=CUTIE)

__HELP__ = """  
*To check your current state:*  
➻ /horny 🦄 : Check your current horniness level  
➻ /gay 🌈 : Check your current gayness level  
➻ /lesbian 🏳️‍🌈 : Check your current lesbian level  
➻ /boobs 🍈🍈 : Check your current boob size  
➻ /cute 🥰 : Check your current cuteness level  
"""
__MODULE__= "Sᴇᴍxʏ"


