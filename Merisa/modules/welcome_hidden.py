import shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import numpy as np
from unidecode import unidecode
import asyncio, os, random, glob
from pyrogram import filters
from pyrogram.types import *
from pyrogram.enums import ParseMode,ChatMemberStatus
from .. import QuantamBot
from Merisa.utils.button_help import ADD_ME
from pytz import timezone 
from datetime import datetime
from urllib.request import urlopen
from Merisa.database.welcome_db import get_welcome_status,set_welcome_status
img_list = [
    "https://graph.org//file/097531769fdd405480e59.jpg",
    "https://graph.org//file/fb12eda9238d49f937eff.jpg",
    "https://graph.org//file/3722679374ed1b56c03e2.jpg",
    "https://graph.org//file/725b0376a8b2f96bc3237.jpg",
    "https://graph.org//file/483972408aa4822b37bfa.jpg",
    "https://graph.org//file/74a85d290f10da5b8e2de.jpg",
    "https://graph.org//file/3948c242bc59f7df58b8b.jpg",
    "https://graph.org//file/3a760fb253b2b3f092e48.jpg",
    "https://graph.org//file/bf3d1c9f56bafbadd7892.jpg",
    "https://graph.org//file/cc4a21ee29bc3689533ac.jpg",
    "https://graph.org//file/28e9b5fb7891a57b8a6a7.jpg",
    "https://graph.org//file/a59daca7c97557f5a2744.jpg",
    "https://graph.org//file/b02b5b696d0dd0f12625f.jpg",
    "https://graph.org//file/b4397d6d5132e15c6c8f0.jpg",
    "https://graph.org//file/4e6eecf4d7f9b39b37997.jpg",
    "https://graph.org//file/c6ea86d02a9ce2dcd6c73.jpg",
    "https://graph.org//file/5d351e89a96408fccd513.jpg",
    "https://graph.org//file/f47d74f996e80983b0252.jpg",
    "https://graph.org//file/1cda6f33211f58057b31f.jpg",
    "https://graph.org//file/f273fe66b8bd930ec5925.jpg",
    "https://graph.org//file/d562e3c85253d8643007a.jpg",
    "https://graph.org//file/491ed50c9af282744aa22.jpg",
    "https://graph.org//file/5a79c463b752ebaf6add3.jpg",
    "https://graph.org//file/3a760fb253b2b3f092e48.jpg",
    "https://graph.org//file/3a760fb253b2b3f092e48.jpg",
    "https://graph.org//file/fe89680d64f0b6a1d5b81.jpg",
    "https://graph.org//file/b5e09ff29506a173c1a84.jpg",
    "https://graph.org//file/42f3996bbc35388e4a78e.jpg",
    "https://graph.org//file/c33cef0464c02c687af59.jpg",
    "https://graph.org//file/e82097db14111d55a43e2.jpg"
]
def thumbnail(chatimg, userimg, background, welcomemsg, userinfo):
    try:

        def create_thumbnail(userimg):
            
            x = Image.open(userimg)
            x.thumbnail((300, 300))
            x.save("thumbnail.jpg")
            thumb = Image.open("thumbnail.jpg")
            constrast = ImageEnhance.Contrast(thumb)
            thumb = constrast.enhance(1.5)
            draw = ImageDraw.Draw(thumb)
            height, width = thumb.size
            lum_img = Image.new("L", thumb.size, 0)
            draw = ImageDraw.Draw(lum_img)
            draw.pieslice([(0, 0), (height, width)], 0, 360, fill=255, outline="white")

            img_arr = np.array(thumb)
            lum_img_arr = np.array(lum_img)

            final_img_arr = np.dstack((img_arr, lum_img_arr))
            thumbn = Image.fromarray(final_img_arr)

            return thumbn

        x = create_thumbnail(chatimg)
        y = create_thumbnail(userimg)
        bg = Image.open(background)
        bg = bg.filter(ImageFilter.BoxBlur(8))
        combine = bg.copy()
        combine.paste(x, (80, 132), mask=x)
        combine.paste(y, (870, 132), mask=y)
        combine.save("ok.png")

        def add_text_to_image():
            img = Image.open("ok.png")
            d1 = ImageDraw.Draw(img)
            font = "Merisa/utils/BebasNeue.otf"
            my_font = ImageFont.truetype(font, size=60)
            my_font2 = ImageFont.truetype(font, size=40)

            d1.line((300, 570, 1000, 570), fill="white", width=4)
            

            d1.arc((72, 130, 380, 435), start=0, end=360, fill="#0b0d0c", width=11)
            d1.arc((862, 130, 1170, 435), start=0,
                   end=360, fill="#0b0d0c", width=11)
            d1.text((300, 50), welcomemsg, font=my_font, fill=(224, 224, 224),stroke_width=2,stroke_fill="#f50727")

            d1.multiline_text((500, 580), userinfo,
                              font=my_font2, fill=(224, 224, 224),stroke_width=2,stroke_fill="#f50727")

            im1= img.crop((0, 0, 1280, 720))

            im1.save("final.jpg")

        add_text_to_image()

    except Exception as e:
        print(e)


