from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from Merisa import QuantamBot as app


def private_help_panel():
    buttons = [
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴘ ᴍᴇɴᴜ", url=f"https://t.me/{app.username}?start=help"
            )
        ]
    ]
    return buttons

def admin_help_panel():
    buttons = [
        [InlineKeyboardButton(
            "ᴏᴘᴇɴ ʜᴇʀᴇ",callback_data="back")],
        
        [
            InlineKeyboardButton(
                text="ᴏᴘᴇɴ ɪɴ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ", url=f"https://t.me/{app.username}?start=help"
            )
        ]
    ]
    return buttons

def served_panel():
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴠᴇʀɪғʏ ʏᴏᴜʀsᴇʟғ", url=f"https://t.me/{app.username}?start"
            )
        ]
    ]
    return buttons


close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="closeforce")
                ]    
            ]
        )