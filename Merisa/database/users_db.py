from .. import db

usersdb = db.users


async def is_served_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_served_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list


async def save_id(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return usersdb.insert_one({"user_id": user_id})
    # return f'added {user_id} to database successfully'
async def remove_served_users(user_id: int):
    is_served = await is_served_user(user_id)
    if not is_served:
        return
    return await usersdb.delete_one({"user_id":user_id})
