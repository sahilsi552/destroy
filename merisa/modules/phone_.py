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
import json
import requests
from pyrogram import filters

from .. import QuantamBot


# __mod_name__ = "𝙿ʜᴏɴᴇ"
# __help__ = """
# » /phone ꜰɪʟʟ ᴀɴʏ ᴍᴏʙɪʟᴇ ɴᴜᴍʙᴇʀ ᴛᴏ ᴄʜᴇᴄᴋ ɪɴꜰᴏ.
# """


@QuantamBot.on_message(filters.command("phone"))

async def phone_num(_, m):
    if len(m.command) < 2:
        return await m.reply_text(
            "please provide phone number  in given format example :/phone +919100000000`")
    number=m.text.split(None,1)[1]

    key = "f66950368a61ebad3cba9b5924b4532d"
    api = (
        "http://apilayer.net/api/validate?access_key="
        + key
        + "&number="
        + number
        + "&country_code=&format=1"
    )
    output = requests.get(api)
    content = output.text
    obj = json.loads(content)
    country_code = obj["country_code"]
    country_name = obj["country_name"]
    location = obj["location"]
    carrier = obj["carrier"]
    line_type = obj["line_type"]
    validornot = obj["valid"]
    aa = "Valid: " + str(validornot)
    a = "Phone number: " + str(number)
    b = "Country: " + str(country_code)
    c = "Country Name: " + str(country_name)
    d = "Location: " + str(location)
    e = "Carrier: " + str(carrier)
    f = "Device: " + str(line_type)
    g = f"{aa}\n{a}\n{b}\n{c}\n{d}\n{e}\n{f}"
    await m.reply_text(g,quote=True)


