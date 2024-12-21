from aiohttp import ClientSession
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .. import QuantamBot
import re


@QuantamBot.on_message(filters.command(["github","git"]))
async def github(_, message):
    if len(message.command) != 2:
        return await message.reply_text("/github {username} \nExample`/github Noob-QuantamBot`")
    username = message.text.split(None, 1)[1]
    URL = f"https://api.github.com/users/{username}"
    async with ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")
            result = await request.json()
            try:
                url = result["html_url"]
                name = result["name"]
                id=result["id"]
                company = result["company"]
                bio = result["bio"]
                pattern = "[a-zA-Z]+"
                created_at = result["created_at"]
                created = re.sub(pattern, " ",created_at)
                updated_at = result["updated_at"]
                updated = re.sub(pattern, " ",updated_at)
                avatar_url = f"https://avatars.githubusercontent.com/u/{id}"

                blog = result["blog"]
                location = result["location"]
                repositories = result["public_repos"]
                followers = result["followers"]
                following = result["following"]
                global QuantamBot
                QuantamBot = [[
            InlineKeyboardButton(text="ᴘʀᴏғɪʟᴇ ʟɪɴᴋ", url=url),
            InlineKeyboardButton("Cʟᴏsᴇ",callback_data="closeforce")
            ]]     
                caption = f"""**Iɴғᴏ Oғ {name}**
**ᴜsᴇʀɴᴀᴍᴇ :** `{username}`
**ɪᴅ:** `{id}`
**ʙɪᴏ :** `{bio}`
**ᴄᴏᴍᴘᴀɴʏ :** `{company}`
**ᴄʀᴇᴀᴛᴇᴅ ᴏɴ:** `{created}`
**ʀᴇᴘᴏsɪᴛᴏʀɪᴇs :** `{repositories}`
**ʙʟᴏɢ :** `{blog}`
**ʟᴏᴄᴀᴛɪᴏɴ :** `{location}`
**ғᴏʟʟᴏᴡᴇʀs  :** `{followers}`
**ғᴏʟʟᴏᴡɪɴɢ :** `{following}`
**ᴜᴘᴅᴀᴛᴇᴅ ᴀᴛ:** `{updated}`"""

            except Exception as e:
                await message.reply(f"#ERROR {e}")
                  
    await message.reply_photo(photo=avatar_url, caption=caption,reply_markup=InlineKeyboardMarkup(QuantamBot))

__MODULE__ = "Gɪᴛʜᴜʙ"

__HELP__ = """
ᴘʀᴏᴠɪᴅᴇs ʏᴏᴜ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ɢɪᴛʜᴜʙ ᴘʀᴏғɪʟᴇ. 

 ❍ /github <ᴜsᴇʀɴᴀᴍᴇ> *:* ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ɢɪᴛʜᴜʙ ᴜsᴇʀ.
"""