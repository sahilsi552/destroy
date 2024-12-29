from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Merisa import QuantamBot as app
from config import SUDOERS
from Merisa.database import set_rule, get_rule, remove_rule
from Merisa.utils import adminsOnly

@app.on_message(filters.command("setrules") & ~filters.private)
@adminsOnly("can_change_info")
async def handle_set_rules(client, message):
    if len(message.command) < 2:
        await message.reply_text("Please provide the rules text after the command. 📜")
        return

    rules_text = " ".join(message.command[1:])
    await set_rule(message.chat.id, rules_text)
    await message.reply_text(f"Rules set successfully! 🎉 by {message.from_user.first_name}")

@app.on_message(filters.command("getrules"))
async def handle_get_rules(client, message):
    rules = await get_rule(message.chat.id)
    if not rules:
        await message.reply_text("The admins for this group have not set up rules! 😔 Please ask them to set some.")
        
    else:
        if len(rules)<= 4096:
            await message.reply_text(
            f"The rules for the chat {message.chat.title} is \n {rules}",
           )
        else:
            with open("rules.txt","w") as rules_t:
                rules_t.write(rules)
            await message.reply_document("rules.txt",caption=f"The rules for the chat {message.chat.title}")

@app.on_message(filters.command("removerules") & ~filters.private)
@adminsOnly("can_change_info")
async def handle_remove_rules(client, message):
    await remove_rule(message.chat.id)
    await message.reply_text(f"Rules removed successfully! 🎉 by {message.from_user.first_name}")

__HELP__="""📜✨
**/setrules [your_rules]**  
   Sets the rules for the group chat. You need to provide the rules text right after the command.  
   ⚠️ **Admin permission required!**

   **Example:** /setrules No spamming, be respectful!

/getrules
   Retrieves the current rules for the chat. If no rules are set, you'll be notified!  
   **Example:** Simply type /getrules to see the rules.  

/removerules  
   Removes the existing rules from the group chat.  
   ⚠️ **Admin permission required!**  
   **Example:** Type /removerules to delete the rules.  """
   
__MODULE__="Rᴜʟᴇꜱ"
   