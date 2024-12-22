# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters,Client
from Merisa.userbot.admins import is_admin

@Client.on_message(filters.command("pin", ".") &~ filters.private & filters.me)
async def pin_msg(_, message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    if message.reply_to_message:
        msg = message.reply_to_message
        try:
            await _.pin_chat_message(message.chat.id,msg.id)
    
            await message.reply(f" pinned msg")
        except Exception as e:
            await message.reply(f"Error: {e}")
        
@Client.on_message(filters.command("unpin", ".") &~ filters.private & filters.me)
async def unpin_msg(client, message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    if message.reply_to_message:
        msg = message.reply_to_message
        try:
            await client.unpin_chat_message(message.chat.id,msg.id)
    
            await message.reply(f" unpinned")
        except Exception as e:
            await message.reply(f"Error: {e}")
            
@Client.on_message(filters.command("unpinall", ".") & filters.me)
async def unpin_all_chat_msg(client, message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    
    try:
        await client.unpin_all_chat_messages(message.chat.id)

        await message.reply(f" unpinned all msgs")
    except Exception as e:
        await message.reply(f"Error: {e}")