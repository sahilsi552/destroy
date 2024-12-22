from pyrogram import Client, filters

@Client.on_message(filters.command("start",prefixes=".")& filters.me)
async def start(b,m):
    await m.reply(f"hi {m.from_user.first_name} use  .help to get details")
    
@Client.on_message(filters.command(["ping","alive"],prefixes=".")& filters.me)
async def ping(b,m):
    await m.reply(f"hi {m.from_user.first_name} I am Alive")
    
ub_help="""ᴛʜᴇsᴇ ᴀʀᴇ ᴛʜᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴏ ᴜꜱᴇʀʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs:\n⦿.stats : ɢᴇᴛ ᴜꜱᴇʀꜱ ᴄʜᴀᴛ ꜱᴛᴀᴛꜱ.\n⦿.pen : ᴡʀɪᴛᴇ ꜱᴏᴍᴇᴛɪɴɢ..\n⦿.ask : ᴄʜᴀᴛ ɢᴘᴛ ᴀꜱᴋ ᴀɴʏ ᴛʜɪɴɢ.\n⦿.ping : ᴄʜᴇᴄᴋ ꜱᴜᴘᴇʀʙᴀɴ ʙᴏᴛ ᴜᴘ ᴛᴏ ᴛɪᴍᴇ & ʟᴏᴀᴅ.\n⦿.tr : ᴛʀᴀɴꜱʟᴀᴛᴇ ᴀɴʏ ʟᴀɴɢᴜᴀɢᴇ.\n⦿.logo : ɴᴏʀᴍᴀʟ ʟᴏɢᴏ ɢᴇɴ.\n⦿ .info ➠ ɢᴇᴛ ᴜꜱᴇʀɪᴅ / ᴜꜱᴇʀɴᴀᴍᴇ ᴛᴏ ᴜꜱᴇʀɪɴꜰᴏ.\n⦿ .id ➠  🇬🇪🇹 info.\n⦿ .block ➠  ᴛᴏ ʙʟᴏᴄᴋ ᴛᴇʟᴇɢʀᴀᴍ ᴜꜱᴇʀꜱ.\n⦿ .unblock ➠ ᴛᴏ ᴏᴘᴇɴ ᴛʜᴇ ᴜꜱᴇʀ ʏᴏᴜ ʙʟᴏᴄᴋᴇᴅ.\n⦿ .kickme ➠  ʟᴇᴀᴠᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ʙʏ ᴅɪꜱᴘʟᴀʏɪɴɢ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ʜᴀꜱ ʟᴇꜰᴛ ᴛʜɪꜱ ɢʀᴏᴜᴘ, ʙʏᴇ!!\n⦿ .join  ➠ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀᴛ ᴠɪᴀ ᴜꜱᴇʀɴᴀᴍᴇ.\n⦿ .leave  ➠  ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ᴠɪᴀ ᴜꜱᴇʀɴᴀᴍᴇ.\n⦿ .admins ➠  ɢᴇᴛ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ ʟɪꜱᴛꜱ.\n⦿ .zombies ➠  ʙᴀɴ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄ ꜰʀᴏᴍ ɢʀᴏᴜᴘ.\n⦿ .ban / .unban  ➠  ʙᴀɴ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ ᴀɴᴅ ᴜɴʙᴀɴ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ.\n⦿ .mute / .unmute ➠  ᴍᴜᴛᴇ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ ᴀɴᴅ ᴜɴᴍᴜᴛᴇ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ.\n⦿ .pin / .unpin ➠  ᴘɪɴ ᴍᴇꜱꜱᴇɢᴇ ᴀɴᴅ ᴜɴᴘɪɴ ᴍᴇꜱꜱᴇɢᴇ.\n⦿ .kick / .dkick ➠  ᴋɪᴄᴋ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ ᴀɴᴅ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴇɢᴇ ᴋɪᴄᴋ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀ.\n⦿ .promote / .fullpromote ➠  ɴᴏʀᴍᴀʟ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇᴍʙᴇʀ ᴀɴᴅ ꜰᴜʟʟ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇᴍʙᴇʀ.\n⦿ .demote ➠  ᴘʀᴏᴍᴏᴛᴇᴅ ᴀᴅᴍɪɴ ᴅᴇᴍᴏᴛᴇ.\n⦿.purge : ᴅᴇʟᴇᴛᴇ ᴀʟʟ ᴍᴇꜱꜱᴀɢᴇꜱ ꜰʀᴏᴍ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ.\n⦿.del : ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ.\n⦿ .banall ➠  ʙᴀɴᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ɪɴ ɢʀᴏᴜᴘꜱ.\n⦿ .unbanall ➠  ᴜɴʙᴀɴᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ɪɴ ɢʀᴏᴜᴘꜱ.\n⦿ .unmuteall ➠  ᴜɴᴍᴜᴛᴇᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ɪɴ ɢʀᴏᴜᴘꜱ.\n⦿ .kickall ➠  ᴋɪᴄᴋᴀʟʟ ᴍᴇᴍʙᴇʀꜱ ɪɴ ɢʀᴏᴜᴘꜱ.\n⦿ .ping ➠ .alive\n⦿ .join  ➠ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀᴛ ᴠɪᴀ ᴜꜱᴇʀɴᴀᴍᴇ.\n⦿ .leave  ➠  ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ᴠɪᴀ ᴜꜱᴇʀɴᴀᴍᴇ.\n⦿ .dm ➠  .dm @username hello hii.⦿ /startub ➠ ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴅᴏ ɪᴛ ᴇᴠᴇʀʏᴛɪᴍᴇ ᴡʜᴇɴᴇᴠᴇʀ ʏᴏᴜ ᴡɪʟʟ ᴄᴏᴍᴇ ʙᴀᴄᴋ ᴏɴʟɪɴᴇ ᴊᴜꜱᴛ ᴠɪꜱɪᴛ ᴛʜᴇ ᴅᴍ/ᴘᴍ ᴏꜰ ᴘᴀʀᴇɴᴛᴀʟ ʙᴏᴛ  ᴀɴᴅ ᴛʏᴘᴇ /startub"
""" 
@Client.on_message(filters.command("help",prefixes=".")& filters.me)
async def help(b,m):
    await m.reply(ub_help)