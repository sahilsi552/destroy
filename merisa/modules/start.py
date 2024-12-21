
import asyncio
import config
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.enums import ParseMode
from Merisa import QuantamBot, HELPABLE
from ..utils import  page_load
from Merisa.utils.database import is_on_off
from Merisa.inline import private_panel,private_panel2
from Merisa.database import save_id,chat_id
from pyrogram.enums import ChatType, ParseMode
loop = asyncio.get_running_loop()


@QuantamBot.on_message(filters.command(["start", "help"]) & ~config.BANNED_USERS & ~filters.group & ~filters.forwarded)
async def private_start(app, message: Message):
    user_id = message.from_user.id
    
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            buttons = page_load(0, HELPABLE, "help")
            return await message.reply_photo(
                photo=config.START_IMG,
                caption="ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ @{}\n\n๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`".format(
                    config.SUPPORT_GRP
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        if await is_on_off(2):
            sender_id = message.from_user.id
            sender_name = message.from_user.mention
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>\n\n<b>ᴜsᴇʀ ɪᴅ:</b> {sender_id}\n<b>ᴜsᴇʀɴᴀᴍᴇ:</b> {sender_name}",
            )
    else:
        out = private_panel()
        image = config.START_IMG
        TXT = f"""*ʜᴇʏ* {message.from_user.mention} , 🥀
*๏ ɪ'ᴍ {QuantamBot.mention} ʜᴇʀᴇ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘs!
ʜɪᴛ ʜᴇʟᴘ ᴛᴏ ғɪɴᴅ ᴏᴜᴛ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ɪɴ ᴍʏ ғᴜʟʟ ᴘᴏᴛᴇɴᴛɪᴀʟ!*
➻ *ᴛʜᴇ ᴍᴏsᴛ ᴩᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴀɴᴅ ɪ ʜᴀᴠᴇ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.*
"""
        try:
            await message.reply_photo(
                photo=image,
                caption=TXT,
                reply_markup=InlineKeyboardMarkup(out),
            )
        except:
            await message.reply_text(
                text=TXT,
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(2):
            sender_id = message.from_user.id
            sender_name = message.from_user.mention
            sender_uname = message.from_user.username
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ʏᴏᴜʀ ʙᴏᴛ.\n\n**ᴜsᴇʀ ɪᴅ:** `{sender_id}`\n**ᴜsᴇʀɴᴀᴍᴇ:** @{sender_uname}",
            )
@QuantamBot.on_message(group=1)
async def start(_, m):
    try:
        if m.chat.type == ChatType.PRIVATE:
            await save_id(m.from_user.id)
        else:
            await chat_id(m.chat.id)
            

    except Exception as e:
        await m.reply(e)


        

            

