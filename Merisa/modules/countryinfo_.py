from countryinfo import CountryInfo
from pyrogram import filters
from .. import QuantamBot
import asyncio
from pyrogram.types import InlineKeyboardButton as ikb, InlineKeyboardMarkup as ikm
from pyrogram.enums import ParseMode

@QuantamBot.on_message(filters.command(["country","nation"]))
async def country_info(bot, message):
    if len(message.command) < 2:
        return await message.reply_text("**Example:**\n\n`/country India`")
    m = message.text.split(' ')[1]
    try:
        country = CountryInfo(m)
        x = country.info()
        name = x.get("name")
        bb = x.get("altSpellings")
        alt= (", ".join(bb))
        area = x.get("area")
        hell = x.get("borders")
        borders=(", ".join(hell))
        WhAt = x.get("callingCodes")
        call = (", ".join(WhAt))
        capital = x.get("capital")
        currencies = x.get("currencies")
        currency=(", ".join(currencies))
        dem = x.get("demonym")
        languages = x.get("languages")
        langs =(", ".join(languages))
        native = x.get("nativeName")
        population = x.get("population")
        region = x.get("region")
        sub_region = x.get("subregion")
        tik = x.get("timezones")
        timzezones =(", ".join(tik))
        GOT = x.get("tld")
        total_levels = (", ".join(GOT))
        wikiped = x.get("wiki")
        z=[
            [ikb("ᴡɪᴋɪᴘᴇᴅɪᴀ", url=wikiped)
            
            ]
        ]
        TEXT = f"""
**ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɢᴀᴛʜᴇʀᴇᴅ sᴜᴄᴇssғᴜʟʟʏ**
      
ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ : `{name}`
ᴀʟᴛᴇʀɴᴀᴛɪᴠᴇ sᴘᴇʟʟɪɴɢs : `{alt}`
ᴄᴏᴜɴᴛʀʏ ᴀʀᴇᴀ :`{area} km square`
ʙᴏʀᴅᴇʀs : `{borders}`
ᴄᴀʟʟɪɴɢ ᴄᴏᴅᴇs : `{call}`
ᴄᴏᴜɴᴛʀʏ's ᴄᴀᴘɪᴛᴀʟ : `{capital}`
ᴄᴏᴜɴᴛʀʏ's ᴄᴜʀʀᴇɴᴄʏ : `{currency}`
ᴅᴇᴍᴏʏᴍ : `{dem}`
ʟᴀɴɢᴜᴀɢᴇs : `{langs}`
ɴᴀᴛɪᴠᴇ ɴᴀᴍᴇs : `{native}`
ᴘᴏᴘᴜʟᴀᴛɪᴏɴs : `{population}`
ʀᴇɢɪᴏɴ : `{region}`
sᴜʙ ʀᴇɢɪᴏɴ : `{sub_region}`
ᴛɪᴍᴇ ᴢᴏɴᴇs : `{timzezones}`
ᴛᴏᴛᴀʟ ʟᴇᴠᴇʟ ᴅᴏᴍᴀɪɴ : `{total_levels}`

ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɢᴀᴛʜᴇʀᴇᴅ ʙʏ {QuantamBot.name}
"""
        await message.reply_text(TEXT,parse_mode=ParseMode.MARKDOWN, reply_markup=ikm(z))
    except Exception as e:
        print(e)

        

__HELP__ = """
 ɪ ᴡɪʟʟ ɢɪᴠᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴄᴏᴜɴᴛʀʏ

 ๏ /country <ᴄᴏᴜɴᴛʀʏ ɴᴀᴍᴇ>*:* ɢᴀᴛʜᴇʀɪɴɢ ɪɴғᴏ ᴀʙᴏᴜᴛ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛʀʏ
 """

__MODULE__ = "Cᴏᴜɴᴛʀʏ"
