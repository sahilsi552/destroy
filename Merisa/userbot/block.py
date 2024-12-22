# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-Client
from pyrogram import filters,Client 
@Client.on_message(filters.command("block", ".") & filters.me)
async def block_user_(b, message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]
    try:
        total = await b.block_user(user_id=user)
    
        await message.reply(f"{user} is blocked")
    except Exception as e:
        await message.reply(f"Error: {e}")
        
@Client.on_message(filters.command("unblock", ".") & filters.me)
async def unblock_user_(_, message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]
    try:
        total = await _.unblock_user(user_id=user)
    
        await message.reply(f"{user} is unblocked")
    except Exception as e:
        await message.reply(f"Error: {e}")