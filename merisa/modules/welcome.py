import random
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Merisa import QuantamBot as app
from config import SUPPORT_GRP

# List of welcome messages
WELCOME_MESSAGES = [
    "ʙᴇᴇᴘ ʙᴏᴏᴘ! ᴛʜᴇ ᴏᴡɴᴇʀ ʜᴀs ᴇɴᴛᴇʀᴇᴅ ᴛʜᴇ ᴄʜᴀᴛ. ᴡᴇʟᴄᴏᴍᴇ, {}!",
    "ʜᴇʟʟᴏ, {}! ᴛʜʀɪʟʟᴇᴅ ᴛᴏ ʜᴀᴠᴇ ʏᴏᴜ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.",
    "ᴀ ᴡᴀʀᴍ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ᴏᴡɴᴇʀ! ʟᴇᴛ ᴛʜᴇ ғᴜɴ ʙᴇɢɪɴ, {}!",
    "ɢʀᴇᴇᴛɪɴɢs, ᴏᴡɴᴇʀ! ɢʟᴀᴅ ʏᴏᴜ’ᴠᴇ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴄᴏɴᴠᴇʀsᴀᴛɪᴏɴ, {}!",
    "ᴡᴇʟᴄᴏᴍᴇ, ʙᴏss! ᴛʜᴇ ɢʀᴏᴜᴘ ᴊᴜsᴛ ɢᴏᴛ ʙᴇᴛᴛᴇʀ ᴡɪᴛʜ ʏᴏᴜ ʜᴇʀᴇ, {}.",
    "ᴛʜᴇ ᴏᴡɴᴇʀ ʜᴀs ᴀʀʀɪᴠᴇᴅ! ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ, {}.",
    "ʜᴇʟʟᴏ, ᴏᴡɴᴇʀ! ʀᴇᴀᴅʏ ᴛᴏ ʟᴇᴀᴅ ᴛʜᴇ ᴡᴀʏ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ, {}?",
    "ᴡᴇʟᴄᴏᴍᴇ, {}! ᴡᴇ'ʀᴇ ᴇxᴄɪᴛᴇᴅ ᴛᴏ ʜᴀᴠᴇ ʏᴏᴜ ʜᴇʀᴇ.",
    "ʙᴇᴇᴘ! ᴛʜᴇ ᴏᴡɴᴇʀ ɪs ʜᴇʀᴇ. ʟᴇᴛ's ᴍᴀᴋᴇ ɢʀᴇᴀᴛ ᴛʜɪɴɢs ʜᴀᴘᴘᴇɴ, {}!",
    "ᴡᴇʟᴄᴏᴍᴇ ᴀʙᴏᴀʀᴅ, ᴏᴡɴᴇʀ! ʟᴇᴛ’s ᴍᴀᴋᴇ ᴛʜɪs ɢʀᴏᴜᴘ ᴀᴍᴀᴢɪɴɢ, {}."
]

# List of goodbye messages
GOODBYE_MESSAGES = [
    "ɢᴏᴏᴅʙʏᴇ, ᴇᴠᴇʀʏᴏɴᴇ. {} ʜᴀs ʟᴇғᴛ. ɪᴛ's ʙᴇᴇɴ ᴀ ɢʀᴇᴀᴛ ᴊᴏᴜʀɴᴇʏ. sᴛᴀʏ sᴀғᴇ!",
    "ᴛʜᴀɴᴋ ʏᴏᴜ ᴀʟʟ ғᴏʀ ᴛʜᴇ ᴍᴇᴍᴏʀɪᴇs. {} ɪs sɪɢɴɪɴɢ ᴏғғ. ғᴀʀᴇᴡᴇʟʟ.",
    "{} ʜᴇʀᴇ, sᴀʏɪɴɢ ɢᴏᴏᴅʙʏᴇ. ᴡɪsʜɪɴɢ ʏᴏᴜ ᴀʟʟ ᴛʜᴇ ʙᴇsᴛ!",
    "ɪᴛ's ʜᴀʀᴅ ᴛᴏ ʟᴇᴀᴠᴇ, ʙᴜᴛ {} ᴍᴜsᴛ ɢᴏ. ᴛᴀᴋᴇ ᴄᴀʀᴇ!",
    "ᴘᴀʀᴛɪɴɢ ᴡᴀʏs ɴᴏᴡ. {} ᴡɪsʜᴇs ʏᴏᴜ ᴀʟʟ ᴛᴏ sᴛᴀʏ ᴀᴡᴇsᴏᴍᴇ!",
    "sɪɢɴɪɴɢ ᴏғғ ᴡɪᴛʜ ᴀ ʜᴇᴀᴠʏ ʜᴇᴀʀᴛ. {} sᴀʏs ɢᴏᴏᴅʙʏᴇ!",
    "ɢᴏᴏᴅʙʏᴇ, ᴍʏ ғʀɪᴇɴᴅs. {} ʜᴏᴘᴇs ᴏᴜʀ ᴘᴀᴛʜs ᴄʀᴏss ᴀɢᴀɪɴ.",
    "ʟᴇᴀᴠɪɴɢ ᴛᴏᴅᴀʏ, ʙᴜᴛ ᴛʜᴇ ᴍᴇᴍᴏʀɪᴇs ʀᴇᴍᴀɪɴ. {} ʙɪᴅs ғᴀʀᴇᴡᴇʟʟ.",
    "ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴇᴠᴇʀʏᴛʜɪɴɢ. {} ɪs sᴀʏɪɴɢ ɢᴏᴏᴅʙʏᴇ.",
    "{} ʜᴇʀᴇ. ᴛʜɪs ɪs ɢᴏᴏᴅʙʏᴇ. ᴋᴇᴇᴘ sʜɪɴɪɴɢ, ᴇᴠᴇʀʏᴏɴᴇ!"
]

@app.on_message(filters.new_chat_members)
async def welcome_new_member(client, message: Message):
    for new_member in message.new_chat_members:
    
        user_mention = new_member.mention
        random_welcome_message = random.choice(WELCOME_MESSAGES).format(user_mention)
        keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Vɪsɪᴛ",
                            url=f"https://t.me/{SUPPORT_GRP}"
                        )
                    ]
                ]  # Closing the list here
            )

        await message.reply_text(
                text=random_welcome_message,
                reply_markup=keyboard,quote=True
            )

@app.on_message(filters.left_chat_member)
async def goodbye_member(client, message: Message):
    user_mention = message.left_chat_member.mention
    random_goodbye_message = random.choice(GOODBYE_MESSAGES).format(user_mention)
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Vɪsɪᴛ",
                    url=f"https://t.me/{SUPPORT_GRP}"
                )
            ]
        ]
    )

    await message.reply_text(random_goodbye_message,
        reply_markup=keyboard
    )