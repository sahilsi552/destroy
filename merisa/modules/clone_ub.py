import re
import logging,asyncio
from pymongo import MongoClient
from pyrogram import Client, filters
from Merisa import QuantamBot as bot
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid
from config import API_ID, API_HASH,MONGO_DATABASE_URI as MONGO_DB_URI,OWNER_ID,SUDOERS

mongo_client = MongoClient(MONGO_DB_URI)

from Merisa.utils.database import add_sudo, remove_sudo

mongo_db = mongo_client["quantum_ub_db"]
mongo_collection = mongo_db["clonedb"]

@bot.on_message(filters.command("clone") & filters.private)
async def on_clone(client, message):  
    try:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        string_token =message.command[1]
        # print(string_token)
        
        bots = list(mongo_collection.find())
        string_tokens = None 

        for bot in bots:
            string_tokens = bot['string']
            # print("31",string_tokens)

        if string_tokens == string_token:
            await message.reply_text("➢ ᴛʜɪs Assɪsᴛᴀɴᴛ UsᴇʀBᴏᴛ  ɪs ᴀʟʀᴇᴀᴅʏ ᴄʟᴏɴᴇᴅ  use /startub command if client is off ")
            return
        try:
            ai = Client(
                f"{user_name}", API_ID, API_HASH,
                session_string=string_token,
                plugins={"root": "Merisa.userbot"},
            )
            
            await ai.start()
            
            bot = await ai.get_me()
            details = {
                'is_bot':False,
                'user_id': user_id,
                'name': bot.first_name,
                'string': string_token,
                'username': bot.username
            }
            mongo_collection.insert_one(details)
            await message.reply_text(f"<b>sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʟᴏɴᴇᴅ ʏᴏᴜʀ Assɪsᴛᴀɴᴛ UsᴇʀBᴏᴛ : @{bot.username}.\n\nʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ sᴇᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ɪɴ ʏᴏᴜʀ ᴄʟᴏɴᴇᴅ ʙᴏᴛ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ sᴛᴀʀᴛ Assɪsᴛᴀɴᴛ UsᴇʀBᴏᴛ using  .start for more type .help</b>")
        except BaseException as e:
            logging.exception(f"Error while cloning ub. {e}")
            await message.reply_text(f"⚠️ <b>Assɪsᴛᴀɴᴛ UsᴇʀBᴏᴛ  Error:</b>\n\n<code>{e}</code>\n\n**Kindly forward this message to owner to get assistance.**")
    except Exception as e:
        logging.exception("Error while handling message.")

@bot.on_message(filters.command("deleteclone") & filters.private)
async def delete_cloned_bot(client, message):
    try:
        if message.reply_to_message:
            string_token = message.reply_to_message.text
        elif not message.reply_to_message and len(message.command) != 1:
            string_token = message.text.split(None, 1)[1]
        # string_token = message.command[1]
        else:
            await message.reply_text("➢ ꜱᴇɴᴅ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ʏᴏᴜʀ Assɪsᴛᴀɴᴛ session \nᴇx ː- /deleteclone <ʏᴏᴜʀ session>.")
    
        # print(string_token)
        user=message.from_user.id
        cloned_bot = mongo_collection.find_one({"string": string_token})
        print(cloned_bot)
        if cloned_bot:
            mongo_collection.delete_one({"string": string_token})
            await message.reply_text(" ➢ ᴛʜᴇ ᴄʟᴏɴᴇᴅ Assɪsᴛᴀɴᴛ UsᴇʀBᴏᴛ ʜᴀs ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴛʜᴇ ʟɪsᴛ ᴀɴᴅ ɪᴛs ᴅᴇᴛᴀɪʟs ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ᴛʜᴇ ᴅᴀᴛᴀʙᴀsᴇ. ")
    except Exception as e:
        logging.exception("Error while deleting cloned Assɪsᴛᴀɴᴛ UsᴇʀBᴏᴛ {e}.")
        await message.reply_text("An error occurred while deleting the cloned Assɪsᴛᴀɴᴛ UsᴇʀBᴏᴛ .")
@bot.on_message(filters.command("startallub",".") & filters.user(OWNER_ID))

async def startall_botsss(b,m):
    logging.info("Restarting all client........")
    bots = list(mongo_collection.find())
    for bot in bots:
        string_token = bot['string']
        try:
            ai = Client(
                f"{string_token}", API_ID, API_HASH,
                session_string=string_token,
                plugins={"root": "Merisa.userbot"},
            )
            await ai.start()
            
        except Exception as e:
            logging.exception(f"Error while restarting assistant  {string_token}: {e}")
async def restart_bots():
    logging.info("Restarting all client........")
    bots = list(mongo_collection.find())
    for bot in bots:
        string_token = bot['string']
        try:
            ai = Client(
                f"{string_token}", API_ID, API_HASH,
                session_string=string_token,
                plugins={"root": "Merisa.userbot"},
            )
            await ai.start()
            await ai.join_chat("mr_sukkun")
           
        except Exception as e:
            logging.exception(f"Error while restarting assistant: {e}")
