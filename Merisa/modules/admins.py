import asyncio
from contextlib import suppress
from config import OWNER_ID
from pyrogram import filters
from pyrogram.errors import ChatWriteForbidden, ChatAdminRequired
from pyrogram.types import (
    ChatPermissions,
    ChatPrivileges,
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from Merisa import QuantamBot as app
from ..utils import *


__MODULE__ = "Aᴅᴍɪɴs"
__HELP__ = """
/ban - ʙᴀɴ ᴀ ᴜsᴇʀ
/dban - ʙᴀɴ ᴀɴᴅ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ
/tban - ʙᴀɴ ᴀ ᴜsᴇʀ ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴛɪᴍᴇ
/unban - ᴜɴʙᴀɴ ᴀ ᴜsᴇʀ
/setting - ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ғᴇᴀᴛᴜʀᴇs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ
/warn - ᴡᴀʀɴ ᴀ ᴜsᴇʀ
/dwarn - ᴡᴀʀɴ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ
/rmwarns - ʀᴇᴍᴏᴠᴇ ᴀʟʟ ᴡᴀʀɴɪɴɢ ᴏғ ᴀ ᴜsᴇʀ
/warns - sʜᴏᴡ ᴡᴀʀɴɪɴɢ ᴏғ ᴀ ᴜsᴇʀ
/kick - ᴋɪᴄᴋ ᴀ ᴜsᴇʀ
/dkick - ᴋɪᴄᴋ ᴀɴᴅ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ
/purge - ᴘᴜʀɢᴇ ᴍᴇssᴀɢᴇs
/purge [n] - ᴘᴜʀɢᴇ "n" ɴᴜᴍʙᴇʀ ᴏғ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ
/del - ᴅᴇʟᴇᴛᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ
/promote - ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ
/fullpromote - ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ ᴡɪᴛʜ ᴀʟʟ ʀɪɢʜᴛs
/demote - ᴅᴇᴍᴏᴛᴇ ᴀ ᴍᴇᴍʙᴇʀ
/pin - ᴘɪɴ ᴀ ᴍᴇssᴀɢᴇ
/mute - ᴍᴜᴛᴇ ᴀ ᴜsᴇʀ
/tmute - ᴍᴜᴛᴇ ᴀ ᴜsᴇʀ ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴛɪᴍᴇ
/unmute - ᴜɴᴍᴜᴛᴇ ᴀ ᴜsᴇʀ
/ban_ghosts - ʙᴀɴ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs
"""


@app.on_message(filters.command("purge") & ~filters.private)
@adminsOnly("can_delete_messages")
async def purgeFunc(_, message: Message):
    try:
        repliedmsg = message.reply_to_message
        try:
            await message.delete()
        except:
            pass
        if not repliedmsg:
            return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘᴜʀɢᴇ ғʀᴏᴍ !")
        cmd = message.command
        if len(cmd) > 1 and cmd[1].isdigit():
            purge_to = repliedmsg.id + int(cmd[1])
            if purge_to > message.id:
                purge_to = message.id
        else:
            purge_to = message.id
        chat_id = message.chat.id
        message_ids = []
        for message_id in range(repliedmsg.id, purge_to):
            message_ids.append(message_id)
            if len(message_ids) == 500:
                await app.delete_messages(
                    chat_id=chat_id,
                    message_ids=message_ids,
                    revoke=True,  # For both sides
                )
                message_ids = []

        if len(message_ids) > 0:
            await app.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True,
            )
    except AttributeError:
        pass
    except ChatWriteForbidden:
        pass
    except ChatAdminRequired:
        await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** :\n`can_delete_messages`"
        )


