import re
from pyrogram import filters
from config import BANNED_USERS,SUPPORT_GRP , START_IMG,SUDOERS
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    CallbackQuery,
)
from pyrogram.enums import ChatType
from pyrogram.errors import MessageNotModified
from Merisa import QuantamBot as app, HELPABLE
from ..utils import (
    page_load,
    
)
from Merisa.inline import (private_panel,
    start_pannel,
    private_help_panel,admin_help_panel
)




@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(_, query: CallbackQuery):
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)

    if mod_match:
        try:
            module = mod_match.group(1)
            text = (
                "**{} --{}--** :\n".format("Hᴇʟᴘ Fᴏʀ", HELPABLE[module].__MODULE__)
                + HELPABLE[module].__HELP__
            )
            key = InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="back"),
                  InlineKeyboardButton(text="Cʟᴏsᴇ", callback_data="closeforce")]]
            )
            await query.message.edit(text=text, reply_markup=key)
        except MessageNotModified:
            return
    elif prev_match:
        try:
            current_page = int(prev_match.group(1))
            buttons = page_load(current_page - 1, HELPABLE, "help")
            await query.message.edit(
                f"ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ @{SUPPORT_GRP}\n\n๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except MessageNotModified:
            return
    elif next_match:
        try:
            current_page = int(next_match.group(1))
            buttons = page_load(current_page + 1, HELPABLE, "help")
            await query.message.edit(
                f"ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ @{SUPPORT_GRP}\n\n๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except MessageNotModified:
            return


@app.on_callback_query(filters.regex("home_help"))
async def back(_, query: CallbackQuery):
    try:
        buttons = page_load(0, HELPABLE, "help")
        await query.message.edit(
            f"ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ @{SUPPORT_GRP}\n\n๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except MessageNotModified:
        return


@app.on_callback_query(filters.regex("back"))
async def back(_, query: CallbackQuery):
    try:
        buttons = page_load(0, HELPABLE, "help")
        await query.message.edit(
            f"ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ @{SUPPORT_GRP}\n\n๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except MessageNotModified:
        return


@app.on_callback_query(filters.regex("semxx"))
async def back(_, query: CallbackQuery):
    try:
        buttons = private_panel()
        await query.message.edit(
            text=f"""ʜᴇʏ {query.from_user.mention}
**ᴛʜɪs ɪs {app.mention} ᴀ ᴛᴇʟᴇɢʀᴀᴍ  ʙᴏᴛ ᴡɪᴛʜ ꜱᴏᴍᴇ ᴀᴡᴇꜱᴏᴍᴇ ꜰᴇᴀᴛᴜʀᴇꜱ....
ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs :**""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except MessageNotModified:
        return


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
async def help_cmd(_, msg: Message):
    try:
        await msg.delete()
    except:
        pass
    
    if msg.from_user.id in SUDOERS:
        buttons=admin_help_panel()
        await msg.reply_photo(START_IMG,caption="» Wʜᴇʀᴇ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴏᴘᴇɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ?",reply_markup=InlineKeyboardMarkup(buttons))
    else:    
        buttons = page_load(0, HELPABLE, "help")
        await msg.reply_photo(START_IMG,
            f"ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\n๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
async def help_cmd(_, msg: Message):
    try:
        await msg.delete()
    except:
        pass
    
    
    buttons=admin_help_panel()
    await msg.reply_photo(START_IMG,caption="» Wʜᴇʀᴇ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴏᴘᴇɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴍᴇɴᴜ?",reply_markup=InlineKeyboardMarkup(buttons))
    