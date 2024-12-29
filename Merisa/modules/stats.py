
# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters
import asyncio
from .. import QuantamBot as Mukesh
from Merisa.utils.button_help import *
from Merisa.database import *
from .. import db
from Merisa.database.approve import Approve


@Mukesh.on_message(filters.command(["stats", f"stats@{Mukesh.username}"]))
async def stats(_, m):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    afk=await db.afkdb.count_documents({})
    chatbot=await db.chatbot.count_documents({})
    notes=await db.notes.count_documents({})
    filters=await db.filters.count_documents({})
    gban=await db.gban.count_documents({})
    
    appdb = Approve
    approved=f"<b>Approved People</b>: <code>{(appdb.count_all_approved())}</code> in <code>{(appdb.count_approved_chats())}</code> chats\n"
    
    await m.reply(f"""
ᴛᴏᴛᴀʟ ꜱᴛᴀᴛꜱ  of {Mukesh.mention}
total ᴜꜱᴇʀꜱ: {users}
total ᴄʜᴀᴛ: {chats}
total ᴀꜰᴋ user: {afk}
{approved}
total Notes saved  :{notes}
total filters saved :{filters}
total gban users :{gban}

""")