@app.on_message(filters.command(["kick", "dkick"]) & ~filters.private)
@adminsOnly("can_restrict_members")
async def kickFunc(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ !")
        if user_id == app.id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴋɪᴄᴋ ᴍʏsᴇʟғ !")
        if user_id in OWNER_ID:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴋɪᴄᴋ ᴍʏ ᴏᴡɴᴇʀ !")
        if user_id in (await list_admins(message.chat.id)):
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴋɪᴄᴋ ᴀɴ ᴀᴅᴍɪɴ !")
        mention = (await app.get_users(user_id)).mention
        msg = f"""
**ᴋɪᴄᴋᴇᴅ ᴜsᴇʀ:** {mention}
**ᴋɪᴄᴋᴇᴅ ʙʏ:** {message.from_user.mention if message.from_user else 'ᴀɴᴏɴ'}
**ʀᴇᴀsᴏɴ:** {reason or 'ɴᴏ ʀᴇᴀsᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ'}
"""
        if message.command[0][0] == "d":
            await message.reply_to_message.delete()
        await message.chat.ban_member(user_id)
        await message.reply("🪦")
        await message.reply_text(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except AttributeError:
        pass
    except ChatWriteForbidden:
        pass
    except ChatAdminRequired:
        await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** : `can_restrict_members`"
        )


@app.on_message(filters.command(["ban", "dban", "tban"]) & ~filters.private)
@adminsOnly("can_restrict_members")
async def banFunc(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        user_id, reason = await extract_user_and_reason(message, sender_chat=True)
        if not user_id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ !")
        if user_id == app.id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ʙᴀɴ ᴍʏsᴇʟғ !")
        if user_id in OWNER_ID:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴋɪᴄᴋ ᴍʏ ᴏᴡɴᴇʀ !")
        if user_id in (await list_admins(message.chat.id)):
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ʙᴀɴ ᴀɴ ᴀᴅᴍɪɴ !")
        try:
            mention = (await app.get_users(user_id)).mention
        except IndexError:
            mention = (
                message.reply_to_message.sender_chat.title
                if message.reply_to_message
                else "ᴀɴᴏɴ"
            )
        msg = (
            f"**ʙᴀɴɴᴇᴅ ᴜsᴇʀ:** {mention}\n"
            f"**ʙᴀɴɴᴇᴅ ʙʏ:** {message.from_user.mention if message.from_user else 'ᴀɴᴏɴ'}\n"
        )
        if message.command[0][0] == "d":
            await message.reply_to_message.delete()
        if message.command[0] == "tban":
            split = reason.split(None, 1)
            time_value = split[0]
            temp_reason = split[1] if len(split) > 1 else ""
            temp_ban = await time_converter(message, time_value)
            msg += f"**ʙᴀɴɴᴇᴅ ғᴏʀ:** {time_value}\n"
            if temp_reason:
                msg += f"**ʀᴇᴀsᴏɴ:** {temp_reason}"
            with suppress(AttributeError):
                if len(time_value[:-1]) < 3:
                    await message.chat.ban_member(user_id, until_date=temp_ban)
                    await message.reply_text(msg)
                else:
                    await message.reply_text("ʏou ᴄᴀɴ'ᴛ ᴜsᴇ ᴍᴏʀᴇ ᴛʜᴀɴ 99 !")
            return
        if reason:
            msg += f"**ʀᴇᴀsᴏɴ:** {reason}"
        await message.chat.ban_member(user_id)
        await message.reply_animation("🪦")
        await message.reply_text(msg)
    except AttributeError:
        pass
    except ChatWriteForbidden:
        pass
    except ChatAdminRequired:
        await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** : `can_restrict_members`"
        )


@app.on_message(filters.command("unban") & ~filters.private)
@adminsOnly("can_restrict_members")
async def unban_func(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        reply = message.reply_to_message
        if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
            return await message.reply_text("ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜɴʙᴀɴ ᴀ ᴄʜᴀɴɴᴇʟ !")
        if len(message.command) == 2:
            user = message.text.split(None, 1)[1]
        elif len(message.command) == 1 and reply:
            user = message.reply_to_message.from_user.id
        else:
            return await message.reply_text(
                "ᴘʀᴏᴠɪᴅᴇ ᴀ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴛᴏ ᴜɴʙᴀɴ !"
            )
        await message.chat.unban_member(user)
        umention = (await app.get_users(user)).mention
        await message.reply_text(f"ᴜɴʙᴀɴɴᴇᴅ ! {umention}")
    except AttributeError:
        pass
    except ChatWriteForbidden:
        pass
    except ChatAdminRequired:
        await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** : `can_restrict_members`"
        )


@app.on_message(filters.command(["del", "delete"]) & ~filters.private)
@adminsOnly("can_delete_messages")
async def deleteFunc(_, message: Message):
    try:
        if not message.reply_to_message:
            return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴅᴇʟᴇᴛᴇ ɪᴛ !")
        await message.reply_to_message.delete()
        await message.delete()
    except AttributeError:
        pass
    except ChatWriteForbidden:
        pass
    except ChatAdminRequired:
        await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** : `can_delete_messages`"
        )