# thumbnail("mukesh.jpg", "mukesh2.jpg", "background2.jpg", welcomemsg=" welcome to the support chat ", userinfo="name:   mukesh \n\n id:   12345678")
@QuantamBot.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):
    user_id = message.from_user.id
    usage = "**ᴜsᴀɢᴇ:**\n**⦿ /welcome [on|off]**"
    if len(message.command) == 1:
        return await message.reply_text(usage)

    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
        state = message.text.split(None, 1)[1].strip().lower()
        current_status = await get_welcome_status(chat_id)

        if state == "off":
            if current_status == "off":
                await message.reply_text("** ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ!**")
            else:
                await set_welcome_status(chat_id, "off")
                await message.reply_text(f"**ᴅɪsᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ** {message.chat.title} **ʙʏ ʙᴏᴛ**")
        elif state == "on":
            if current_status == "on":
                await message.reply_text("**ᴇɴᴀʙʟᴇᴅ ʙᴏᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ!**")
            else:
                await set_welcome_status(chat_id, "on")
                await message.reply_text(f"**ᴇɴᴀʙʟᴇᴅ ʙᴏᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ** {message.chat.title}")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("**sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ʙᴏᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!**")


@QuantamBot.on_chat_member_updated(filters.group)

async def member_has_joined(c: QuantamBot, member: ChatMemberUpdated):
    chat_id = member.chat.id

    welcome_status = await get_welcome_status(chat_id)
    if welcome_status == "off":
        return
    
    back_img = urlopen(random.choice(img_list))
    if (
        member.new_chat_member
        and not member.old_chat_member
        and not member.new_chat_member.user.is_bot == "true"
        and member.new_chat_member.user.status
        not in [
            ChatMemberStatus.BANNED,
            ChatMemberStatus.RESTRICTED,
            ChatMemberStatus.LEFT
        ]
    ):
        user = member.new_chat_member.user if member.new_chat_member else member.from_user
        user_photo = user.photo.big_file_id if user.photo else None
        chat_photo = member.chat.photo.big_file_id if member.chat.photo else None
        chat_title = unidecode(member.chat.title)
        username = "@" + user.username if user.username else None
        fullname = user.first_name + user.last_name if user.last_name else user.first_name
        name = unidecode(f"{fullname}")
        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
    
        if not(user_photo or chat_photo):
            return await c.send_message(
                member.chat.id,f"""<b><u>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {member.chat.title} </u>
    ɴᴀᴍᴇ : {fullname[:45]}
    ᴜꜱᴇʀ ɪᴅ : <code>{user.id}</code>
    ᴜꜱᴇʀɴᴀᴍᴇ :<code> {username}</code>
    ᴍᴇɴᴛɪᴏɴ : {user.mention("ʟɪɴᴋ")}
    ᴊᴏɪɴᴇᴅ ᴀᴛ: {ind_time} </b>""",parse_mode=ParseMode.HTML,reply_markup=InlineKeyboardMarkup(ADD_ME)
        )
        chatphoto = await c.download_media(member.chat.photo.big_file_id)
        info = f" Name  :  {name}\n\nUser id  : {user.id}"
        if not user_photo:
            thumbnail(
                chatphoto,
                urlopen("https://te.legra.ph/file/f72a978a5c26bf59fadf8.jpg"),
                back_img,
                welcomemsg=f"welcome to {chat_title}",
                userinfo=info,
            )
    
            return await c.send_photo(
                member.chat.id,
                photo="final.jpg",
            caption=f"""<b><u>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {member.chat.title} </u>
    ɴᴀᴍᴇ : {fullname[:45]}
    ᴜꜱᴇʀ ɪᴅ : <code>{user.id}</code>
    ᴜꜱᴇʀɴᴀᴍᴇ :<code> {username}</code>
    ᴍᴇɴᴛɪᴏɴ : {user.mention("ʟɪɴᴋ")}
    ᴊᴏɪɴᴇᴅ ᴀᴛ: {ind_time}</b>""",parse_mode=ParseMode.HTML,reply_markup=InlineKeyboardMarkup(ADD_ME)
        )
    
        userphoto = await c.download_media(user.photo.big_file_id)
    
        thumbnail(
            chatphoto,
            userphoto,
            back_img,
            welcomemsg=f"welcome to {chat_title}",
            userinfo=info,
        )
    
        await c.send_photo(
            member.chat.id,
            photo="final.jpg",
            caption=f"""<b><u>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {member.chat.title} </u>
    ɴᴀᴍᴇ : {fullname[:45]}
    ᴜꜱᴇʀ ɪᴅ : <code>{user.id}</code>
    ᴜꜱᴇʀɴᴀᴍᴇ :<code> {username}</code>
    ᴍᴇɴᴛɪᴏɴ : {user.mention("ʟɪɴᴋ")}
    ᴊᴏɪɴᴇᴅ ᴀᴛ: {ind_time} </b>""",parse_mode=ParseMode.HTML,reply_markup=InlineKeyboardMarkup(ADD_ME)
        )
        try:
            os.remove("ok.png")
            os.remove(chatphoto)
            os.remove(userphoto)
            shutil.rmtree("downloads")
            os.remove("final.jpg")
            os.remove("thumbnail.jpg")
    
        except:
            pass
    
            
        else:
            return
        
