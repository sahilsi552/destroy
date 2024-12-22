from telegraph import Telegraph
from .. import QuantamBot
from pyrogram import filters
import requests,os
from Merisa.modules.telegrph_ import  graph_img,resize_image
telegraph = Telegraph(domain="graph.org")
telegraph.create_account("QuantamBot")
@QuantamBot.on_message(filters.command("detect"))
async def detect_(_, m):
    x = await m.reply("wait a moment")
    try:
        if m.reply_to_message and m.reply_to_message.media:
            img = await m.reply_to_message.download()
            if img.endswith((".webp")):
                resize_image(img)
            h = graph_img(img)
            await x.delete()
            url = f"https://script.google.com/macros/s/AKfycbwURISN0wjazeJTMHTPAtxkrZTWTpsWIef5kxqVGoXqnrzdLdIQIfLO7jsR5OQ5GO16/exec?url=https://graph.org/{h}"
            response = requests.get(url).json()
            if response["status"] == 200:
                out = response["text"]
                await m.reply_text(f"`{out}`")
            else:
                await m.reply("failed to fetch")
    except Exception as e:
        await m.reply(e, quote=True)
