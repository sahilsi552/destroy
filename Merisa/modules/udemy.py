from Merisa.modules.many_extra import *
import random
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    UserIsBlocked,
    PeerIdInvalid,
)
from pyrogram.enums import ChatType
from .. import QuantamBot
from config import MONGO_DATABASE_URI
client = MongoClient(MONGO_DATABASE_URI)
db = client.udemy
users_collection = db['users']

@QuantamBot.on_message(filters.command("udemy"))
async def start_handler(client, message):
    # if message.chat.type==ChatType.PRIVATE:
    #     
    await message.reply_text("Do you want to receive free udemy courses?", reply_markup=get_inline_keyboard())
    


def get_inline_keyboard():
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='udemy_yes')],
        [InlineKeyboardButton("No", callback_data='udemy_no')]
    ]
    return InlineKeyboardMarkup(keyboard)

@QuantamBot.on_callback_query(filters.regex("^udemy"))
async def button_click_handler(client, callback_query):
    user_id = callback_query.from_user.id
    data = callback_query.data
    chat_id = callback_query.message.chat.id

    if callback_query.message.chat.type == ChatType.PRIVATE:

        if data == 'udemy_yes':
            existing_user= users_collection.find_one({"user_id": user_id})

            if existing_user:
                await callback_query.answer("You are already subscribed 🎉")
            else:
                users_collection.insert_one({"user_id": user_id})
                await callback_query.answer("You will receive bot messages 🎉")

        elif data == 'udemy_no':
            users_collection.delete_one({"user_id": user_id})
            await callback_query.answer("You won't receive bot messages")
        await callback_query.message.delete()

    else:
        if data == 'udemy_yes':
            existing_group = users_collection.find_one({"chat_id": chat_id})

            if existing_group:
                await callback_query.answer("This group/channel is already subscribed 🎉", show_alert=True)
            else:
                users_collection.insert_one({"chat_id": chat_id})
                await callback_query.answer("This group/channel will receive udemy courses 🎉, Thanks for using me", show_alert=True)
        elif data == 'udemy_no':
            users_collection.delete_one({"chat_id": chat_id})
            await callback_query.answer("You won't receive bot messages")
        await callback_query.message.delete()

    # await callback_query.message.delete()


# def search5(self,category):
#     url = f"{self._base_url}/{self.endpoint}?category={category}"
#     headers = {"accept": "application/json"}
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": f"Failed to retrieve. Status code: {response.status_code}"}

# MukeshAPI.search5=search5
scheduler = AsyncIOScheduler()

# async def udemy(client):
#     course=["all","digitalMarketing","others","coding","dataScience","ethicalHacking","design","linguistics"]

#     try:
#         api.endpoint = "udemy"
#         data = api.search5(random.choice(course))

#         results = data['results']
#         courses = results['courses']
        
#         if courses:
#             course = random.choice(courses)
#             course_link = course['courseLink']
#             title = course['title']
#             original_price = course['originalPrice']
#             instructor_name = course['instructorName']
#             language = course['language']
#             description = course['description']
#             category = course['category']
#             image = course['imageLink']
#             caption = f'''**--{title}--**
# **Original Price**: `{original_price}`
# **Instructor Name**: `{instructor_name}`
# **Language**: `{language}`
# **Description**: `{description}`
# **Category**: `{category}`
# 🔥 ʙʏ : {QuantamBot.mention}'''
#             reply_markup = IKM([
#                 [IKB("👩‍🏫 Enroll Now 👨‍🏫", url=course_link)],
#                 [IKB("Aᴅᴅ Mᴇ",url=f"https://t.me/{QuantamBot.username}?startgroup=true")]
#             ])
#             user_ids = []
#             cursor = users_collection.find({'$or': [{'user_id': {'$exists': True}}, {'chat_id': {'$exists': True}}]})
#             for document in cursor:
#                 if 'user_id' in document:
#                     user_ids.append(document['user_id'])
#                 if 'chat_id' in document:
#                     user_ids.append(document['chat_id'])
#             print(user_ids)
#             if len(user_ids)>=1:
#                 try:

#                     for user in user_ids:
#                         await client.send_photo(user,photo=image, caption=caption, reply_markup=reply_markup)
#                 except FloodWait as e:
#                     await asyncio.sleep(e.value)
#                     return await udemy(client)
#                 except InputUserDeactivated:
#                     pass
#                 except UserIsBlocked:
#                     pass
#             else:
#                 print("no,user present whom i can send bitch")
#         else:
#             pass
#     except Exception as e:
#         await client.send_message(OWNER_ID,str(e))

# scheduler.add_job(udemy, 'interval', seconds=300, args=[QuantamBot])
# scheduler.start()
