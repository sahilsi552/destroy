

from .. import db



welcomedb = db.welcome_text

welcomest=db.welcome.stats

async def get_welcome(chat_id: int) -> str:
    text = await welcomedb.find_one({"chat_id": chat_id})
    if not text:
        return ""
    return text["text"]


async def set_welcome(chat_id: int, text: str):
    return await welcomedb.update_one(
        {"chat_id": chat_id}, {"$set": {"text": text}}, upsert=True
    )


async def del_welcome(chat_id: int):
    return await welcomedb.delete_one({"chat_id": chat_id})
# 

async def get_welcome_status(chat_id):
    status = await welcomest.find_one({"chat_id": chat_id})
    if status:
        return status.get("welcome", "on")
    return "on"

async def set_welcome_status(chat_id, state):
    await welcomest.update_one(
        {"chat_id": chat_id},
        {"$set": {"welcome": state}},
        upsert=True
    )
