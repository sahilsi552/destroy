# -----------CREDITS -----------
# telegram : @Mr_Sukkun
# github : noob-mukesh
from pyrogram import filters
import random
from .. import QuantamBot

@QuantamBot.on_message(filters.command("react"))
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
        # if message.forward_from:
        #     CHAT_ID = message.forward_from.id
        # if message.reply_to_message.forward_from_chat:
        #     CHAT_ID = message.reply_to_message.forward_from_chat.id
        #     msg_id=message.reply_to_message.forward_from_message_id
        # if message.chat.type == ChatType.PRIVATE:
        #     CHAT_ID = message.from_user.id
        # else:
        CHAT_ID=message.chat.id
        msg_id=(message.reply_to_message.id)
        # print(CHAT_ID)
        
        # print(msg_id)
        # print(reactions)
        await b.send_reaction(chat_id =CHAT_ID,message_id=msg_id, emoji=reactions, big=True)
        # await  message.reply("Done!")
        # await message.react(reactions,big=True)
        # await m.react(reactions,big=True)
    except Exception as e:
        print(e)