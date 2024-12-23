# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters, Client
import asyncio
from .. import QuantamBot
from Merisa.utils.button_help import *
from pyrogram.enums import ParseMode
from pyrogram.errors import UserNotParticipant, ChatWriteForbidden, ChatAdminRequired
from config import UPDATE_CHNL, SUPPORT_GRP as Update2

#  force

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# @QuantamBot.on_message(filters.incoming & filters.private, group=-1)
# async def must_join_channel(bot: Client, msg):
#     if not UPDATE_CHNL and not Update2:
#         return
#     try:
#         try:
#             await bot.get_chat_member(UPDATE_CHNL, msg.from_user.id)
#             await bot.get_chat_member(Update2, msg.from_user.id)
#         except UserNotParticipant:
#             if UPDATE_CHNL.isalpha() and Update2.isalpha():
#                 link = "https://t.me/" + UPDATE_CHNL
#                 link2 = "https://t.me/" + Update2

#             else:
#                 chat_info = await bot.get_chat(UPDATE_CHNL)
#                 link = chat_info.invite_link
#                 chat_info = await bot.get_chat(Update2)
#                 link2 = chat_info.invite_link
#             try:
#                 await msg.reply_photo(
#                     photo=START_IMG,
#                     caption=f'»<b> ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ\'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ <a href ="{link}"> ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ </a> ᴀɴᴅ <a href="{link2}">Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ </a> ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ <a href="{link}"> ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ </a> ᴀɴᴅ <a href="{link2}"> Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ </a> ᴛʜᴇɴ /start  ᴍᴇ ᴀɢᴀɪɴ !</b>',
#                     parse_mode=ParseMode.HTML,
#                     reply_markup=InlineKeyboardMarkup(
#                         [
#                             [
#                                 InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=link),
#                                 InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ", url=link2),
#                             ]
#                         ]
#                     ),
#                 )
#                 await msg.stop_propagation()
#             except ChatWriteForbidden:
#                 pass
#     except ChatAdminRequired:
#         print(f"Promote me as an admin in the UPDATE CHANNEL  : {UPDATE_CHNL} !")
#         print(f"Promote me as an admin in the Update2  : {Update2} !")
