# -----------CREDITS -----------
# telegram : @Mr_Sukkun
# github : noob-mukesh
from pyrogram import filters,Client 
import random

@Client.on_message(filters.command("react",".")& filters.me)
async def react_msg(b, message):
    await message.delete()
    if message.reply_to_message:
        reactions = message.reply_to_message.text
    try:
        reactions = message.text.split(None, 1)[1]
        print(reactions)
    except IndexError:
        reactions = random.choice(['👍', '❤️', '🔥', '🥰', '👏', '😁', '🤔', '😱', '🎉', '🤩', '🙏', '👌', '🕊', '🤡', '🥴', '😍', '🐳', '❤️‍🔥', '🌚', '💯', '🤣', '🤗', '🫡', '✍️', '🤝', '🙈', '😇', '👀', '👨‍💻', '👻', '💋', '💔', '🤨', '😐', '⚡️', '🏆', '😢', '🍾', '🍓', '😈', '😴', '🤓', '🎃', '🎅', '🎄', '☃️', '💅', '🤪', '🆒', '🗿', '💘', '😘', '💊', '🦄', '🙉', '🙊', '😎', '👾', '🤷‍♂️', '🤷', '🤷‍♀️', '😡', '🥱'])

    try:
       
        CHAT_ID=message.chat.id
        msg_id=(message.reply_to_message.id)
    
        await b.send_reaction(chat_id =CHAT_ID,message_id=msg_id, emoji=reactions, big=True)
    except Exception as e:
        print(e)