from .. import db



tokendb = db.tokendb
async def token_is_user(user_id: int) -> bool:
    user = await tokendb.find_one({"user_id": user_id})
    if user:
        return user["api"]
    else:
        return False


async def token_add_user(user_id: int, api: str):
    user = await token_is_user(user_id)
    if not user:
        return await tokendb.insert_one({"user_id": user_id, "api": api})


async def token_remove_user(user_id: int, api: str):
    user = await token_is_user(user_id)
    if not user:
        return
    return await tokendb.delete_one({"user_id": user_id, "api": api})