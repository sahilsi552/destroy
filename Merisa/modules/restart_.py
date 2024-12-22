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
import os
import asyncio
from config import OWNER_ID 
from pyrogram import filters
from .. import QuantamBot

@QuantamBot.on_message(filters.command(["reboot", "update"]) &filters.user(OWNER_ID))
async def update_bot(_, m):
    rr = await m.reply_text("__ʀᴇsᴛᴀʀᴛɪɴɢ__")
    await rr.edit("__sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇsᴛᴀʀᴛᴇᴅ ᴡᴀɪᴛ ᴀ ᴡʜɪʟᴇ..__")
    os.system("pip3 install -r requirements.txt")
    os.system(f"kill -9 {os.getpid()} && python3 -m Merisa")
