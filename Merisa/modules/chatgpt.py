import requests
from pyrogram import filters

from .. import QuantamBot as app
from SafoneAPI import SafoneAPI


@app.on_message(filters.command(["gpt"]))
async def bard(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text(
            "Example:\n\n`/bard what is color of ass `"
        )
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])

    try:
        Z = await SafoneAPI().bard(user_input)
        result = Z["candidates"][0]["content"]["parts"][0]["text"]
        await message.reply_text(result)
    except requests.exceptions.RequestException as e:
        pass
