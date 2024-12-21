# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import Client,filters
import asyncio
from .. import QuantamBot
from config import OWNER_ID
from Merisa.utils.button_help import *
from pyrogram.types import CallbackQuery
from pyrogram.types import InputMediaVideo

@QuantamBot.on_callback_query(filters.regex("^HELP"))
async def callback_handler(_: Client, query: CallbackQuery):
    try:
        if query.data == "HELP_AI":
            await query.message.edit_text(
                text=AI_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_AFK":
            await query.message.edit(
                text=AFK_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_CODE":
            await query.message.edit_text(
                text=CODE_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_CARBON":
            await query.message.edit(
                text=CARBON_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_COUPLE":
            await query.message.edit(
                text=COUPLES_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_DOWNLOAD":
            await query.message.edit_text(
                text=DOWNLOAD_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_ENCRYPT":
            await query.message.edit(
                text=ENCYRPT_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_ENGLISH":
            await query.message.edit(
                text=ENGLISH_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_INLINE":
            await query.message.edit_text(
                text=INLINE_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_INFO":
            await query.message.edit(
                text=INFO_HELP,
                reply_markup=IKM(HELP_BACK),
            ) 
        elif query.data == "HELP_GAME":
            await query.message.edit(
                text=GAME_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_KARMA":
            await query.message.edit_text(
                text=KARMA_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_LOGO":
            await query.message.edit(
                text=LOGO_HELP,
                reply_markup=IKM(HELP_BACK),
            ) 
        elif query.data == "HELP_NEWS":
            await query.message.edit(
                text=NEWS_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_QUOTE":
            await query.message.edit_text(
                text=QUOTE_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_RANDOM":
            await query.message.edit(
                text=RANDOM_HELP,
                reply_markup=IKM(HELP_BACK),
            ) 
        elif query.data == "HELP_SHORTNER":
            await query.message.edit(
                text=SHORTNER_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_SUDO":
            await query.message.edit_text(
                text=SUDO_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_STICKER":
            await query.message.edit(
                text=STICKER_HELP,
                reply_markup=IKM(HELP_BACK),
            ) 
        elif query.data == "HELP_TOKEN":
            await query.message.edit(
                text=TOKEN_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_TRANS":
            await query.message.edit_text(
                text=TRANS_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_TRUTH":
            await query.message.edit(
                text=TRUTH_HELP,
                reply_markup=IKM(HELP_BACK),
            )   
        elif query.data == "HELP_TOOLS":
            await query.message.edit_text(
                text=TOOLS_HELP,
                reply_markup=IKM(HELP_BACK),
            )
        elif query.data == "HELP_TELEGRAPH":
            await query.message.edit(
                text=TELEGRAPH_HELP,
                reply_markup=IKM(HELP_BACK),
            )    
        elif query.data == "HELP_BACK":
            await query.message.edit(
                text=f"➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ {QuantamBot.mention} ",
                reply_markup=IKM(HELP),
            )
        elif query.data == "HELP":
            await query.message.edit(
                text=f"➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ {QuantamBot.mention} ",
                reply_markup=IKM(HELP),
            )    
        elif query.data == "HELP_source":
            await query.message.edit(SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
        elif query.data == "HELP_hurr":
            await query.edit_message_media(
                media=InputMediaVideo(
                    "https://te.legra.ph/file/9a5019c9245db95e06c79.mp4"
                ),reply_markup=M,
            )
            #await query.answer("Landh lele mera", show_alert=True)
        
        
    except Exception as e:
        print(e)
        # await query.message.forward(OWNER_ID)
        # await query.message.reply(e)
@QuantamBot.on_callback_query(filters.regex("^closeforce"))
async def callback_handler(_: Client, query: CallbackQuery):
    if query.data == "closeforce":
        #await query.answer("deleted")
        await query.message.delete()
@QuantamBot.on_callback_query(filters.regex("^RETURN"))
async def callback_handler(_: Client, query: CallbackQuery):
    if query.data == "RETURN":
        #await query.answer("deleted")
        await query.message.edit(
                text=START,
                reply_markup=IKM(MAIN),
            )    
    
