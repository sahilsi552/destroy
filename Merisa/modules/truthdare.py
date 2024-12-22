import requests

# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters
import asyncio

from .. import QuantamBot


@QuantamBot.on_message(filters.command(["truth", f"truth@{QuantamBot.username}"]))
async def truth(bot, message):

    truth = requests.get(f"https://api.truthordarebot.xyz/v1/truth").json()["question"]
    await message.reply_text(truth)
@QuantamBot.on_message(filters.command(["dare", f"dare@{QuantamBot.username}"]))
async def dare(bot, message):

    dare = requests.get(f"https://api.truthordarebot.xyz/v1/dare").json()["question"]
    await message.reply_text(dare)