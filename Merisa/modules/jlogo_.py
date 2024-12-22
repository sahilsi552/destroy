
import io, os, random
from config import SUPPORT_GRP
from ..utils.button_help import ADD_ME
import requests
from PIL import Image, ImageDraw, ImageFont
from ..  import QuantamBot
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup

import random,io,requests
from pyrogram.enums import ChatAction

LOGO_LINKS = [
    "https://telegra.ph/file/7345fd37e2ed393b37643.jpg",
    "https://telegra.ph/file/5ced2c3542ef0662fd6e2.jpg",
    "https://telegra.ph/file/aafd14122a2db67ebb0b7.jpg",
    "https://telegra.ph/file/b6871572b43784c534e85.jpg",
    "https://telegra.ph/file/286b7d5d0b1ea517118cc.jpg",
    "https://telegra.ph/file/fc0de575d62277a0612ea.jpg",
    "https://telegra.ph/file/d241b20bcf1d71c4190bf.jpg",
    "https://telegra.ph/file/3cf270784feb63bd3afbe.jpg",
    "https://telegra.ph/file/f67e80b654520da632edf.jpg",
    "https://telegra.ph/file/3f480f4d5136fee436501.jpg",
    "https://telegra.ph/file/fc0de575d62277a0612ea.jpg"
    
]


@QuantamBot.on_message(filters.command("jlogo"))
async def JLOGO_(b, m):
    if len(m.command) < 2:
        return await m.reply_text(
            "ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟᴏɢᴏ ʙᴀʙᴇ​ !`\nExample `/jlogo mukesh`")
    
    text=m.text.split(None,1)[1]
    
    pesan = await m.reply("**ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ʟᴏɢᴏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ​...**")
    try:
        await b.send_chat_action(m.chat.id, ChatAction.UPLOAD_PHOTO)
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        fnt = "Merisa/utils/UrbanJungleDEMO.otf"
        font = ImageFont.truetype(fnt, 50)
        bbox= draw.textbbox((0,0),text, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        h += int(h * 0.21)
        draw.text(
            ((image_widthz - w) / 2, (image_heightz - h) / 2),
            text,
            font=font,
            fill=(255, 255, 255),
        )
        x = (image_widthz - w) / 2
        y = (image_heightz - h) / 2 + 6
        draw.text(
            (x, y), text, font=font, fill="white", stroke_width=1, stroke_fill="black"
        )
        fname = "mukesh.png"
        img.save(fname)
        # img.show()
        await m.reply_photo(photo="mukesh.png",
            caption=f"""━━━━━━━{QuantamBot.name}━━━━━━━

☘️ ʟᴏɢᴏ ᴄʀᴇᴀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ☘️
◈──────────────◈
🔥 ᴄʀᴇᴀᴛᴇᴅ ʙʏ : @{QuantamBot.username}
━━━━━━━{QuantamBot.name}━━━━━━━""",reply_markup=InlineKeyboardMarkup(ADD_ME)
)
        await pesan.delete()
        if os.path.exists(fname):
            os.remove(fname)
    except Exception as e:
        await m.reply(f"ғʟᴏᴏᴅ ᴡᴀɪᴛ ᴇʀʀᴏʀ, ʀᴇᴩᴏʀᴛ ᴛʜɪs ᴀᴛ @{SUPPORT_GRP} \n #Error {e}")


