from pyrogram import filters,Client
from Merisa import QuantamBot
import speedtest
from config import SUPPORT_GRP
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,CallbackQuery
def convert(speed):
    return round(int(speed) / 1048576, 2)
@QuantamBot.on_message(filters.command("speedtest"))
async def speed_test(_, message):
    s=speedtest.Speedtest()
    buttons = [
        [
            InlineKeyboardButton("ɪᴍᴀɢᴇ", callback_data="speedtest_image"),
            InlineKeyboardButton("ᴛᴇxᴛ", callback_data="speedtest_text"),
        ]
    ]
    await message.reply_text(
        "sᴩᴇᴇᴅᴛᴇsᴛ ᴍᴏᴅᴇ", reply_markup=InlineKeyboardMarkup(buttons)
    )
@QuantamBot.on_callback_query(filters.regex("^speedtest"))
async def callback_handler(_: Client, query: CallbackQuery):
    msg =await query.message.edit_text("ʀᴜɴɴɪɴɢ ᴀ sᴩᴇᴇᴅᴛᴇsᴛ...")
    speed = speedtest.Speedtest()
    speed.get_best_server()
    speed.download()
    speed.upload()
    replymsg = "sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛ"
    if query.data == "speedtest_image":
            speedtest_image = speed.results.share()
            await query.message.reply_photo(
                photo=speedtest_image, caption=replymsg
            )
            await msg.delete()

    elif query.data == "speedtest_text":
            result = speed.results.dict()
            replymsg += f"\nᴅᴏᴡɴʟᴏᴀᴅ: `{convert(result['download'])}ᴍʙ/ꜱ`\nᴜᴘʟᴏᴀᴅ: `{convert(result['upload'])}ᴍʙ/ꜱ`\nᴘɪɴɢ: `{result['ping']}`"
            await query.message.edit_text(replymsg, parse_mode=ParseMode.MARKDOWN)
    else:
        await query.answer(F"You are required to join @{SUPPORT_GRP} to use this command.")
__HELP__ = """
» /speedtest *:* ʀᴜɴs ᴀ sᴘᴇᴇᴅᴛᴇsᴛ ᴀɴᴅ ᴄʜᴇᴄᴋ ᴛʜᴇ sᴇʀᴠᴇʀ sᴘᴇᴇᴅ.
"""

__MODULE__ = "SᴘᴇᴇᴅTᴇsᴛ​"