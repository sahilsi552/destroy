import requests
from .. import QuantamBot

import time
import logging
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
AI_MODELS: dict = {
   "gpt": 1,
   "claude": 2,
   "mistral": 3,
   "meta": 4
}



@QuantamBot.on_message(filters.command(["gpt", "mistral", "claude", "meta"]))
async def _AiCmds(_, message):
     cmd = message.text.split()[0][1:].lower()
     model_id = AI_MODELS[cmd]
     if len(message.text.split()) < 2:
          return await message.reply("**——› No query provided** 😶")

     query = message.text.split(maxsplit=1)[1]
     data = {
       "messages": [{ "role": "user", "content": query }],
       "model_id": model_id
     }

     msg = await message.reply("✏️")
     api_url = "https://nandhabots-api.vercel.app/duckai"
     response = requests.post(api_url, json=data)
     if response.status_code != 200:
         return await msg.edit_text(f"[ ❌ ERROR: `{response.reason}`]")
     else:
         text = response.json()['reply']
         return await msg.edit_text(text)

__MODULE__ = "Cʜᴀᴛɢᴘᴛ"  

__HELP__ = """
*Get Assistance on a Query:*
๏ /gpt : Reply to a message or type your question and let BaBa provide the answer
""" 
 
