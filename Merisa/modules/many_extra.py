
from pyrogram import filters,Client,idle
from config import *
import requests
from .. import QuantamBot
from pyrogram.enums import ChatAction, ParseMode, ChatType
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM,CallbackQuery
import random
from MukeshAPI import api
from Merisa.utils.button_help import *

async def question(message):
    """Extract the text from a message.
    
    Arguments:
    message -- the message to extract text from
    
    Returns:
    text -- the extracted text from the message, if available; otherwise, a response to provide a query
    
    """
    if message.reply_to_message:
        text = message.reply_to_message.text
    try:
        text = message.text.split(None, 1)[1]
    except IndexError:
        return await message.reply("Please provide a query too")
    
    return text

@QuantamBot.on_message(filters.command("bhagwatgita"))
async def bhagwat_gita_intro(b, message):
    await b.send_chat_action(message.chat.id, ChatAction.TYPING)
    if message.reply_to_message:
        text = message.reply_to_message.text
    try:
        text = message.text.split(None, 1)[1]
        
        print(text)
    except IndexError:
        text=int(random.randint(1,18))

    output = await message.reply("<i>Processing...</i>", quote=True)
    try:
        search_result = api.bhagwatgita(text,text)["chapter_intro"]
        await output.edit_text(search_result)
    except Exception as e:
        await output.edit_text(e)









# @QuantamBot.on_message(filters.command("randomquotes"))
# async def randquotes_res(b,message):
  
#     output = await message.reply("<i>Processing...</i>", quote=True)
#     try:
#         api.endpoint="randomquotes"
#         search_result = api.search2()
#         await output.edit_text(f"{search_result["results"]}")
#     except Exception as e:
#         await output.edit_text(e)
# @QuantamBot.on_message(filters.command("joke"))
# async def joke_res(b,message):
  
#     output = await message.reply("<i>Processing...</i>", quote=True)
#     try:
#         api.endpoint="joke"
#         search_result = api.search2()
#         await output.edit_text(f"**`{search_result["results"]}`**")
#     except Exception as e:
#         await output.edit_text(e)

# @QuantamBot.on_message(filters.command(["hateshyari","hate"]))
# async def randquotes_res(b,message):
  
#     output = await message.reply("<i>Processing...</i>", quote=True)
#     try:
#         api.endpoint="hateshayri"
#         search_result = api.search2()
#         await output.edit_text(f"**{search_result["results"]}**")
#     except Exception as e:
#         await output.edit_text(e)

# @QuantamBot.on_message(filters.command(["love","loveshayri"]))
# async def love_res(b,message):
  
#     output = await message.reply("<i>Processing...</i>", quote=True)
#     try:
#         api.endpoint="loveshayri"
#         search_result = api.search2()
#         await output.edit_text(f"**{search_result["results"]}**")
#     except Exception as e:
#         await output.edit_text(e)


@QuantamBot.on_message(filters.command(["meme","memes"]))
async def meme_res(b,message):
    await b.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
  
    output = await message.reply("<i>Processing...</i>", quote=True)
    try:

        search_result = api.meme()["url"]
        await output.delete()
        caption=search_result["title"]
        await message.reply_photo(photo=search_result,caption=caption)
    except Exception as e:
        await output.edit_text(e)

# @QuantamBot.on_message(filters.command(["flirt"]))
# async def flirt_res(b,message):
  
#     output = await message.reply("<i>Processing...</i>", quote=True)
#     try:
#         api.endpoint="flirt"
#         search_result = api.search4(api_key=API_KEY)
#         await output.edit_text(f"**{search_result["results"][0]}**")
#     except Exception as e:
#         await output.edit_text(e)

# @QuantamBot.on_message(filters.command("randomimg"))
# async def random_img(b, message):
#     if message.reply_to_message:
#         text = message.reply_to_message.text
#     try:
#         text = message.text.split(None, 1)[1]
#         print(text)
#     except IndexError:
#         text=int(random.randint(200,2000))

#     output = await message.reply("<i>Processing...</i>", quote=True)
#     try:
#         api.endpoint="randomimg"
#         search_result = api.search(query=text)
#         await output.edit_text(f"{search_result["results"]}")
#     except Exception as e:
#         await output.edit_text(e)

# @QuantamBot.on_message(filters.command("test"))
# async def testcode(b,m):
#     await m.reply("hii")

def imdb_search(text):
    api.endpoint = "imdb"
    search_result = api.imdb(text)
    results = search_result.get("results", [])
    for result in results:
        description = result.get("description")
        movie_image = result.get("movie_image")
        movie_actors = result.get("movie_actors", [])
        movie_trailer = result.get("movie_trailer", {}).get("url")
        movie_review_rating = result.get("movie_review_rating") 
        movie_name = result.get("movie_name") 
        output_text = f"""
**Movie Name**: `{movie_name}`
**Movie Review Rating:** `{movie_review_rating}` ⭐️ 
**Movie Actors:** `{", ".join(movie_actors)}`
**Description:** `{description}`"""
    return output_text,movie_trailer,movie_image


@QuantamBot.on_message(filters.command(["imdb"]))
async def imdb_res(b, message):
    await b.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
    text = await question(message)
    res=imdb_search(text)
    # print(res)
    output = await message.reply("<i>Processing...</i>", quote=True)
    try:
        
        reply_markup = IKM([
            [IKB("Movie Trailer", url=res[1])]])
        await output.delete()
        await message.reply_photo(photo=f"{res[2]}", caption=res[0],reply_markup=reply_markup)
    except Exception as e:
        await message.reply_text(str(e))

