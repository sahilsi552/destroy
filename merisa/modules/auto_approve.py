# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters
import asyncio,os
from .. import QuantamBot
from Merisa.utils.button_help import *
from pyrogram.enums import ParseMode
from pyrogram.types import ChatJoinRequest
from pytz import timezone 
from datetime import datetime
from config import *

@QuantamBot.on_chat_join_request(filters.group | filters.channel)
async def join_requests(client: QuantamBot, msg: ChatJoinRequest):
    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    try:
        await client.approve_chat_join_request(chat_id, user_id)
        if APPROVED == "on":
            chat_photo = msg.chat.photo.big_file_id 
            img=await client.download_media(chat_photo)
            await client.send_photo(
                chat_id=user_id,photo=img,
                caption=f"​ʜᴇʟʟᴏ {msg.from_user.mention}\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {msg.chat.title}  \nᴊᴏɪɴᴇᴅ ᴀᴛ: {ind_time}\n\nʏᴏᴜʀ ᴀᴜᴛᴏ ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ {QuantamBot.mention} \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ  ||@mr_sukkun||\nʜɪᴛ ʜᴇʟᴘ ꜰᴏʀ ᴍᴏʀᴇ /help", reply_markup=IKM(ADD_ME)
                )
            
    except:
        pass
