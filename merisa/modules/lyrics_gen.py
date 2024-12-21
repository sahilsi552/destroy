from pyrogram import filters
from Merisa import QuantamBot
import requests as r
from pyrogram.enums import ParseMode

@QuantamBot.on_message(filters.command("lyrics"))
async def lyrics_gen(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**Example:**\n\n`/lyrics  <song name>`")
    m = message.text.split(' ',1)[1]
    try:  
        url = f"https://song.panditsiddharth.repl.co/lyrics?song={m}"
        lyrics=r.get(url).text
 
        await message.reply_text(f"`{lyrics}`")       
    except Exception as e:
        await message.reply_text(f"Error {e}")
