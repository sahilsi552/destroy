
import io
import aiohttp
from pyrogram import filters
from .. import QuantamBot

@QuantamBot.on_message(filters.command("weather"))
async def weathers_(_, m):
    if len(m.command) < 2:
        return await m.reply_text(
            "​usage!`\nExample `/weather bihar`")
    text=m.text.split(None,1)[1]
    sample_url = "https://wttr.in/{}.png"
    async with aiohttp.ClientSession() as session:
        response_api_zero = await session.get(sample_url.format(text))
        response_api = await response_api_zero.read()
        with io.BytesIO(response_api) as out_file:
            await m.reply_photo(photo=out_file)


__HELP__ = """
ɪ ᴄᴀɴ ғɪɴᴅ ᴡᴇᴀᴛʜᴇʀ ᴏғ ᴀʟʟ ᴄɪᴛɪᴇs

 ❍ /weather <ᴄɪᴛʏ>*:* ᴀᴅᴠᴀɴᴄᴇᴅ ᴡᴇᴀᴛʜᴇʀ ᴍᴏᴅᴜʟᴇ, ᴜsᴀɢᴇ sᴀᴍᴇ ᴀs /ᴡᴇᴀᴛʜᴇʀ
 ❍ /weather  ᴍᴏᴏɴ*:* ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs ᴏғ ᴍᴏᴏɴ
ɪ ᴡɪʟʟ ɢɪᴠᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴄᴏᴜɴᴛʀʏ
 ❍ /nation <ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ>*:* ɢᴀᴛʜᴇʀɪɴɢ ɪɴғᴏ ᴀʙᴏᴜᴛ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛʀʏ"""
__MODULE__ = "World"
