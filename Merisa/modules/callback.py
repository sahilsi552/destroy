
from pyrogram import Client,filters
import asyncio
from .. import QuantamBot
from config import OWNER_ID
from Merisa.utils.button_help import *
from pyrogram.types import CallbackQuery
from pyrogram.types import InputMediaVideo

@QuantamBot.on_callback_query(filters.regex("^closeforce"))
async def callback_handler(_: Client, query: CallbackQuery):
    if query.data == "closeforce":
        await query.message.delete()

    
