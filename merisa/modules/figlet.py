from pyrogram import filters  
import asyncio  
import pyfiglet  
from random import choice  
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery  
from .. import QuantamBot as Client  


DEFAULT_FONT = "standard"  # Default font if none provided  

# 🎩 Figlet Generation Function: Transforms text into Figlet! Wow!  
def generate_figlet(text, font=None):  
    try:  
        all_fonts = pyfiglet.FigletFont.getFonts()  
        chosen_font = font if font in all_fonts else choice(all_fonts)  
        figlet_text = pyfiglet.figlet_format(text, font=chosen_font)  
        keyboard = InlineKeyboardMarkup([  
            [InlineKeyboardButton(text="Change ✏️", callback_data="figlet"),  
             InlineKeyboardButton(text="Close ❌", callback_data="close_reply")],  
            [InlineKeyboardButton(text="Random Style 🎲", callback_data="random_style"),  
             InlineKeyboardButton(text="List Fonts 📜", callback_data="list_fonts")]  
        ])  
        return figlet_text, keyboard  
    except Exception as e:  
        return str(e), None  

# 💌 Command to Create Figlet Text  
@Client.on_message(filters.command("figlet"))  
async def figlet_command(bot, message):  
    try:  
        text = message.text.split(' ', 1)[1]  
    except IndexError:  
        return await message.reply_text("Example:\n\n`/figlet Merisa` ⠀🔤")  
    
    figlet_text, keyboard = generate_figlet(text)  
    await message.reply_text(f"Here's your Figlet:\n<pre>{figlet_text}</pre>", quote=True, reply_markup=keyboard)  
    # Store the text in the message for later retrieval in callbacks
    message.text = text  

# 📜 Command to List Available Fonts  
@Client.on_message(filters.command("figletfonts"))  
async def list_fonts_command(bot, message):  
    fonts = pyfiglet.FigletFont.getFonts()  
    await message.reply_text(f"Available Fonts:\n\n{', '.join(fonts)}")  

# 🎨 Command to List Available Styles  
@Client.on_message(filters.command("figletstyles"))  
async def list_styles_command(bot, message):  
    styles = ["standard", "slant", "3-d", "3x5", "5lineoblique", "alphabet", "banner", "doh", "isometric1"]  
    await message.reply_text(f"Available Styles:\n\n{', '.join(styles)}")  

# 🔄 Callback Query Handler for Figlet  
@Client.on_callback_query(filters.regex("figlet"))  
async def figlet_callback(client, query: CallbackQuery):  
    text = query.message.text.split(' ', 1)[1]  # Retrieve the original text from the message  
    try:  
        figlet_text, keyboard = generate_figlet(text)  
        await query.message.edit_text(f"Here's your Figlet:\n<pre>{figlet_text}</pre>", reply_markup=keyboard)  
    except Exception as e:  
        await query.message.reply_text(str(e))  

# 🎲 Callback Query Handler for Random Style  
@Client.on_callback_query(filters.regex("random_style"))  
async def random_style_callback(client, query: CallbackQuery):  
    try:  
        figlet_text, keyboard = generate_figlet("random text!")  # Placeholder text for the fun of it!  
        await query.message.edit_text(f"Here's your Figlet:\n<pre>{figlet_text}</pre>", reply_markup=keyboard)  
    except Exception as e:  
        await query.message.reply_text(str(e))  

# 📜 Callback Query Handler for Listing Fonts  
@Client.on_callback_query(filters.regex("list_fonts"))  
async def list_fonts_callback(client, query: CallbackQuery):  
    fonts = pyfiglet.FigletFont.getFonts()  
    await query.message.reply_text(f"Available Fonts:\n\n{', '.join(fonts)}")  

