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
                [[InlineKeyboardButton(text="๏ ʙᴀᴄᴋ ๏", callback_data="back"),
                  InlineKeyboardButton(text="๏ Cʟᴏsᴇ ๏", callback_data="closeforce")]]
            )
            await query.message.edit(text=text, reply_markup=key)
        except MessageNotModified:
            return
    elif prev_match:
        try:
            current_page = int(prev_match.group(1))
            buttons = page_load(current_page - 1, HELPABLE, "help")
            await query.message.edit(
                f"ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ [Sᴜᴘᴘᴏʀᴛ](https://t.me/daisysupport_0)\n\n๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except MessageNotModified:
            return
    elif next_match:
        try:
            current_page = int(next_match.group(1))
            buttons = page_load(current_page + 1, HELPABLE, "help")
            await query.message.edit(
                f"ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ [Sᴜᴘᴘᴏʀᴛ](https://t.me/daisysupport_0)\n\n๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except MessageNotModified:
            return


@app.on_callback_query(filters.regex("home_help"))
async def back(_, query: CallbackQuery):
    try:
        await query.answer("Here is the main help menu")
        buttons = page_load(0, HELPABLE, "help")
        await query.message.edit(
            f"ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ [Sᴜᴘᴘᴏʀᴛ](https://t.me/daisysupport_0)\n\n๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except MessageNotModified:
        return


@app.on_callback_query(filters.regex("back"))
async def back(_, query: CallbackQuery):
    try:
        buttons = page_load(0, HELPABLE, "help")
        await query.answer("Here is the main help menu")
        await query.message.edit(
            f"ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴄᴀᴛᴇɢᴏʀʏ ғᴏʀ ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴɴᴀ ɢᴇᴛ ʜᴇʟᴩ.\nᴀsᴋ ʏᴏᴜʀ ᴅᴏᴜʙᴛs ᴀᴛ [Sᴜᴘᴘᴏʀᴛ](https://t.me/daisysupport_0)\n\n๏ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except MessageNotModified:
        return


@app.on_callback_query(filters.regex("semxx"))
async def back(_, query: CallbackQuery):
    try:
        buttons = private_panel()
        await query.message.edit(
            text=f"""Hello {query.from_user.mention} 🥀.

๏ This is {app.mention} 🖤!
➻ The most comprehensive Telegram bot for managing and protecting group chats from spammers and rule-breakers.

──────────────────
๏ Click the help button to learn about my modules and commands.""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    except MessageNotModified:
        return