@bot.on_message(filters.command("stopallub",".")& filters.user(OWNER_ID))
async def stop_All_ub():
    logging.info("stopping all client........")
    bots = list(mongo_collection.find())
    for bot in bots:
        string_token = bot['string']
        try:
            ai = Client(
                f"{string_token}", API_ID, API_HASH,
                session_string=string_token,
                plugins={"root": "Merisa.userbot"},
            )
            await ai.stop()
            
        except Exception as e:
            logging.exception(f"Error while stopping assistant  {string_token}: {e}")         
@bot.on_message(filters.command("allclient",".") & filters.user(OWNER_ID))
async def akll(b,m):
    bots = list(mongo_collection.find())
    all_client="all client\n"
    for bot in bots:
        all_client+=f"{bot['user_id']} : {bot['name']}\n"
    #     print(bot["user_id"],bot["name"])
    # print(all_client)
    await m.reply(all_client)

@bot.on_message(filters.command("startclient") & filters.private & filters.user(OWNER_ID))
async def start_client_owner(b, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user_id = message.text.split(None, 1)[1]
    
    cloned_bot = mongo_collection.find_one({"user_id": user_id})
    
    if cloned_bot:
        # Retrieve the token string associated with the cloned bot
        token_data = mongo_collection.find_one({"user_id": user_id})
        string_token = token_data.get("string") if token_data else None
        
        # Check if string_token is present
        if string_token:
            try:
                ai = Client(
                    f"{string_token}", API_ID, API_HASH,
                    session_string=string_token,
                    plugins={"root": "Merisa.userbot"},
                )
                # await b.stop()
                await ai.start()
                
                await message.reply("client started use .ping")
            except Exception as e:
                logging.exception(f"Error while restarting assistant {string_token}: {e}")
        else:
            await message.reply("Token not found. Please check your credentials! 🚫")
    else:
        await message.reply("No cloned assistant found for your user ID! 🚫")
@bot.on_message(filters.command("stopclient") & filters.private & filters.user(OWNER_ID))
async def stop_ub_client(b, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
    elif not message.reply_to_message and len(message.command) != 1:
        user_id = message.text.split(None, 1)[1]
    cloned_bot = mongo_collection.find_one({"user_id": user_id})
    
    if cloned_bot:
        # Retrieve the token string associated with the cloned bot
        token_data = mongo_collection.find_one({"user_id": user_id})
        string_token = token_data.get("string") if token_data else None
        
        # Check if string_token is present
        if string_token:
            try:
                ai = Client(
                    f"{string_token}", API_ID, API_HASH,
                    session_string=string_token,
                    plugins={"root": "Merisa.userbot"},
                )
                # await b.stop()
                await ai.stop()

            except Exception as e:
                logging.exception(f"Error while stopping assistant {string_token}: {e}")
        else:
            await message.reply("Token not found. Please check your credentials! 🚫")
    else:
        await message.reply("No cloned assistant found for your user ID! 🚫")
        
@bot.on_message(filters.command("stopub") & filters.private )
async def start_ub(b, message):
    cloned_bot = mongo_collection.find_one({"user_id": message.from_user.id})
    
    if cloned_bot:
        # Retrieve the token string associated with the cloned bot
        token_data = mongo_collection.find_one({"user_id": message.from_user.id})
        string_token = token_data.get("string") if token_data else None
        
        # Check if string_token is present
        if string_token:
            try:
                ai = Client(
                    f"{string_token}", API_ID, API_HASH,
                    session_string=string_token,
                    plugins={"root": "Merisa.userbot"},
                )
                # await b.stop()
                await ai.stop()
                await message.reply("client stopped")

            except Exception as e:
                logging.exception(f"Error while stopping assistant {string_token}: {e}")
        else:
            await message.reply("Token not found. Please check your credentials! 🚫")
    else:
        await message.reply("No cloned assistant found for your user ID! 🚫")
@bot.on_message(filters.command("startub") & filters.private)
async def restartub(b, message):
    cloned_bot = mongo_collection.find_one({"user_id": message.from_user.id})
    
    if cloned_bot:
        # Retrieve the token string associated with the cloned bot
        token_data = mongo_collection.find_one({"user_id": message.from_user.id})
        string_token = token_data.get("string") if token_data else None
        
        # Check if string_token is present
        if string_token:
            try:
                ai = Client(
                    f"{string_token}", API_ID, API_HASH,
                    session_string=string_token,
                    plugins={"root": "Merisa.userbot"},
                )
                # await b.stop()
                await ai.start()
                
                await message.reply("client started use .ping")
            except Exception as e:
                logging.exception(f"Error while restarting assistant {string_token}: {e}")
        else:
            await message.reply("Token not found. Please check your credentials! 🚫")
    else:
        await message.reply("No cloned assistant found for your user ID! 🚫")