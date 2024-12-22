# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters
from pyrogram.enums import ParseMode
from .. import QuantamBot
from Merisa.utils.button_help import IMGX
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import *
from pyrogram import *
import  asyncio


def get_user_status():
    if status == pyrogram.enums.UserStatus.ONLINE:
        return "online"
    elif status == pyrogram.enums.UserStatus.OFFLINE:
        return "User is offline"
    elif status == pyrogram.enums.UserStatus.RECENTLY:
        return "last seen recently"
    elif status == pyrogram.enums.UserStatus.LAST_WEEK:
        return "last seen within a week"
    elif status == pyrogram.enums.UserStatus.LAST_MONTH:
        return "last seen within a month"
    else:
        return "last seen a long time ago"


@QuantamBot.on_message(filters.command(["info", f"info@{QuantamBot.username}"]))
async def info_user(_, message):
    global status
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) == 1:
        user = message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]
    m = await message.reply_text("ɢᴇᴛᴛɪɴɢ ᴜsᴇʀɪɴғᴏ")
    hm = await QuantamBot.get_users(user)
    status = hm.status
    await m.delete()

    userinfo = f"""<b><u>ᴜsᴇʀ ɪɴғᴏ </u>
ᴜsᴇʀ ɪᴅ: <code>{hm.id}</code>
ғɪʀsᴛ ɴᴀᴍᴇ: {hm.first_name}
{"ʟᴀsᴛ ɴᴀᴍᴇ: " + hm.last_name if hm.last_name else ""}
{"ᴜsᴇʀɴᴀᴍᴇ: @" + hm.username  if hm.username else ""}
ʟɪɴᴋ: {hm.mention}
sᴛᴀᴛᴜs: {get_user_status()}
ᴅᴄ ɪᴅ: <code>{hm.dc_id}</code>
ᴘʀᴇᴍɪᴜᴍ: <code>{hm.is_premium}</code>
ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇ: <code>{hm.language_code}</code></b>
"""

    photo_id = hm.photo.big_file_id if hm.photo else None
    if not photo_id:
        return await message.reply_text(
            userinfo,parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(IMGX)
        )
    photo = await QuantamBot.download_media(photo_id)

    await message.reply_photo(
        photo, caption=userinfo,parse_mode=ParseMode.HTML, reply_markup=InlineKeyboardMarkup(IMGX)
    )
