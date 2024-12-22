
from pyrogram import filters,Client
from pyrogram.types import Message
from pyrogram.enums import ChatType


@Client.on_message(filters.command("join",".")& filters.me)
async def join_chatSS(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    try:
        await _.join_chat(chat_id=text)
        await message.reply_text(f"joined chat {text}")
    except Exception as e:
        await message.reply_text(e)
        
@Client.on_message(filters.command("left",".")&~ filters.private & filters.me)
async def left_chatSS(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    try:
        await _.leave_chat(chat_id=text,delete=True)
        await message.reply_text(f"left chat {text}")
    except Exception as e:
        await message.reply_text(e)
        

@Client.on_message(filters.command("pm",".")& filters.me)
async def pm_msg(_, message: Message):
    args=message.text.split(None, 1)[1].strip()
    if not args:return await message.reply("Provide username/id and message")
    user, text = args.split(None, 1)
    if user.startswith("@"):
        user = user[1:]

    try:
        await _.send_message(user, text)
    except Exception as e:
        await message.reply_text(e)

        
        
@Client.on_message(filters.command("botall",".") & filters.me)
async def bot_All_Add(_, message: Message): 
    added=0  
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
        
    try:
        async for dialog in _.get_dialogs():
            if dialog.chat.type==ChatType.GROUP or dialog.chat.type==ChatType.GROUP:
                await _.add_users(dialog.chat.id, text)
                added+=1
        await message.reply_text(f"added  in {added} chats")
    except Exception as e:
        print(e)
        await message.reply_text(e)
    # print(dialog.chat.
    