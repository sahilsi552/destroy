
from pyrogram import filters
import asyncio
from .. import QuantamBot
from Merisa.utils.button_help import *
from music_text import SEEKBACK

@QuantamBot.on_message(
    filters.command(["source", "repo"], prefixes=["+", ".", "/", "-", "?", "$"])
)
async def source(_, m):
    await m.reply_photo(
        START_IMG,
        caption=SOURCE_TEXT,
        reply_markup=SOURCE_BUTTONS
    )
__MODULE__="SEEK"
__HELP__=SEEKBACK