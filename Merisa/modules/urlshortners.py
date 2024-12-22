from pyrogram import Client, enums, filters, idle
import re
from requests import get
import asyncio
from Merisa import QuantamBot
from pyrogram.types import InlineKeyboardButton as ikb, InlineKeyboardMarkup as ikm, Message
from pyrogram.enums import ChatAction, ParseMode
import pyshorteners
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

shortener = pyshorteners.Shortener()
from pyrogram.handlers import MessageHandler

# URL validation function
def is_valid_url(url):
    url_pattern = re.compile(r'https?://\S+')
    return re.match(url_pattern, url)

@QuantamBot.on_message(filters.command(["short"]))
async def short_urls(bot, message):
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    if len(message.command) < 2:
        return await message.reply_text("**Example:**\n\n`/short [url]`")
    
    link = message.command[1]
    
    if not is_valid_url(link):
        return await message.reply_text("Invalid URL. Please provide a valid URL.")
    
    try:
        tiny_link = shortener.tinyurl.short(link)
        dagd_link = shortener.dagd.short(link)
        clckru_link = shortener.clckru.short(link)
        isgd_link = shortener.isgd.short(link)
        osdb_link = shortener.osdb.short(link)

        shorted = [tiny_link, dagd_link, clckru_link, isgd_link, osdb_link]
        url = [
            [ikb("🔗 Tiny Url", url=tiny_link)],
            [ikb("🔗 Dagd Url", url=dagd_link), ikb("🔗 Clckru Url", url=clckru_link)],
            [ikb("🔗 Is.gd Url", url=isgd_link), ikb("🔗 Osdb Url", url=osdb_link)]
        ]
        await message.reply_text("Here are a few shortened links:", reply_markup=ikm(url))
        logger.info(f"Shortened URLs for {link}: {shorted}")

    except pyshorteners.exceptions.ShorteningErrorException as e:
        logger.error(f"Shortening error: {e}")
        await message.reply_text("Error in shortening the URL. Please try again later.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        await message.reply_text("An unexpected error occurred. Please try again later.")

@QuantamBot.on_message(filters.command(["unshort"]))
async def unshort(bot, message):
    await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    if len(message.command) < 2:
        return await message.reply_text("**Example:**\n\n`/unshort [short-url]`")
    
    link = message.text.split(' ')[1]
    
    if not is_valid_url(link):
        return await message.reply_text("Invalid URL. Please provide a valid URL.")
    
    try:
        x = get(link, allow_redirects=True).url
        url = [[ikb("🔗 View Link", url=x)]]
        await message.reply_text(f"Here's the unshortened link:\n`{x}`", reply_markup=ikm(url))
        logger.info(f"Unshortened URL for {link}: {x}")

    except requests.exceptions.RequestException as e:
        logger.error(f"Request error: {e}")
        await message.reply_text("Error in unshortening the URL. Please try again later.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        await message.reply_text(f"An unexpected error occurred: {e}")

__HELP__ = """
*To create a shortened URL:*
๏ /short (URL): Creates a short version of the provided URL. For example:
`/short https://t.me/text`.

*To unshorten a URL:*
๏ /unshort (short-URL): Retrieves the original URL from the shortened version. For example:
 `/unshort https://tinyurl.com/example`.
"""

__MODULE__ = "Sʜᴏʀᴛᴇɴ"  
