from unidecode import unidecode
# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters
import asyncio
from pyrogram.enums import ParseMode
from .. import QuantamBot
from Merisa.utils.button_help import *
from Merisa.database import is_served_user
@QuantamBot.on_message(filters.command(["unidecode", f"unidecode@{QuantamBot.username}"]))
async def unide_user(bot, message):
    try:
        x=await is_served_user(message.from_user.id)
        if x==False:
            return await message.reply("you are not verifed user start me in pm to verfiy",reply_markup=VERIFY)
        if message.reply_to_message:
            text = message.reply_to_message.text
        elif not message.reply_to_message and len(message.command) != 1:
            text = message.text.split(None, 1)[1]
        await message.reply_text(unidecode(text),quote=True)
    except Exception as e:
        await message.reply(e,quote=True)