@app.on_message(filters.command(["promote"]) & ~filters.private)
@adminsOnly("can_promote_members")
async def promoteFunc(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ !")
        bot = (await app.get_chat_member(message.chat.id, app.id)).privileges
        if user_id == app.id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴘʀᴏᴍᴏᴛᴇ ᴍʏsᴇʟғ !")
        if not bot:
            return await message.reply_text("ɪ'ᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ !")
        if not bot.can_promote_members:
            return await message.reply_text("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !")
        umention = (await app.get_users(user_id)).mention

        await message.chat.promote_member(
            user_id=user_id,
            privileges=ChatPrivileges(
                can_change_info=False,
                can_invite_users=bot.can_invite_users,
                can_delete_messages=bot.can_delete_messages,
                can_restrict_members=False,
                can_pin_messages=bot.can_pin_messages,
                can_promote_members=False,
                can_manage_chat=bot.can_manage_chat,
                can_manage_video_chats=bot.can_manage_video_chats,
            ),
        )
        await message.reply_text(f"ᴘʀᴏᴍᴏᴛᴇᴅ ! {umention}")
    except AttributeError:
        pass
    except ChatAdminRequired:
        return await message.reply_text("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !")


@app.on_message(filters.command(["fullpromote", "fpromote"]) & ~filters.private)
@ownerOnly("can_restrict_members")
@adminsOnly("can_promote_members")
async def promoteFunc(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ !")
        bot = (await app.get_chat_member(message.chat.id, app.id)).privileges
        if user_id == app.id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴘʀᴏᴍᴏᴛᴇ ᴍʏsᴇʟғ !")
        if not bot:
            return await message.reply_text("ɪ'ᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ !")
        if not bot.can_promote_members:
            return await message.reply_text("I ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ғᴜʟʟ ᴘᴇʀᴍɪssɪᴏɴs !")
        umention = (await app.get_users(user_id)).mention

        await message.chat.promote_member(
            user_id=user_id,
            privileges=ChatPrivileges(
                can_change_info=bot.can_change_info,
                can_invite_users=bot.can_invite_users,
                can_delete_messages=bot.can_delete_messages,
                can_restrict_members=bot.can_restrict_members,
                can_pin_messages=bot.can_pin_messages,
                can_promote_members=bot.can_promote_members,
                can_manage_chat=bot.can_manage_chat,
                can_manage_video_chats=bot.can_manage_video_chats,
            ),
        )
        await message.reply_text(f"ғᴜʟʟʏ ᴘʀᴏᴍᴏᴛᴇᴅ ! {umention}")
    except AttributeError:
        pass
    except ChatAdminRequired:
        return await message.reply_text("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ғᴜʟʟ ᴘᴇʀᴍɪssɪᴏɴs !")


@app.on_message(filters.command("demote") & ~filters.private)
@adminsOnly("can_promote_members")
async def demote(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ !")
        if user_id == app.id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴅᴇᴍᴏᴛᴇ ᴍʏsᴇʟғ !")
        await message.chat.promote_member(
            user_id=user_id,
            privileges=ChatPrivileges(
                can_change_info=False,
                can_invite_users=False,
                can_delete_messages=False,
                can_restrict_members=False,
                can_pin_messages=False,
                can_promote_members=False,
                can_manage_chat=False,
                can_manage_video_chats=False,
            ),
        )
        umention = (await app.get_users(user_id)).mention
        await message.reply_text(f"ᴅᴇᴍᴏᴛᴇᴅ ! {umention}")
    except AttributeError:
        pass
    except ChatAdminRequired:
        return await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** : `can_promote_members`"
        )


@app.on_message(filters.command(["pin", "unpin"]) & ~filters.private)
@adminsOnly("can_pin_messages")
async def pin(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if not message.reply_to_message:
            return await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴘɪɴ/ᴜɴᴘɪɴ ɪᴛ !")
        r = message.reply_to_message
        if message.command[0][0] == "u":
            await r.unpin()
            return await message.reply_text(
                f"**ᴜɴᴘɪɴɴᴇᴅ [ᴛʜɪs]({r.link}) ᴍᴇssᴀɢᴇ !**",
                disable_web_page_preview=True,
            )
        await r.pin(disable_notification=True)
        await message.reply(
            f"**ᴘɪɴɴᴇᴅ [ᴛʜɪs]({r.link}) ᴍᴇssᴀɢᴇ !**", disable_web_page_preview=True
        )
        msg = "ᴘʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇ: ~ " + f"[ᴄʜᴇᴄᴋ, {r.link}]"
        filter_ = dict(type="text", data=msg)
        await save_filter(message.chat.id, "~pinned", filter_)
    except AttributeError:
        pass
    except ChatWriteForbidden:
        pass
    except ChatAdminRequired:
        await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** : `can_pin_messages`"
        )


@app.on_message(filters.command(["mute", "tmute"]) & ~filters.private)
@adminsOnly("can_restrict_members")
async def mute(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        user_id, reason = await extract_user_and_reason(message)
        if not user_id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ !")
        if user_id == app.id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴍᴜᴛᴇ ᴍʏsᴇʟғ !")
        if user_id in OWNER_ID:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴍᴜᴛᴇ ᴍʏ ᴏᴡɴᴇʀ !")
        if user_id in (await list_admins(message.chat.id)):
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴍᴜᴛᴇ ᴀɴ ᴀᴅᴍɪɴ !")
        mention = (await app.get_users(user_id)).mention
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ᴜɴᴍᴜᴛᴇ", callback_data=f"unmute_{user_id}")]]
        )
        msg = (
            f"**ᴍᴜᴛᴇᴅ ᴜsᴇʀ:** {mention}\n"
            f"**ᴍᴜᴛᴇᴅ ʙʏ:** {message.from_user.mention if message.from_user else 'ᴀɴᴏɴ'}\n"
        )
        if message.command[0] == "tmute":
            split = reason.split(None, 1)
            time_value = split[0]
            temp_reason = split[1] if len(split) > 1 else ""
            temp_mute = await time_converter(message, time_value)
            msg += f"**ᴍᴜᴛᴇᴅ ғᴏʀ:** {time_value}\n"
            if temp_reason:
                msg += f"**ʀᴇᴀsᴏɴ:** {temp_reason}"
            try:
                if len(time_value[:-1]) < 3:
                    await message.chat.restrict_member(
                        user_id,
                        permissions=ChatPermissions(),
                        until_date=temp_mute,
                    )
                    await message.reply_animation("https://fonts.gstatic.com/s/e/notoemoji/latest/1f92b/512.gif")
                    await message.reply_text(msg, reply_markup=keyboard)
                else:
                    await message.reply_text("ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴍᴏʀᴇ ᴛʜᴀɴ 99 !")
            except AttributeError:
                pass
            return
        if reason:
            msg += f"**ʀᴇᴀsᴏɴ:** {reason}"
        await message.chat.restrict_member(user_id, permissions=ChatPermissions())
        await message.reply_text(msg, reply_markup=keyboard)
    except AttributeError:
        pass
    except ChatWriteForbidden:
        pass
    except ChatAdminRequired:
        await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** : `can_restrict_members`"
        )


@app.on_message(filters.command("unmute") & ~filters.private)
@adminsOnly("can_restrict_members")
async def unmute(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        user_id = await extract_user(message)
        if not user_id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ !")
        await message.chat.unban_member(user_id)
        umention = (await app.get_users(user_id)).mention
        await message.reply_text(f"ᴜɴᴍᴜᴛᴇᴅ ! {umention}")
    except AttributeError:
        pass
    except ChatWriteForbidden:
        pass
    except ChatAdminRequired:
        await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** : `can_restrict_members`"
        )


@app.on_message(filters.command("ban_ghosts") & ~filters.private)
@adminsOnly("can_restrict_members")
async def ban_deleted_accounts(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        chat_id = message.chat.id
        deleted_users = []
        banned_users = 0
        m = await message.reply("ғɪɴᴅɪɴɢ ɢʜᴏsᴛs !")
        async for i in app.get_chat_members(chat_id):
            if i.user.is_deleted:
                deleted_users.append(i.user.id)
        if len(deleted_users) > 0:
            for deleted_user in deleted_users:
                try:
                    await message.chat.ban_member(deleted_user)
                except Exception:
                    pass
                banned_users += 1
            await m.edit(f"ʙᴀɴɴᴇᴅ {banned_users} ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs !")
        else:
            await m.edit("ᴛʜᴇʀᴇ ᴀʀᴇ ɴᴏ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ɪɴ ᴛʜɪs ᴄʜᴀᴛ !")
    except AttributeError:
        pass
    except ChatWriteForbidden:
        pass
    except ChatAdminRequired:
        await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** : `can_restrict_members`"
        )


@app.on_message(filters.command(["warn", "dwarn"]) & ~filters.private)
@adminsOnly("can_restrict_members")
async def warn_user(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        user_id, reason = await extract_user_and_reason(message)
        chat_id = message.chat.id
        if not user_id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ !")
        if user_id == app.id:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴡᴀʀɴ ᴍʏsᴇʟғ !")
        if user_id in OWNER_ID:
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴡᴀʀɴ ᴍʏ ᴏᴡɴᴇʀ !")
        if user_id in (await list_admins(chat_id)):
            return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ᴡᴀʀɴ ᴀɴ ᴀᴅᴍɪɴ !")
        user, warns = await asyncio.gather(
            app.get_users(user_id), get_warn(chat_id, await int_to_alpha(user_id))
        )
        mention = user.mention
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ʀᴇᴍᴏᴠᴇ ᴡᴀʀɴ", callback_data=f"unwarn_{user_id}"
                    )
                ]
            ]
        )
        if warns:
            warns = warns["warns"]
        else:
            warns = 0
        if message.command[0][0] == "d":
            await message.reply_to_message.delete()
        if warns >= 2:
            await message.chat.ban_member(user_id)
            await message.reply_text(
                f"ɴᴜᴍʙᴇʀ ᴏғ ᴡᴀʀɴs ᴏғ {mention} ᴇxᴄᴇᴇᴅᴇᴅ !\nʙᴀɴɴᴇᴅ !"
            )
            await remove_warns(chat_id, await int_to_alpha(user_id))
        else:
            warn = {"warns": warns + 1}
            msg = f"""
**ᴡᴀʀɴᴇᴅ ᴜsᴇʀ:** {mention}
**ᴡᴀʀɴᴇᴅ ʙʏ:** {message.from_user.mention if message.from_user else 'ᴀɴᴏɴ'}
**ʀᴇᴀsᴏɴ:** {reason or 'ɴᴏ ʀᴇᴀsᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ'}
**ᴡᴀʀɴs:** {warns + 1}/3
""" 
            await message.reply_animation("https://fonts.gstatic.com/s/e/notoemoji/latest/1f198/512.gif")
            await message.reply_text(msg, reply_markup=keyboard)
            await add_warn(chat_id, await int_to_alpha(user_id), warn)
    except AttributeError:
        pass
    except ChatWriteForbidden:
        pass
    except ChatAdminRequired:
        await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** : `can_restrict_members`"
        )


