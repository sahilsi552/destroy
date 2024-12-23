
# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters
import asyncio
from .. import QuantamBot as Mukesh
from Merisa.utils.button_help import *
from Merisa.database import *


@Mukesh.on_message(filters.command(["stats", f"stats@{Mukesh.username}"]))
async def stats(_, m):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await m.reply(f"""  ᴛᴏᴛᴀʟ ꜱᴛᴀᴛꜱ  {Mukesh.mention}:\nᴜꜱᴇʀꜱ: {users}\nᴄʜᴀᴛ: {chats}""")