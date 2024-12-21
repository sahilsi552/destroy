# Standard library imports  
from base64 import b64decode  
from inspect import getfullargspec  
from io import BytesIO  
import logging  

# Third-party imports  
from pyrogram import filters  
from pyrogram.types import Message  

from Merisa import QuantamBot  
from Merisa.utils.http import post  

# Configure logging  
logging.basicConfig(level=logging.INFO)  
logger = logging.getLogger(__name__)  

# User-defined constants  
SCREENSHOT_API = "https://webscreenshot.vercel.app/api"  
DEFAULT_WIDTH = 1920  
DEFAULT_HEIGHT = 1080  
SUCCESS_RESPONSES = ["yes", "y", "1", "true"]  

async def take_screenshot(url: str, full: bool = False, width: int = DEFAULT_WIDTH, height: int = DEFAULT_HEIGHT):  
    """  
    Take a screenshot of the given URL.  
    
    :param url: The URL of the webpage  
    :param full: Capture full page or not  
    :param width: Screenshot width  
    :param height: Screenshot height  
    :return: BytesIO object containing the image  
    """  
    url = "https://" + url if not url.startswith("http") else url  
    payload = {  
        "url": url,  
        "width": width,  
        "height": height,  
        "scale": 1,  
        "format": "jpeg",  
        "full": full  
    }  
    try:  
        data = await post(SCREENSHOT_API, data=payload)  
        if "image" not in data:  
            logger.error("No image found in response")  
            return None  
        image_data = data["image"].replace("data:image/jpeg;base64,", "")  
        file = BytesIO(b64decode(image_data))  
        file.name = "webss.jpg"  
        return file  
    except Exception as e:  
        logger.error(f"Error taking screenshot: {e}")  
        return None  

async def eor(msg: Message, **kwargs):  
    """  
    Edit or reply to a message intelligently based on user/bot.  
    :param msg: The message object to respond to or edit  
    :param kwargs: Additional keyword arguments for the message  
    :return: The sent message object  
    """  
    func = (msg.edit_text if msg.from_user.is_self else msg.reply) if msg.from_user else msg.reply  
    spec = getfullargspec(func.__wrQuantamBoted__).args  
    return await func(**{k: v for k, v in kwargs.items() if k in spec})  

@QuantamBot.on_message(filters.command(["webss", "ss", "webshot"]))  
async def take_ss(_, message: Message):  
    """  
    Command to take a screenshot of a provided URL.  
    """  
    if len(message.command) < 2:  
        return await eor(message, text="❌ Please provide a URL to fetch the screenshot.")  

    url = message.text.split(None, 1)[1]  
    full = False  
    width = DEFAULT_WIDTH  
    height = DEFAULT_HEIGHT  

    if len(message.command) >= 3:  
        full = message.text.split(None, 2)[2].lower().strip() in SUCCESS_RESPONSES  
    if len(message.command) == 4:  
        try:  
            width, height = map(int, message.text.split(None, 3)[3].split('x'))  
        except ValueError:  
            return await eor(message, text="❌ Invalid dimensions. Use format: <width>x<height>")  

    m = await eor(message, text="📸 Capturing screenshot...")  

    try:  
        photo = await take_screenshot(url, full, width, height)  
        if not photo:  
            return await m.edit("❌ Failed to take screenshot.")  

        m = await m.edit("📤 Uploading...")  

        await message.reply_document(photo)  
        await m.delete()  
    except Exception as e:  
        await m.edit(f"❌ Error: {str(e)}")  

@QuantamBot.on_message(filters.command(["webss_status"]))  
async def webss_status(_, message: Message):  
    """  
    Check the status of the screenshot service.  
    """  
    try:  
        response = await post(SCREENSHOT_API + "/status")  
        status_message = "✅ Screenshot service is up and running." if response.get("status") == "ok" else "❌ Screenshot service is currently down."  
        await message.reply(status_message)  
    except Exception as e:  
        await message.reply(f"❌ Error checking status: {str(e)}")  

@QuantamBot.on_message(filters.command(["webss_help"]))  
async def webss_help(_, message: Message):  
    """  
    Display help information for the webshot commands.  
    """  
    help_text = (  
        "🌐 *Website Capture Help* 🌐\n"  
        "✦ /webshot <URL> : Takes a screenshot of the specified webpage.\n"  
        "✦ /webshot <URL> <full> : Takes a full-page screenshot if <full> is 'yes', 'y', '1', or 'true'.\n"  
        "✦ /webshot <URL> <full> <width>x<height> : Takes a screenshot with custom dimensions.\n"  
        "✦ /webss_status : Checks the status of the screenshot service.\n"  
        "✦ /webss_help : Shows this help message."  
    )  
    await message.reply(help_text)  

__HELP__ = """  
*Website Capture:*  
✦ /webshot <URL> : Takes a screenshot of the specified webpage and presents it to you 🌐  
✦ /webshot <URL> <full> : Takes a full-page screenshot if <full> is 'yes', 'y', '1', or 'true'.  
✦ /webshot <URL> <full> <width>x<height> : Takes a screenshot with custom dimensions.  
✦ /webss_status : Checks the status of the screenshot service.  
✦ /webss_help : Shows this help message.  
"""  
__MODULE__ = "🌐 WebPic" 
