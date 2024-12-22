
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
from .. import  QuantamBot
from bs4 import BeautifulSoup
import requests, asyncio
from pyrogram import Client, filters

from gtts import gTTS


@QuantamBot.on_message(filters.command("news"))
async def news(_, m):
    await m.delete()
    msg=await m.reply("Wait a moment..")
    try:
        #hour = int(datetime.datetime.now().hour)

        url = "https://www.thehindu.com/news/national"
        x = requests.get(url)
        soup = BeautifulSoup(x.content, "html.parser")
        head = soup.title.string

        cl = soup.find("body").find_all("h3")
        X=f" **{head}**"
        for c, news in enumerate( cl,start=1):
            X+=f"`{c}. {news.text.strip()}`\n"
        #print(X)
        lang = 'en'
        myobj = gTTS(text=X, lang=lang, slow=False)
        myobj.save("news.mp3")
        await msg.delete()
        async def progress(current, total):
            print(f"{current * 100 / total:.1f}%")      
        await m.reply_audio("news.mp3",caption=f"{X[:1000]} ....",title=head[:25]
          ,performer=f"@{QuantamBot.username}",progress=progress)

    except Exception as e:
        await m.reply_text(e)
__HELP__="""
Iɴᴅɪᴀ Lᴀᴛᴇsᴛ Nᴇᴡs:

"""
__MODULE__="Nᴇᴡs"
