import secureme  
import hashlib  
import logging  
from pyrogram import filters  
from Merisa import  QuantamBot  

# 🛡️ Configure Logging  
logging.basicConfig(level=logging.INFO)  

# 🎯 User-Defined Variables and Configuration  
DEFAULT_HASH_ALGORITHM = 'sha256'  # You can expand with new algorithms like 'md5', 'sha1', etc.  

# 💬 Command Functionality Descriptions  
COMMANDS = {  
    "encrypt": "Converts the specified text into an encrypted format 🔒",  
    "decrypt": "Decodes the previously encrypted text back into its original form 🔓",  
    "hash": "Generates a hash of the specified text using the default algorithm 🔑",  
    "reverse": "Reverses the specified text 🔄"  
}  

# 🚀 Message Processing Functions  
@QuantamBot.on_message(filters.command("encrypt"))  
async def encrypt(bot, message):  
    if len(message.command) < 2:  
        return await message.reply_text(f"Usage: `/encrypt <text>` 🔒\n\n{COMMANDS['encrypt']}")  
    m = message.text.split(' ', 1)[1]  
    try:  
        encrypted_text = secureme.encrypt(m)  
        await message.reply_text(f"🔒 **Encrypted Text:**\n`{encrypted_text}`")  
    except Exception as e:  
        logging.error(f"Encryption error: {e}")  
        await message.reply_text(f"❌ **Error in encryption:** {e}")  

@QuantamBot.on_message(filters.command("decrypt"))  
async def decrypt(bot, message):  
    if len(message.command) < 2:  
        return await message.reply_text(f"Usage: `/decrypt <encrypted_text>` 🔓\n\n{COMMANDS['decrypt']}")  
    m = message.text.split(' ', 1)[1]  
    try:  
        decrypted_text = secureme.decrypt(m)  
        await message.reply_text(f"🔓 **Decrypted Text:**\n`{decrypted_text}`")  
    except Exception as e:  
        logging.error(f"Decryption error: {e}")  
        await message.reply_text(f"❌ **Error in decryption:** {e}")  

@QuantamBot.on_message(filters.command("hash"))  
async def hash_text(bot, message):  
    if len(message.command) < 2:  
        return await message.reply_text(f"Usage: `/hash <text>` 🔑\n\n{COMMANDS['hash']}")  
    m = message.text.split(' ', 1)[1]  
    try:  
        hashed = hashlib.new(DEFAULT_HASH_ALGORITHM, m.encode()).hexdigest()  
        await message.reply_text(f"🔑 **{DEFAULT_HASH_ALGORITHM.upper()} Hash:**\n`{hashed}`")  
    except Exception as e:  
        logging.error(f"Hashing error: {e}")  
        await message.reply_text(f"❌ **Error in hashing:** {e}")  

@QuantamBot.on_message(filters.command("reverse"))  
async def reverse_text(bot, message):  
    if len(message.command) < 2:  
        return await message.reply_text(f"Usage: `/reverse <text>` 🔄\n\n{COMMANDS['reverse']}")  
    m = message.text.split(' ', 1)[1]  
    try:  
        reversed_text = m[::-1]  
        await message.reply_text(f"🔄 **Reversed Text:**\n`{reversed_text}`")  
    except Exception as e:  
        logging.error(f"Reversing error: {e}")  
        await message.reply_text(f"❌ **Error in reversing text:** {e}")  

# 📜 Module Meta Information  
# __MODULE__ = "🔒 Encrypt"  
# __HELP__ = """  

# """