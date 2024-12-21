
from pyrogram import filters
from pyrogram.types import Message
import requests
from .. import QuantamBot as pbot
from ..database import token_is_user as is_user,token_add_user as add_user,token_remove_user as remove_user
from MukeshAPI import api
@pbot.on_message(filters.command("token") & filters.private)
async def gen_token(_, message: Message):
    apis = f"{message.from_user.id}-mukesh-api-{api.password()}"
    if not await is_user(message.from_user.id):
        await add_user(message.from_user.id, apis)
        await message.reply_text(
            f"🔑 ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴛᴏᴋᴇɴ ғᴏʀ ᴍᴜᴋᴇsʜ ᴀᴘɪ:\n<code>{api}</code>\n\n<b>ᴅᴏɴ'ᴛ sʜᴀʀᴇ ᴛʜɪs ᴛᴏᴋᴇɴ ᴡɪᴛʜ ᴀɴʏᴏɴᴇ ᴇʟsᴇ.</b>"
        )
    else:
        mukesh = await is_user(message.from_user.id)
        await message.reply_text(
            f"🔑 ʏᴏᴜ'ᴠᴇ ᴀʟʀᴇᴀᴅʏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʏᴏᴜʀ ᴛᴏᴋᴇɴ:\n<code>{mukesh}</code>\n\n<b>ᴅᴏɴ'ᴛ sʜᴀʀᴇ ᴛʜɪs ᴛᴏᴋᴇɴ ᴡɪᴛʜ ᴀɴʏᴏɴᴇ ᴇʟsᴇ.</b>"
        )

@pbot.on_message(filters.command("revoke") & filters.private)
async def rev_token(_, message: Message):
    if not await is_user(message.from_user.id):
        return await message.reply_text(
            f"🚫 ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴛᴏᴋᴇɴ ʙᴇғᴏʀᴇ."
        )
    mukesh = await is_user(message.from_user.id)
    await remove_user(message.from_user.id, mukesh)
    await message.reply_text(
        f"<b>🔓 ᴍᴜᴋᴇsʜ ᴀᴘɪ ᴛᴏᴋᴇɴ ʀᴇᴠᴏᴋᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.</b>\n\nʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ʏᴏᴜʀ ᴛᴏᴋᴇɴ ᴀɢᴀɪɴ ʙʏ /token"
    )

