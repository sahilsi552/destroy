from telegraph import Telegraph
# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from PIL import Image
from pyrogram import filters
import asyncio,requests,shutil
from .. import QuantamBot
from Merisa.utils.button_help import ADD_ME
from pyrogram.types import InlineKeyboardButton as ikb, InlineKeyboardMarkup 

def resize_image(image):
    img= Image.open(image)
    img.save(image, "PNG")



    
@QuantamBot.on_message(filters.command(["removebg", f"removebg@{QuantamBot.username}","bgrm"]))
async def remove_bg(b, m):
    

    try:
        
        if m.reply_to_message and m.reply_to_message.media:
            Z=await m.reply("wait a moment")
            img=await m.reply_to_message.download()
            if img.endswith((".webp")):
                resize_image(img)
            with open(img, "rb") as image_file:
                X=image_file.read()
                endpoint = "https://api.remove.bg/v1.0/removebg"
                payload = {"size": "auto"}
                response = requests.post(endpoint,data=payload,headers={"X-Api-Key": "cjFwfkwVr6ZgByFuQjkVbt53"}, files={"image_file":X},stream=True )
            with open("output.png", "wb") as out_file:
                x=shutil.copyfileobj(response.raw, out_file)
            await Z.delete()
            await m.reply_photo(photo="output.png",reply_markup=InlineKeyboardMarkup(ADD_ME))
    except Exception as e:
        await m.reply(e,quote=True)   
