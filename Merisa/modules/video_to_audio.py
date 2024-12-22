from moviepy.editor import VideoFileClip as VFC
from .. import QuantamBot
from pyrogram import filters
import requests,os

@QuantamBot.on_message(filters.command("extractaudio"))
async def audiofromvideo(_, m):
    
    try:
        if m.reply_to_message and m.reply_to_message.media:
            vid = await m.reply_to_message.download()
            x = await m.reply("wait a moment")
            video=VFC(vid)
            audio=video.audio
            audio.write_audiofile("audio.mp3")
            await x.delete()
            await m.reply_voice("audio.mp3",quote=True)
    except Exception as e:
        await m.reply(e, quote=True)
from music_text import *
__MODULE="BLACKLIST"
__HELP=blacklist
