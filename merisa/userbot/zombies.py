
from pyrogram import  filters,Client
from pyrogram.errors import ChatAdminRequired, UserAdminInvalid
from pyrogram.types import ChatPermissions
from pyrogram.enums import ChatMembersFilter
import requests,asyncio


# Check if user has admin rights
async def is_administrator(user_id: int, message,client):
    admin = False
    administrators = []
    async for m in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m)
    for user in administrators:
        if user.user.id == user_id:
            admin = True
            break
    return admin

@Client.on_message(filters.command("zombies", prefixes=["."]) &~ filters.private & filters.me)
async def rm_deletedacc(client, message):
    del_u=0
    
    admin=await is_administrator(message.from_user.id,message,client)
    
    if not admin:
        return await message.reply("Sorry, you are not an admin!")
    
    memek = await message.reply("Removing deleted accounts...")
    participants=[]
    async for member in client.get_chat_members(message.chat.id):
        participants.append(member)
   
    for user in participants:
        if user.user.is_deleted:
            print(user.user.is_deleted)
            try:
                
                await client.ban_chat_member(message.chat.id, user.user.id)
                await client.unban_chat_member(message.chat.id, user.user.id)
                
            except ChatAdminRequired:
                print("Do not have permission to ban in this group")
            except UserAdminInvalid:
                del_u += 1
            await asyncio.sleep(1)
    
    if del_u > 0:
        del_status = f"Cleaned {del_u} Zombies"
    
    await memek.edit(del_status)

@Client.on_message(filters.command("unbanall", prefixes=["."])&~ filters.private & filters.me)
async def rm_deletedacc(client, message):
    # con = message.text.split(" ", 1)[1].lower() if len(message.command) > 1 else ""
    del_u = 0
    
    participants=[]
    async for member in client.get_chat_members(message.chat.id):
        participants.append(member)
    for user in participants:
        try:
          
            await client.unban_chat_member(message.chat.id, user.user.id)
            del_u+=1
        except ChatAdminRequired:
            print("Do not have permission to ban in this group")
        except UserAdminInvalid:
            del_u -= 1
        await asyncio.sleep(1)
    
    if del_u > 0:
        del_status = f"unbanned {del_u} users"
    
    await message.reply_text(del_status)

@Client.on_message(filters.command("unbanall", prefixes=["."]) &~ filters.private & filters.me)
async def rm_deletedacc(client, message):
    # con = message.text.split(" ", 1)[1].lower() if len(message.command) > 1 else ""
    del_u = 0
    
    participants=[]
    async for member in client.get_chat_members(message.chat.id):
        participants.append(member)
    for user in participants:
        try:
            await client.ban_chat_member(message.chat.id, user.user.id)
            del_u+=1
        except ChatAdminRequired:
            print("Do not have permission to ban in this group")
        except UserAdminInvalid:
            del_u -= 1
        await asyncio.sleep(1)
    
    if del_u > 0:
        del_status = f"banned {del_u} users"
    
    await message.reply_text(del_status)
    
    
@Client.on_message(filters.command("kickall", prefixes=["."]) &~ filters.private & filters.me)
async def rm_deletedacc(client, message):
    # con = message.text.split(" ", 1)[1].lower() if len(message.command) > 1 else ""
    del_u = 0
    participants=[]
    async for member in client.get_chat_members(message.chat.id):
        participants.append(member)
    for user in participants:
        try:
            await client.ban_chat_member(message.chat.id, user.user.id)
            await client.unban_chat_member(message.chat.id, user.user.id)
            del_u+=1
        except ChatAdminRequired:
            print("Do not have permission to ban in this group")
        except UserAdminInvalid:
            del_u -= 1
        await asyncio.sleep(1)
    
    if del_u > 0:
        del_status = f"kicked {del_u} users sucessfully "
    
    await message.reply_text(del_status)
