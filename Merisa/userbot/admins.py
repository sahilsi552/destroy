# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-Client
from pyrogram import filters,Client
from pyrogram.types import ChatPrivileges,ChatPermissions
from pyrogram.types import *
from pyrogram.enums import ChatMembersFilter

# Check if user has admin rights
async def is_administrator(user_id: int, message,client):
    admin = False
    administrators = []
    async for m in app.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m)
    for user in administrators:
        if user.user.id == user_id:
            admin = True
            break
    return admin
async def is_admin(user_id: int, message):
    
    administrators = []
    async for m in app.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m)
    if user_id in administrators:
        return True     
    else:
        return False
 
 
    
@Client.on_message(filters.command(["ban"], prefixes=["."] )  & ( filters.group | filters.channel) & filters.me )
async def  banuser(b,message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    try:
    
        await b.ban_chat_member(message.chat.id,user)
        
        await message.reply_text(f"banned by {message.from_user.mention} \n banned to {hm.mention}")
    except Exception as e:
        await message.reply_text(f"failed due to {e}")
        
@Client.on_message(filters.command(["mute"], prefixes=["."] )  & ( filters.group | filters.channel) & filters.me )
async def  mute_user(b,message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    try:
    
        await b.restrict_chat_member(message.chat.id, user,
    ChatPermissions(can_send_messages=False))
        
        await message.reply_text(f"mute by {message.from_user.mention} \n muted to {hm.mention}")
    except Exception as e:
        await message.reply_text(f"failed due to {e}")
        
@Client.on_message(filters.command(["unmute"], prefixes=["."] )  & ( filters.group | filters.channel) & filters.me )
async def  mute_user(b,message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]

    try:
    
        await b.restrict_chat_member(message.chat.id, user,
    ChatPermissions(can_send_messages=True))
        
        await message.reply_text(f"unmute by {message.from_user.mention} \n unmuted to {hm.mention}")
    except Exception as e:
        await message.reply_text(f"failed due to {e}")
        
@Client.on_message(filters.command(["staff","admins"], prefixes=["."] ) & ( filters.group | filters.channel) & filters.me)

async def get_staff(b,message):
    administrators = []
    async for m in b.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m)
    staff = "Admins:\n"
    for user,x in enumerate(administrators):
        staff += f"{user.user.mention}\n"
    await message.reply_text(staff)
        
@Client.on_message(filters.command("unban", prefixes=["."] ) & ( filters.group | filters.channel) & filters.me)
async def  unbanuser(b,message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user = message.text.split(None, 1)[1]
    
    # hm = await Client.get_users(user)
    try:
        await b.unban_chat_member(message.chat.id,user)
        await message.reply_text(f"unbanned by {message.from_user.mention} \n unbanned to {hm.mention}")
    except Exception as e:
        await message.reply_text(f"failed due to {e}")

@Client.on_message(filters.command("leave", prefixes=["."] )  & ( filters.group | filters.channel)& filters.me )
async def  leaveuser(b,message):
    
    chat= message.chat.id
    if len(message.command) != 1:
        chat = message.text.split(None, 1)[1]
        
    try:
        await message.reply_text(f"left chat 🤧 : {chat}")
        await b.leave_chat(chat,delete=True)
    except Exception as e:
        await message.reply_text(f" failed due to {e}")

@Client.on_message(filters.command("setgpic",".")  & ( filters.group | filters.channel) & filters.me)
async def  setgpic(b,message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")

    if message.reply_to_message.photo:
        img = await message.reply_to_message.download()
    try:
        await b.set_chat_photo(message.chat.id,img)
    except Exception as e:
        await message.reply_text(f"failed due to {e}")


@Client.on_message(filters.command("settitle", prefixes=["."] )  & ( filters.group | filters.channel)& filters.me)
async def  set_chat_title(b,message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    if message.reply_to_message:
        msg = message.reply_to_message.text
    elif not message.reply_to_message and len(message.command) != 1:
        msg = message.text.split(None, 1)[1]
    
    chat=message.chat.id
    try:
        await b.set_chat_title(chat,msg)
    except Exception as e:
        await message.reply_text(f"failed due to {e}")


@Client.on_message(filters.command("setdesc", prefixes=["."] )  & ( filters.group | filters.channel) & filters.me)
async def  set_chat_description(b,message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    if message.reply_to_message:
        msg = message.reply_to_message.text
    elif not message.reply_to_message and len(message.command) != 1:
        msg = message.text.split(None, 1)[1]
    
    chat=message.chat.id
    try:
        await b.set_chat_description(chat,msg)
    except Exception as e:
        await message.reply_text(f"failed due to {e}")
@Client.on_message(filters.command("delchannel", prefixes=["."] )  & ( filters.group | filters.channel)& filters.me )
async def  delete_channel(b,message):
    if  not is_admin(message.from_user.id,message):
        return await message.reply_text("u cant do that")
    if message.reply_to_message:
        msg = message.reply_to_message.text
    elif not message.reply_to_message and len(message.command) != 1:
        msg = message.text.split(None, 1)[1]
    
    chat=message.chat.id
    try:
        await b.delete_channel(chat,msg)
    except Exception as e:
        await message.reply_text(f"failed due to {e}")
        
        
        
        # 
        
@Client.on_message(filters.command("stats", ".")& filters.me)
async def stats(_, message):
    chats = []
    async for dialog in _.get_dialogs():
        chats.append(int(dialog.chat.id))
    
    await message.reply(f"{len(chats)} chats")

@Client.on_message(filters.command("del", ".")&~ filters.private & filters.me)
async def del_msg(_, msg: Message):
    repliedmsg = msg.reply_to_message.id
    await msg.delete()

    if not repliedmsg:
        return await ctx.reply_text("reply to msg from u want delete ")
    await _.delete_messages(
                    chat_id=msg.chat.id,
                    message_ids=repliedmsg,
                    revoke=True,  # For both sides
                )
    

    
@Client.on_message(filters.command("purge", ".")&~ filters.private & filters.me)
async def purge(_, ctx: Message):
    try:
        repliedmsg = ctx.reply_to_message
        await ctx.delete()

        if not repliedmsg:
            return await ctx.reply_text("reply to msg from u want delete ")

        cmd = ctx.command
        if len(cmd) > 1 and cmd[1].isdigit():
            purge_to = repliedmsg.id + int(cmd[1])
            purge_to = min(purge_to, ctx.id)
        else:
            purge_to = ctx.id

        chat_id = ctx.chat.id
        message_ids = []
        del_total = 0

        for message_id in range(
            repliedmsg.id,
            purge_to,
        ):
            message_ids.append(message_id)

            # Max message deletion limit is 100
            if len(message_ids) == 100:
                await _.delete_messages(
                    chat_id=chat_id,
                    message_ids=message_ids,
                    revoke=True,  # For both sides
                )
                del_total += len(message_ids)
                # To delete more than 100 messages, start again
                message_ids = []

        # Delete if any messages left
        if len(message_ids) > 0:
            await _.delete_messages(
                chat_id=chat_id,
                message_ids=message_ids,
                revoke=True,
            )
            del_total += len(message_ids)
        await ctx.reply_text("purge completed")
    except Exception as err:
        await ctx.reply_text(f"ERROR: {err}")
        
        
        
# Promote Members
@Client.on_message(filters.command(["promote", "fullpromote"], ".")&~ filters.private & filters.me)

async def promoteFunc(client, message):
    try:
        if message.reply_to_message:
            user = message.reply_to_message.from_user.id
        elif not message.reply_to_message and len(message.command) != 1:
            user = message.text.split(None, 1)[1]
        
        umention = (await client.get_users(user)).mention
    except:
        return await message.reply(("invalid id"))
    if not user:
        return await message.reply_text(("user_not_found"))
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if user == client.me.id:
        return await message.reply_text(("promote_self_err"))
    if not bot:
        return await message.reply_text("I'm not an admin in this chat.")
    if not bot.can_promote_members:
        return await message.reply_text("no_promote_perm")
    try:
        if message.command[0][0] == "f":
            await message.chat.promote_member(
                user_id=user,
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
            return await message.reply_text("full promoted")

        await message.chat.promote_member(
            user_id=user,
            privileges=ChatPrivileges(
                can_change_info=False,
                can_invite_users=bot.can_invite_users,
                can_delete_messages=bot.can_delete_messages,
                can_restrict_members=bot.can_restrict_members,
                can_pin_messages=bot.can_pin_messages,
                can_promote_members=False,
                can_manage_chat=bot.can_manage_chat,
                can_manage_video_chats=bot.can_manage_video_chats,
            ),
        )
        await message.reply_text("promoted")
    except Exception as err:
        await message.reply_text(err)
        
        
        
# Promote Members
@Client.on_message(filters.command(["demote"], ".")&~ filters.private & filters.me)

async def demoteFunc(client, message):
    try:
        if message.reply_to_message:
            user = message.reply_to_message.from_user.id
        elif not message.reply_to_message and len(message.command) != 1:
            user = message.text.split(None, 1)[1]
        
        umention = (await client.get_users(user)).mention
    except:
        return await message.reply(("invalid id"))
    try:
        await message.chat.promote_member(user_id=user,
            privileges=ChatPrivileges(
                can_change_info=False,
                can_invite_users=False,
                can_delete_messages=False,
                can_restrict_members=False,
                can_pin_messages=False,
                can_promote_members=False,
                can_manage_chat=False,
                can_manage_video_chats=False,
            ))
        return await message.reply_text("demoted")

       
    except Exception as err:
        await message.reply_text(err)
