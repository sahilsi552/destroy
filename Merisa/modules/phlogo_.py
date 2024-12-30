import asyncio
from Merisa import QuantamBot
from pyrogram import filters
from phlogo import generate
import os
from PIL import Image
from pyrogram.enums import ChatAction

os.system("pip install pillow==9.5.0")


@QuantamBot.on_message(filters.command("phlogo"))
async def phlogo(b, m):
    await b.send_chat_action(m.chat.id, ChatAction.UPLOAD_PHOTO)
    try:
        text = m.text[1:]
        all_text = text.split()
        first_name = all_text[1]
        last_name = all_text[2]
        result = generate(first_name, last_name)
    except IndexError:
        return await m.reply_text("**Example:**\n\n`/phlogo <text> <text2>`")
    try:
        result.save("mukesh.png")
        x = Image.open("mukesh.png")
        x.save("mukesh.png")
        x.close()
        await m.reply_photo("mukesh.png")
        if os.path.exists("mukesh.png"):
            os.remove("mukesh.png")
    except Exception as e:
        return await m.reply(str(e))


@QuantamBot.on_message(filters.command("phst"))
async def phst(b, m):
    await b.send_chat_action(m.chat.id, ChatAction.UPLOAD_PHOTO)
    try:
        text = m.text[1:]
        all_text = text.split()
        first_name = all_text[1]
        last_name = all_text[2]
        result = generate(first_name, last_name)
    except IndexError:
        return await m.reply_text("**Example:**\n\n`/phlogo <text> <text2>`")
    try:
        result.save("mukesh.png")
        x = Image.open("mukesh.png")
        r, b, g = x.split()
        x = Image.merge("RGB", (b, g, r))
        sticker_size = (512, 512)
        x.thumbnail(sticker_size)
        x.save("mukesh.WEBP", "WEBP")
        x.close()
        await m.reply_sticker("mukesh.WEBP")
        if os.path.exists("mukesh.WEBP"):
            os.remove("mukesh.WEBP")
    except Exception as e:
        return await m.reply(str(e))
