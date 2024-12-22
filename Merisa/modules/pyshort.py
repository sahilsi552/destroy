from pyrogram import filters
from Merisa import QuantamBot
from pyrogram.types import InlineKeyboardButton as ikb, InlineKeyboardMarkup as ikm
import pyshorteners,re,requests
shortener = pyshorteners.Shortener()
@QuantamBot.on_message(filters.command("shorturl"))
async def short_url(b,m):
    if len(m.command) < 2:
        return await m.reply_text(
            "**Example:**\n\n`/shorturl [url]`")
    msg=m.text.split(None,1)[1]
    if not msg.startswith("http"):
        return await m.reply_text("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ᴠᴀʟɪᴅ ᴘʀᴏᴠɪᴅᴇ ᴜʀʟ")

    tiny_link = shortener.tinyurl.short(msg)
    url=[
        [ikb("ᴠɪᴇᴡ ʟɪɴᴋ",url=tiny_link)]
        ]
    await m.reply_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ sʜᴏʀᴛᴇɴᴇᴅ ᴜʀʟ:\n `{tiny_link}` ",reply_markup=ikm(url))
@QuantamBot.on_message(filters.command(["unshorturl"]))
async def unshort(_, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "**Example:**\n\n`/unshorturl [shorted url]`")
    link=message.text.split(' ')[1]
    if not link.startswith("http"):
        return await message.reply_text("ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ᴠᴀʟɪᴅ ᴘʀᴏᴠɪᴅᴇ ꜱʜᴏʀᴛᴇᴅ ᴜʀʟ")
    
    try:
        

        x =requests.get(link, allow_redirects=True).url
        url=[ [ikb ("ᴠɪᴇᴡ ʟɪɴᴋ",url=x)] ]
        await message.reply_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴜɴsʜᴏʀᴛᴇɴᴇᴅ ᴜʀʟ:\n`{x}` " ,reply_markup=ikm(url))
    except Exception as e:

        await message.reply_text(f"ᴇʀʀᴏʀ:    {e} ")