
import io, os, random,requests
from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters,Client
from pyrogram.enums import ChatAction


LOGO_LINKS = [
    "https://graph.org//file/85b028860a806850691fe.jpg",
    "https://graph.org//file/ea05097695dc1986e93b2.jpg",
    "https://graph.org//file/ffc0129562d2d0f020ea6.jpg",
    "https://graph.org//file/80973e756ba2a8ee92a63.jpg",
    "https://graph.org//file/6d9c7033e6c81dfdaf727.jpg"
]
@Client.on_message(filters.command("logo",".")& filters.me)
async def LOGO_(b, m):
    if len(m.command) < 2:
        return await m.reply_text(
            "ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟᴏɢᴏ ʙᴀʙᴇ​ !`\nExample `/logo mukesh`")
    
    text=m.text.split(None,1)[1]
    
    pesan = await m.reply("**ᴄʀᴇᴀᴛɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ ʟᴏɢᴏ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ᴀ sᴇᴄ​...**")
    try:
    
        randc = random.choice(LOGO_LINKS)
        img = Image.open(io.BytesIO(requests.get(randc).content))
        draw = ImageDraw.Draw(img)
        image_widthz, image_heightz = img.size
        fnt = "Merisa/utils/font.otf"
        font = ImageFont.truetype(fnt, 120)
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
            caption=f"""
☘️ ʟᴏɢᴏ ᴄʀᴇᴀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ☘️
"""
)
        await pesan.delete()
        if os.path.exists(fname):
            os.remove(fname)
    except Exception as e:
        await m.reply(f"ғʟᴏᴏᴅ ᴡᴀɪᴛ ᴇʀʀᴏʀ, ʀᴇᴩᴏʀᴛ ᴛʜɪs  \n #Error {e}")