@app.on_message(filters.command(["rmwarns", "removewarn"]) & ~filters.private)
@adminsOnly("can_restrict_members")
async def remove_warnings(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if not message.reply_to_message:
            return await message.reply_text(
                "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴀ ᴜsᴇʀ's ᴡᴀʀɴɪɴɢ !"
            )
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
        chat_id = message.chat.id
        warns = await get_warn(chat_id, await int_to_alpha(user_id))
        if warns:
            warns = warns["warns"]
        if warns == 0 or not warns:
            await message.reply_text(f"{mention} ʜᴀᴠᴇ ɴᴏ ᴡᴀʀɴɪɴɢ's !")
        else:
            await remove_warns(chat_id, await int_to_alpha(user_id))
            await message.reply_text(f"ʀᴇᴍᴏᴠᴇᴅ ᴡᴀʀɴɪɴɢ's ᴏғ {mention} !")
    except AttributeError:
        pass
    except ChatWriteForbidden:
        pass
    except ChatAdminRequired:
        await message.reply_text(
            "ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs !\n\n**ᴘᴇʀᴍɪssɪᴏɴ** : `can_restrict_members`"
        )


@app.on_message(filters.command("warns") & ~filters.private)
async def check_warns(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text("ɪ ᴄᴀɴ'ᴛ ғɪɴᴅ ᴛʜᴀᴛ ᴜsᴇʀ !")
    warns = await get_warn(message.chat.id, await int_to_alpha(user_id))
    mention = (await app.get_users(user_id)).mention
    if warns:
        warns = warns["warns"]
        return await message.reply_text(f"{mention} ʜᴀs {warns}/3 ᴡᴀʀɴɪɴɢ's !")
    else:
        return await message.reply_text(f"{mention} ʜᴀs ɴᴏ ᴡᴀʀɴɪɴɢ's !")


@app.on_callback_query(filters.regex("unwarn_"))
async def remove_warning(_, cq: CallbackQuery):
    from_user = cq.from_user
    chat_id = cq.message.chat.id
    permissions = await member_permissions(chat_id, from_user.id)
    permission = "can_restrict_members"
    if permission not in permissions:
        return await cq.answer(
            "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ !",
            show_alert=True,
        )
    user_id = cq.data.split("_")[1]
    warns = await get_warn(chat_id, await int_to_alpha(user_id))
    if warns:
        warns = warns["warns"]
    if not warns or warns == 0:
        return await cq.answer("ᴜsᴇʀ ʜᴀs ɴᴏ ᴡᴀʀɴɪɴɢ's !")
    warn = {"warns": warns - 1}
    await add_warn(chat_id, await int_to_alpha(user_id), warn)
    text = cq.message.text.markdown
    text = f"~~{text}~~\n\n"
    text += f"__ᴡᴀʀɴ ʀᴇᴍᴏᴠᴇᴅ ʙʏ {from_user.mention}__"
    await cq.message.edit(text)


@app.on_callback_query(filters.regex("unmute_"))
async def remove_warning(_, cq: CallbackQuery):
    from_user = cq.from_user
    chat_id = cq.message.chat.id
    permissions = await member_permissions(chat_id, from_user.id)
    permission = "can_restrict_members"
    if permission not in permissions:
        return await cq.answer(
            "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ !",
            show_alert=True,
        )
    user_id = cq.data.split("_")[1]
    await cq.message.chat.unban_member(user_id)
    text = cq.message.text.markdown
    text = f"~~{text}~~\n\n"
    text += f"__ᴜɴᴍᴜᴛᴇᴅ ʙʏ {from_user.mention}__"
    await cq.message.edit(text)