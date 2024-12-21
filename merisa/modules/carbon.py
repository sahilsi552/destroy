from pyrogram import filters
from .. import QuantamBot 
from pyrogram.enums import ChatAction
from io import BytesIO
from base64 import b64decode
import requests


@QuantamBot.on_message(filters.command("carbon"))
async def carbon_(b, m):
    await b.send_chat_action(m.chat.id, ChatAction.UPLOAD_PHOTO)
    if len(m.command) < 2:
        return await m.reply_text("Example:\n\n/carbon <text>")
    mukesh = await m.reply("Please wait a sec...")
    try:
        if m.reply_to_message and m.reply_to_message.text:
            text = m.reply_to_message.text
        else:
  
            text = m.text.split(" ", 1)[1]
        url = "https://api.safone.dev/carbon"
        headers = {"accept": "application/json"}
        params = {"code": text}
        try:
            response = requests.get(url, params=params, headers=headers)
            out = response.json()
            img = out["image"]
            photo = BytesIO(b64decode(img.encode("utf-8")))
            await mukesh.delete()
            await m.reply_photo(photo)
        except Exception as e:
            await m.reply(f"error: {str(e)}")
    except Exception as e:
        await m.reply(str(e))
