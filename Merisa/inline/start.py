from Merisa import QuantamBot as app
from config import UPDATE_CHNL 
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup


def start_pannel():
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"
            )
        ]
    ]
    return buttons


def private_panel():
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ],
        [
            InlineKeyboardButton(text="📚 ʜᴇʟᴘ",callback_data="Main_help"),
        ],
        [
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/{UPDATE_CHNL}"),
        ],
    ]
    return buttons

def private_panel2():
    reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="📕 Mᴀɴᴀɢᴇᴍᴇɴᴛ", callback_data="back"),
                        InlineKeyboardButton(text="Mᴜsɪᴄ 🎧", callback_data="Music_")
                    ],
                    [
                        InlineKeyboardButton(text="🌐 Bᴀsɪᴄ ", callback_data="basic_help"),
                        InlineKeyboardButton(text="Exᴘᴇʀᴛ 👮", callback_data="expert_help")
                    ],
                    [
                        InlineKeyboardButton(text="♻️ Aᴅᴠᴀɴᴄᴇ", callback_data="advance_help"),
                        InlineKeyboardButton(text="💡 UsᴇʀBᴏᴛ", callback_data="userbot_help"),
                        
                    ],
                    
                    [ InlineKeyboardButton(text="• Hᴏᴍᴇ •", callback_data="semxx")
                    ],
                ]
            )
    return reply_markup
