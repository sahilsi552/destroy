
from pyrogram import filters,Client 
from Merisa.userbot.admins import is_admin

@Client.on_message(filters.command("kick", prefixes=["."] ) &~ filters.private & filters.me)
async def  kickuser(b,message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]
    
    # hm = await Client.get_users(user)
    try:
        await b.ban_chat_member(message.chat.id,user)
        await b.unban_chat_member(message.chat.id,user)
        await message.reply_text(f"kicked")
    except Exception as e:
        await message.reply_text(f"failed due to {e}")
        
@Client.on_message(filters.command("dkick", prefixes=["."] ) &~ filters.private & filters.me)
async def  dkickuser(b,message):
    await message.delete()
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]
    
    # hm = await Client.get_users(user)
    try:
        await b.ban_chat_member(message.chat.id,user)
        await b.unban_chat_member(message.chat.id,user)
        # await message.reply_text(f"kicked")
    except Exception as e:
        await message.reply_text(f"failed due to {e}")
