from telegraph import Telegraph
# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from PIL import Image
from pyrogram import filters
import asyncio
from .. import QuantamBot
from Merisa.utils.button_help import *
from pyrogram.types import InlineKeyboardButton as ikb, InlineKeyboardMarkup as ikm

def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


telegraph = Telegraph(domain="graph.org")
telegraph.create_account(QuantamBot.username)
def graph_text(title,text):
    z=telegraph.create_page(title=title,html_content=text.html.replace("\n", "<br>"))
    return z["url"]
def graph_img(img):
    try:
        z=telegraph.upload_file(img)
        return z[0]["src"]
    except Exception as e:
        print(e)
@QuantamBot.on_message(filters.command(["tgt", f"tgt@{QuantamBot.username}"]))
async def telegraph_text(_, m):
    
    if m.reply_to_message:
        text=m.reply_to_message.text
    elif not m.reply_to_message:
        text = m.text.split(None, 1)[1]
    x=await m.reply("wait a moment")

    h=graph_text(m.from_user.first_name,text)
    
    url=[
        [ikb("ᴠɪᴇᴡ ᴛᴇʟᴇɢʀᴀᴘʜ",url=h)]
        ]
    await m.reply("Uᴘʟᴏᴀᴅᴇᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ",disable_web_page_preview=True,reply_markup=ikm(url))
    
@QuantamBot.on_message(filters.command(["tgm", f"tgm@{QuantamBot.username}"]))
async def telegraph_img(b, m):
    

    try:
        
        if m.reply_to_message and m.reply_to_message.media:
            x=await m.reply("wait a moment")
            img=await m.reply_to_message.download()
            if img.endswith((".webp")):
                resize_image(img)
            h=graph_img(img)
            url=[
        [ikb("ᴠɪᴇᴡ ᴛᴇʟᴇɢʀᴀᴘʜ",url=f"https://graph.org/{h}")]
        ]
            await x.delete()
            await m.reply(f"Uᴘʟᴏᴀᴅᴇᴅ ᴛᴏ [ᴛᴇʟᴇɢʀᴀᴘʜ](https://graph.org/{h})",disable_web_page_preview=False,reply_markup=ikm(url))
    except Exception as e:
        await m.reply(e,quote=True)

    

