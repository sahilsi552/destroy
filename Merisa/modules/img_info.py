"""MIT License

Copyright (c) 2023-24 Noob-QuantamBot

          GITHUB: NOOB-MUKESH
          TELEGRAM: @MR_SUKKUN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
from pyrogram import filters
from PIL import Image,ImageFilter ,ImageDraw,ImageEnhance
from Merisa import QuantamBot as pbot

import os
from random import randrange
from pyrogram.enums import ChatAction
import numpy as np
@pbot.on_message(filters.command("img"))
async def img_info(_, message):
    if message.reply_to_message and message.reply_to_message.media:
        try:
            
            m = await message.reply_to_message.download()
            image= Image.open(m)
            f=image.format 
            mode=image.mode 
            s=image.size
            p=image.palette
            image.close()
            await message.reply_text(f"""ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ɪᴍᴀɢᴇ :\n
    ғᴏʀᴍᴀᴛ : {f}
    ᴍᴏᴅᴇ : {mode}
    sɪᴢᴇ : {s}
    ᴘᴀʟᴇᴛᴛᴇ : {p}""")  
        except Exception as e:
            await message.reply(e)
@pbot.on_message(filters.command("img_split"))
async def img_split(bot, message):
    
    if message.reply_to_message and message.reply_to_message.media:
        try:
            await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
            m = await message.reply_to_message.download()
            image= Image.open(m)
            r, g, b = image.split()
            
            image = Image.merge("RGB", (b, g, r)) 
            image.save("test.jpg")
            image.close()
            await message.reply_photo(photo="test.jpg",quote=True)  
        except Exception as e:
            if os.path.exists("test.jpg"):
                os.remove("test.jpg")
            await message.reply(e)            
@pbot.on_message(filters.command("img_blur"))

async def img_blur(bot, message):
    if message.reply_to_message and message.reply_to_message.media:
        try:
            await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
            m = await message.reply_to_message.download()
            image= Image.open(m)
            
            blur_Image = image.filter(ImageFilter.GaussianBlur(randrange(6))) 
            blur_Image.save("test.jpg")
            image.close()
            blur_Image.close()
            
            
            await message.reply_photo(photo="test.jpg",quote=True)  
            
        except Exception as e:
            if os.path.exists("test.jpg"):
                os.remove("test.jpg")
            await message.reply(e)          
        
@pbot.on_message(filters.command("img_to_gif"))

async def img_gif(bot, message):
    if message.reply_to_message and message.reply_to_message.media:
        try:
           
            await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
            m = await message.reply_to_message.download()
            if m.endswith(".jpg"):
                image= Image.open(m)  
                image.save("test.gif")
                image.close()   
                await message.reply_animation("test.gif",quote=True)
            else:
                await message.reply_text("this commands work  for .jpg  extension")
            
        except Exception as e:
            if os.path.exists("test.gif"):
                os.remove("test.gif")
            await message.reply(e)           
        
@pbot.on_message(filters.command("gif_to_img"))

async def gif_img(_, message):
    if message.reply_to_message and message.reply_to_message.media:
        try:
            m = await message.reply_to_message.download()
            if m.endswith(".gif"):
                image= Image.open(m)  
                image.save("test.jpg")
                image.close()
                await message.reply_animation("test.jpg",quote=True)
            else:
                await message.reply_text("this commands work  for .gif  extension")
            
        except Exception as e:
            if os.path.exists("test.jpg"):
                os.remove("test.jpg")
            await message.reply(e)                 
@pbot.on_message(filters.command("crop_circle"))

async def crop(_, message):
    if message.reply_to_message and message.reply_to_message.media:
        try:
            m = await message.reply_to_message.download()
            img= Image.open(m).convert("RGB")
            height,width = img.size
            lum_img = Image.new('L', [height,width] , 0)
            draw = ImageDraw.Draw(lum_img)
            draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255, outline = "white")
            img_arr =np.array(img)
            lum_img_arr =np.array(lum_img)
            final_img_arr = np.dstack((img_arr,lum_img_arr))
            h=Image.fromarray(final_img_arr)
            h.save("circle.png")
            img.close()
            
            await message.reply_photo("circle.png",quote=True)
            
        except Exception as e:
            if os.path.exists("circle.png"):
                os.remove("circele.png")
            await message.reply(e)                 

async def crop_without_bg(_, message):
    if message.reply_to_message and message.reply_to_message.media:
        try:
            m = await message.reply_to_message.download()
            img= Image.open(m).convert("RGB")
            height,width = img.size
            lum_img = Image.new('L', [height,width] , 0)
            draw = ImageDraw.Draw(lum_img)
            draw.pieslice([(0,0), (height,width)], 0, 360,fill = 255)
            img_arr =np.array(img)
            lum_img_arr =np.array(lum_img)
            final_img_arr = np.dstack((img_arr,lum_img_arr))
            h=Image.fromarray(final_img_arr)
            h.save("circle.png")
            img.close()
            
            await message.reply_document("circle.png",quote=True)
            
        except Exception as e:
            if os.path.exists("circle.png"):
                os.remove("circele.png")
            await message.reply(e)    
@pbot.on_message(filters.command("contrast"))

async def contrast(_, message):
    if message.reply_to_message and message.reply_to_message.media:
        try:
            m = await message.reply_to_message.download()
            img= Image.open(m)
            contrast = ImageEnhance.Contrast(img)
            c=contrast.enhance(1.5)
            c.save("contrast.jpg")
            img.close()
            
            await message.reply_photo("contrast.jpg",quote=True)
            
        except Exception as e:
            if os.path.exists("contrast.jpg"):
                os.remove("contrast.jpg")
            await message.reply(e)         
@pbot.on_message(filters.command("crop"))
async def img_crop(bot, message):
    
    if message.reply_to_message and message.reply_to_message.media:
        try:
            await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
            m = await message.reply_to_message.download()
            image= Image.open(m)
            image.resize((640,360))
            image.save("test.jpg")
            image.close()
            await message.reply_photo(photo="test.jpg",quote=True)  
        except Exception as e:
            if os.path.exists("test.jpg"):
                os.remove("test.jpg")
            await message.reply(e)