import requests
from pyrogram import filters
from Merisa import QuantamBot
from textblob import TextBlob
@QuantamBot.on_message(filters.command("spellcheck"))
async def spellcheck(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**Example:**\n\n`/spellcheck authentcation`")
    m = message.text.split(' ',1)[1]
    try:
        blob=TextBlob(m)
        await message.reply_text(f"`{blob.correct()}`", quote=True)       
    except Exception as e:
        await message.reply_text(f"Error {e}")
