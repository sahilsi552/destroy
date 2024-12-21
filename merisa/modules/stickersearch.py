from pyrogram import filters
from .. import QuantamBot 
from pyrogram.enums import ChatAction

import requests


@QuantamBot.on_message(filters.command("stickers"))
async def sticker_search(b, m):
  #  await b.send_chat_action(m.chat.id, ChatAction.UPLOAD_PHOTO)
    if len(m.command) < 2:
        return await m.reply_text("Example:\n\n/stickers boy")
    mukesh = await m.reply("Please wait a sec...")
    try:
        if m.reply_to_message and m.reply_to_message.text:
            text = m.reply_to_message.text
        else:
  
            text = m.text.split(" ", 1)[1]
        url = f"https://api.safone.dev/tgsticker?query={text}"
        headers = {"accept": "application/json"}
        
        try:
            response = requests.get(url, headers=headers)
            out = response.json()
            X=out["results"]
            Title=[]
            Link=[]
            for i in X:
                Title.append(i["title"])
                Link.append(i["link"])
            stick= f"sᴛɪᴄᴋᴇʀs ғᴏʀ {text}"
            for t, l in zip(Title, Link):
                stick+= f"\n• <a href='{l}'> {t}</a>"
            await mukesh.delete()
            await m.reply(stick)
    
          
          
    
            
            
        except Exception as e:
            await m.reply(f"Error: {str(e)}")
    except Exception as e:
        await m.reply(str(e))
