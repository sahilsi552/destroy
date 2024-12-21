"""MIT License

Copyright (c) 2023-24 Noob-QuantamBot

          GITHUB: NOOB-MUKESH
          TELEGRAM: @MR_SUKKUN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.enums import ChatAction

from .. import QuantamBot
import requests
from telegraph import Telegraph


from Merisa.utils.button_help import *
from Merisa.modules.telegrph_ import graph_img

@QuantamBot.on_message(filters.command("qrcode"))
async def qrcode_(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "`Please wait...,\n\nCreating your Qrcode ...`")
    write = requests.get(f"https://mukesh-api.vercel.app/qrcode/{text}").json()["results"]

    caption = f"""
sᴜᴄᴇssғᴜʟʟʏ Gᴇɴᴇʀᴀᴛᴇᴅ Qʀᴄᴏᴅᴇ 💘
✨ **Gᴇɴᴇʀᴀᴛᴇᴅ ʙʏ :** {QuantamBot.mention}
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption)
# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh

telegraph = Telegraph(domain="graph.org")
@QuantamBot.on_edited_message(
    filters.command(
        ["scan"],
        prefixes=[ "+", ".", "/", "-", "?", "$", "#", "&"],
    )
)
@QuantamBot.on_message(
    filters.command(
        ["scan"], prefixes=["+", ".", "/", "-", "?", "$", "#", "&"]
    )
)
            
async def scanning(bot, message):
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if message.reply_to_message:
            m = await message.reply_text(
            f"{message.from_user.first_name} Pʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ Qᴜᴇʀʏ.....")
          
            if message.reply_to_message.photo:
                img = await message.reply_to_message.download()
                
                h = graph_img(img)
                url =f"http://api.qrserver.com/v1/read-qr-code/?fileurl=https://graph.org/{h}"
                response = requests.get(url).json()
                text= response[0]["symbol"][0]["data"]
            else:
                return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ǫʀᴄᴏᴅᴇ")
            await m.delete()
            await message.reply_text(f"`{text}`",quote=True)
    except Exception as e:
        return await message.reply(e)
              
