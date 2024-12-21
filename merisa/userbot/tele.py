from telegraph import Telegraph
# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from PIL import Image
from pyrogram import filters,Client 
import asyncio


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


telegraph = Telegraph(domain="graph.org")
telegraph.create_account("Client.username")

def graph_text(title,text):
    z=telegraph.create_page(title=title,html_content=text.html.replace("\n", "<br>"))
    return z["url"]

def graph_img(img):
    try:
        z=telegraph.upload_file(img)
        return z[0]["src"]
    except Exception as e:
        print(e)
        
@Client.on_message(filters.command(["tgt"],".")& filters.me)
async def telegraph_text(_, m):
    
    if m.reply_to_message:
        text=m.reply_to_message.text
    elif not m.reply_to_message:
        text = m.text.split(None, 1)[1]
    x=await m.reply("wait a moment")

    h=graph_text(m.from_user.first_name,text)
   
    await m.reply(f"Uᴘʟᴏᴀᴅᴇᴅ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ {h}",disable_web_page_preview=True)
    
@Client.on_message(filters.command("tgm",".")& filters.me)
async def telegraph_img(b, m):
    

    try:
        
        if m.reply_to_message and m.reply_to_message.media:
            x=await m.reply("wait a moment")
            img=await m.reply_to_message.download()
            if img.endswith((".webp")):
                resize_image(img)
            h=graph_img(img)
            await x.delete()
            await m.reply(f"Uᴘʟᴏᴀᴅᴇᴅ ᴛᴏ [ᴛᴇʟᴇɢʀᴀᴘʜ](https://graph.org/{h})",disable_web_page_preview=False)
    except Exception as e:
        await m.reply(e,quote=True)

    
