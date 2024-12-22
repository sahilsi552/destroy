from pyrogram import filters
import pyfiglet
from Merisa import QuantamBot
from Merisa.utils.button_help import M

@QuantamBot.on_message(filters.command("figlet"))
async def echo(_, message):
    global text
    try:
        text = message.text.split(' ',1)[1]
    except IndexError:
        return await message.reply_text("Example:\n\n`/figlet QuantamBot`")
    kul_text= pyfiglet.figlet_format(text,font = "slant")
    await message.reply_text(f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ғɪɢʟᴇᴛ :\n<pre>{kul_text}</pre>", quote=True,reply_markup=M)

  