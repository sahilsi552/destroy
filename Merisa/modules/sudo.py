# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters
from .. import QuantamBot, LOGGER as logger
from Merisa.utils.button_help import *
from Merisa.database import *
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    UserIsBlocked,
    PeerIdInvalid,
)
import time, asyncio, logging, datetime


@QuantamBot.on_message(filters.command(["bchat","broadcastchat"]) & filters.user(OWNER_ID) & filters.reply)
async def broadcast_handler(bot: Client, m: Message):
    all_chats = await get_served_chats()
    await bot.send_message(
        OWNER_ID,
        f"{m.from_user.mention} or {m.from_user.id} Iꜱ ꜱᴛᴀʀᴛᴇᴅ ᴛʜᴇ Bʀᴏᴀᴅᴄᴀꜱᴛ......",
    )
    broadcast_msg = m.reply_to_message
    sts_msg = await m.reply_text(f"broadcasting ..")
    done = 0
    failed = 0
    success = 0
    start_time = time.time()
    total_chats = len(await get_served_chats())

    for chat in all_chats:
        sts = await send_chat(chat["chat_id"], broadcast_msg)

        if sts == 200:
            success += 1
        else:
            failed += 1
        if sts == 400:
            pass
        done += 1
        if not done % 20:
            await sts_msg.edit(
                f"Bʀᴏᴀᴅᴄᴀꜱᴛ Iɴ Pʀᴏɢʀᴇꜱꜱ: \nTᴏᴛᴀʟ ᴄʜᴀᴛꜱ  {total_chats} \nCᴏᴍᴩʟᴇᴛᴇᴅ: {done} / {total_chats}\nSᴜᴄᴄᴇꜱꜱ: {success}\nFᴀɪʟᴇᴅ: {failed}"
            )
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts_msg.edit(
        f"Bʀᴏᴀᴅᴄᴀꜱᴛ Cᴏᴍᴩʟᴇᴛᴇᴅ: \nCᴏᴍᴩʟᴇᴛᴇᴅ Iɴ {completed_in}.\n\nTᴏᴛᴀʟ ᴄʜᴀᴛꜱ {total_chats}\nCᴏᴍᴩʟᴇᴛᴇᴅ: {done} / {total_chats}\nSᴜᴄᴄᴇꜱꜱ: {success}\nFᴀɪʟᴇᴅ: {failed}"
    )


async def send_chat(chat_id, message):
    try:
        await message.forward(chat_id=int(chat_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return send_msg(chat_id, message)
    except InputUserDeactivated:
        await remove_served_chat(chat_id)
        logger.info(f"{chat_id} : Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ")
        return 400
    except UserIsBlocked:
        await remove_served_chat(chat_id)
        logger.info(f"{chat_id} : Bʟᴏᴄᴋᴇᴅ Tʜᴇ Bᴏᴛ")
        return 400
    except PeerIdInvalid:
        await remove_served_chat(chat_id)
        logger.info(f"{chat_id} : Uꜱᴇʀ Iᴅ Iɴᴠᴀʟɪᴅ")
        return 400
    except Exception as e:
        await remove_served_chat(chat_id)
        logger.error(f"{chat_id} : {e}")
        pass


# broadcast
@QuantamBot.on_message(filters.command("buser") & filters.user(OWNER_ID) & filters.reply)
async def broadcast_handler(bot: Client, m: Message):
    all_users = await get_served_users()
    await bot.send_message(
        OWNER_ID,
        f"{m.from_user.mention} or {m.from_user.id} Iꜱ ꜱᴛᴀʀᴛᴇᴅ ᴛʜᴇ Bʀᴏᴀᴅᴄᴀꜱᴛ......",
    )
    broadcast_msg = m.reply_to_message
    sts_msg = await m.reply_text(f"broadcasting ..")
    done = 0
    failed = 0
    success = 0
    start_time = time.time()
    total_users = len(await get_served_users())
    for user in all_users:
        sts = await send_msg(user["user_id"], broadcast_msg)
        if sts == 200:
            success += 1
        else:
            failed += 1
        if sts == 400:
            pass
        done += 1
        if not done % 20:
            await sts_msg.edit(
                f"Bʀᴏᴀᴅᴄᴀꜱᴛ Iɴ Pʀᴏɢʀᴇꜱꜱ: \nTᴏᴛᴀʟ Uꜱᴇʀꜱ {total_users} \nCᴏᴍᴩʟᴇᴛᴇᴅ: {done} / {total_users}\nSᴜᴄᴄᴇꜱꜱ: {success}\nFᴀɪʟᴇᴅ: {failed}"
            )
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts_msg.edit(
        f"Bʀᴏᴀᴅᴄᴀꜱᴛ Cᴏᴍᴩʟᴇᴛᴇᴅ: \nCᴏᴍᴩʟᴇᴛᴇᴅ Iɴ {completed_in}.\n\nTᴏᴛᴀʟ Uꜱᴇʀꜱ {total_users}\nCᴏᴍᴩʟᴇᴛᴇᴅ: {done} / {total_users}\nSᴜᴄᴄᴇꜱꜱ: {success}\nFᴀɪʟᴇᴅ: {failed}"
    )


async def send_msg(user_id, message):
    try:
        await message.forward(chat_id=int(user_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        await remove_served_users(user_id)
        logger.info(f"{user_id} : Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ")
        return 400
    except UserIsBlocked:
        await remove_served_users(user_id)
        logger.info(f"{user_id} : Bʟᴏᴄᴋᴇᴅ Tʜᴇ Bᴏᴛ")
        return 400
    except PeerIdInvalid:
        await remove_served_users(user_id)
        logger.info(f"{user_id} : Uꜱᴇʀ Iᴅ Iɴᴠᴀʟɪᴅ")
        return 400
    except Exception as e:
        await remove_served_users(user_id)
        logger.error(f"{user_id} : {e}")
        return 500


        
@QuantamBot.on_message(filters.command("logs") & filters.user(OWNER_ID))
async def logss(bot: Client, m: Message):
    await m.reply_document(document="log.txt")
