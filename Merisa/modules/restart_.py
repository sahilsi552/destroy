
import os
import asyncio
from config import OWNER_ID 
from pyrogram import filters
from .. import QuantamBot

@QuantamBot.on_message(filters.command(["reboot", "update"]) &filters.user(OWNER_ID))
async def update_bot(_, m):
    rr = await m.reply_text("__ʀᴇsᴛᴀʀᴛɪɴɢ__")
    await rr.edit("__sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ ᴡᴀɪᴛ ᴀ ᴡʜɪʟᴇ..__")
    os.system("pip3 install -r requirements.txt")
    os.system(f"kill -9 {os.getpid()} && python3 -m Merisa")
