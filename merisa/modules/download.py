from cloudscraper import create_scraper
from datetime import datetime
from urllib.parse import unquote
from pyrogram import Client, enums, filters
import asyncio,random, requests
from .. import QuantamBot ,logging
from bs4 import BeautifulSoup
from ..utils.button_help import ADD_ME
from pyrogram.types import InlineKeyboardMarkup
from pySmartDL import SmartDL
@QuantamBot.on_message(filters.command(["instadownload","instadl"]))
async def instadownload(bot, message):
    try:
        if message.reply_to_message:
            text = message.reply_to_message.text
        elif not message.reply_to_message and len(message.command) != 1:
            text = message.text.split(None, 1)[1]
        
            link = f"https://instagramdownloader.apinepdev.workers.dev/?url={text}"
            response = requests.get(link).json()
            insta=response["data"][0]["url"]
            

            #print(response["data"][0]["url"])
            try:
                await message.reply_video(insta,caption=f"""━━━━━━━{QuantamBot.mention}━━━━━━━

☘️  ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ☘️
◈──────────────◈
🔥 ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ : @{QuantamBot.username}
━━━━━━━{QuantamBot.mention}━━━━━━━""",reply_markup=InlineKeyboardMarkup(ADD_ME)
,quote=True)
            except:
                await message.reply_photo(insta,caption=f"""━━━━━━━{QuantamBot.mention}━━━━━━━

☘️ ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ☘️
◈──────────────◈
🔥 ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ : @{QuantamBot.username}
━━━━━━━{QuantamBot.mention}━━━━━━━""",reply_markup=InlineKeyboardMarkup(ADD_ME)
,quote=True)
            
                
    except Exception as e:
        await message.reply(e,quote=True)



@QuantamBot.on_message(filters.command(["twitterdl"]))
async def twitterdl(_, message):
    if len(message.command) == 1:
        return await message.reply(
            f"Use command /{message.command[0]} [link] to download Twitter video."
        )
    url = message.command[1]
    if "x.com" in url:
        url = url.replace("x.com", "twitter.com")
    msg = await message.reply("Trying download...")
    try:
        headers = {
            "Host": "ssstwitter.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "HX-Request": "true",
            "Origin": "https://ssstwitter.com",
            "Referer": "https://ssstwitter.com/id",
            "Cache-Control": "no-cache",
        }
        data = {
            "id": url,
            "locale": "id",
            "tt": "bc9841580b5d72e855e7d01bf3255278l",
            "ts": "1691416179",
            "source": "form",
        }
        post = await requests.post(f"https://ssstwitter.com/id", data=data, headers=headers, follow_redirects=True)
        if post.status_code not in [200, 401]:
            return await msg.edit_msg("Unknown error.")
        soup = BeautifulSoup(post.text, "lxml")
        cekdata = soup.find("a", {"pure-button pure-button-primary is-center u-bl dl-button download_link without_watermark vignette_active"})
        if not cekdata:
            return await message.reply("ERROR: Oops! It seems that this tweet doesn't have a video! Try later or check your link")
        try:
            fname = (requests.head(cekdata.get("href"))).headers.get("content-disposition", "").split("filename=")[1]
            obj = SmartDL(cekdata.get("href"), progress_bar=False, timeout=15)
            obj.start()
            path = obj.get_dest()
            await message.reply_video(path, caption=f"<code>{fname}</code>\n\nUploaded for {message.from_user.mention} ",)
        except Exception as er:
            logging.error(f"ERROR: while fetching TwitterDL. {er}")
            return await msg.edit_msg("ERROR: Got error while extracting link.")
        await msg.delete()
    except Exception as e:
        await message.reply(f"Failed to download twitter video..\n\n<b>Reason:</b> {e}")
        await msg.delete()




@QuantamBot.on_message(filters.command(["fbdl"]))

