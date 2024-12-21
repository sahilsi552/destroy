import asyncio
import importlib
from config import START_IMG,OWNER_ID,LOG_GROUP_ID
from pyrogram import idle
from Merisa.misc import sudo
from Merisa import LOGGER, QuantamBot,HELPABLE
from Merisa.modules import ALL_MODULES


async def Merisa_start():
    try:
        await sudo()
        await QuantamBot.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        imported_module=importlib.import_module("Merisa.modules." + all_module)
        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            imported_module.__MODULE__ = imported_module.__MODULE__
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                HELPABLE[imported_module.__MODULE__.lower()] = imported_module
    # LOGGER.info(HELPABLE)
    LOGGER.info(f"@{QuantamBot.username} Started.")
    # await QuantamBot.send_photo(LOG_GROUP_ID,START_IMG,"I am Alive")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Merisa_start())
    LOGGER.info("Stopping Merisa bot")