async def fbdl(_, message):
    if len(message.command) == 1:
        return await message.reply(
            f"Use command /{message.command[0]} [link] to download Facebook video."
        )
    link = message.command[1]
    msg = await message.reply("Trying download...")
    try:
        resjson = ( requests.get(f"https://yasirapi.eu.org/fbdl?link={link}")).json()
        try:
            url = resjson["result"]["hd"]
        except KeyError:
            url = resjson["result"]["sd"]

        
        await message.reply_video(
            url,
            caption=f"\nUploaded for {message.from_user.mention} ]",
            thumb="assets/thumb.jpg",
        )
        await msg.delete()
        
    except Exception as e:
        await message.reply(
            f"Failed to download Facebook video..\n\n<b>Reason:</b> {e}"
        )
        await msg.delete()
@QuantamBot.on_message(filters.command(["pixelvid","pixelvideo"]))

async def pixelvideo(_, message):
    if len(message.command) == 1:
        return await message.reply(
            f"Use command /{message.command[0]} [link] to download pixel video."
        )
    link = message.command[1]
    msg = await message.reply("Trying download...")
    try:
        url = f"https://api.pexels.com/videos/search?query={link}&per_page=80"
        response = requests.get(url, headers={'Authorization': 'QKyJ9cgOWYD2bbDujIOqYE4w5ZwT7mNGh73sBf0g5oHihnaUNFRT0qPm'})
        quotes = response.json()
        Video=quotes["videos"][random.randint(1,80)]["video_files"][0]["link"]

        
        await message.reply_video(
            Video,
            caption=f"\nUploaded for {message.from_user.mention} </code>]",
            thumb="assets/thumb.jpg",
        )
        await msg.delete()
        
    except Exception as e:
        await message.reply(
            f"Failed to download pixel video..\n\n<b>Reason:</b> {e}"
        )
        await msg.delete()
@QuantamBot.on_message(filters.command(["pixelimg","pixelimage"]))

async def pixelvideo(_, message):
    if len(message.command) == 1:
        return await message.reply(
            f"Use command /{message.command[0]} [link] to download pixel image"
        )
    link = message.command[1]
    msg = await message.reply("Trying download...")
    try:
        url = f"https://api.pexels.com/v1/search?query={link}&per_page=80"
        response = requests.get(url, headers={'Authorization': 'QKyJ9cgOWYD2bbDujIOqYE4w5ZwT7mNGh73sBf0g5oHihnaUNFRT0qPm'})
        quotes = response.json()
        img=quotes["photos"][random.randint(1,80)]["src"]["original"]
        
        await message.reply_photo(
            img,
            caption=f"\nUploaded for {message.from_user.mention} </code>]"
        )
        await msg.delete()
        
    except Exception as e:
        await message.reply(
            f"Failed to download pixel image..\n\n<b>Reason:</b> {e}"
        )
        await msg.delete()

@QuantamBot.on_message(filters.command(["tiktokdl","tikdl"]))
async def tiktokdownload(bot, message):
    try:
        if message.reply_to_message:
            text = message.reply_to_message.text
        elif not message.reply_to_message and len(message.command) != 1:
            text = message.text.split(None, 1)[1]
        
            link = f"https://api.sdbots.tech/tiktok?url={text}"
            response = requests.get(link)
            try:
                results = response.json()
                caption = results.get("result", {}).get("desc", "")
                video_url = results.get("result", {}).get("withoutWaterMarkVideo", "")
                music_mp3 = results.get("result", {}).get("music", "")
                if video_url:
                    return await message.reply_video(video_url,caption=f"""{caption}""",reply_markup=InlineKeyboardMarkup(ADD_ME)
,quote=True)
                    
                
                else:
                    return await message.reply_audio(music_mp3,caption=f"""{caption}""",reply_markup=InlineKeyboardMarkup(ADD_ME),quote=True)
            except Exception as e:
                await message.reply(e,quote=True)
    except Exception as e:
        await message.reply(e,quote=True)
                    
                
