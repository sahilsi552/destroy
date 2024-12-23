
import imghdr
import os
from asyncio import gather
from traceback import format_exc
from Merisa import QuantamBot as app,eor
from Merisa.misc import SUDOERS
from Merisa.utils.errors import capture_err
from pyrogram import filters
from pyrogram.errors import (
    PeerIdInvalid,
    ShortnameOccupyFailed,
    StickerEmojiInvalid,
    StickerPngDimensions,
    StickerPngNopng,
    UserIsBlocked,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from Merisa.utils.files import (
    get_document_from_file_id,
    resize_file_to_sticker_size,
    upload_document,
)
from Merisa.utils.stickersets import (
    add_sticker_to_set,
    create_sticker,
    create_sticker_set,
    get_sticker_set_by_name,
)

import os
import math
from PIL import Image
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import TelegramError
from io import BytesIO

__MODULE__ = "Sᴛɪᴄᴋᴇʀs"
__HELP__ = """
๏ /sticker_id ➥ To get FileID of a Sticker.
๏ /get_sticker ➥To get sticker as a photo and document.
๏ /kang  ➥To kang a Sticker or an Image."""

MAX_STICKERS = (
    120  # would be better if we could fetch this limit directly from telegram
)
SUPPORTED_TYPES = ["jpeg", "png", "webp"]


@app.on_message(filters.command("sticker_id"))
@capture_err
async def sticker_id(_, message: Message):
    reply = message.reply_to_message

    if not reply:
        return await message.reply("Reply to a sticker.")

    if not reply.sticker:
        return await message.reply("Reply to a sticker.")

    await message.reply_text(f"`{reply.sticker.file_id}`")


@app.on_message(filters.command("get_sticker"))
@capture_err
async def sticker_image(_, message: Message):
    r = message.reply_to_message

    if not r:
        return await message.reply("Reply to a sticker.")

    if not r.sticker:
        return await message.reply("Reply to a sticker.")

    m = await message.reply("Sending..")
    f = await r.download(f"{r.sticker.file_unique_id}.png")

    await gather(
        *[
            message.reply_photo(f),
            message.reply_document(f),
        ]
    )

    await m.delete()
    os.remove(f)



@app.on_message(filters.command("kang"))
@capture_err
async def kang(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a sticker/image to kang it.")
    if not message.from_user:
        return await message.reply_text(
            "You are anon admin, kang stickers in my pm."
        )
    msg = await message.reply_text("Kanging Sticker..")

    # Find the proper emoji
    args = message.text.split()
    if len(args) > 1:
        sticker_emoji = str(args[1])
    elif (
        message.reply_to_message.sticker
        and message.reply_to_message.sticker.emoji
    ):
        sticker_emoji = message.reply_to_message.sticker.emoji
    else:
        sticker_emoji = "🤔"

    # Get the corresponding fileid, resize the file if necessary
    doc = message.reply_to_message.photo or message.reply_to_message.document
    try:
        if message.reply_to_message.sticker:
            sticker = await create_sticker(
                await get_document_from_file_id(
                    message.reply_to_message.sticker.file_id
                ),
                sticker_emoji,
            )
        elif doc:
            if doc.file_size > 10000000:
                return await msg.edit("File size too large.")

            temp_file_path = await app.download_media(doc)
            image_type = imghdr.what(temp_file_path)
            if image_type not in SUPPORTED_TYPES:
                return await msg.edit(
                    "Format not supported! ({})".format(image_type)
                )
            try:
                temp_file_path = await resize_file_to_sticker_size(
                    temp_file_path
                )
            except OSError as e:
                await msg.edit_text("Something wrong happened.")
                raise Exception(
                    f"Something went wrong while resizing the sticker (at {temp_file_path}); {e}"
                )
            sticker = await create_sticker(
                await upload_document(client, temp_file_path, message.chat.id),
                sticker_emoji,
            )
            if os.path.isfile(temp_file_path):
                os.remove(temp_file_path)
        else:
            return await msg.edit("Nope, can't kang that.")
    except ShortnameOccupyFailed:
        await message.reply_text("Change Your Name Or Username")
        return

    except Exception as e:
        await message.reply_text(str(e))
        e = format_exc()
        return print(e)

    # Find an available pack & add the sticker to the pack; create a new pack if needed
    # Would be a good idea to cache the number instead of searching it every single time...
    packnum = 0
    packname = "f" + str(message.from_user.id) + "_by_" + BOT_USERNAME
    limit = 0
    try:
        while True:
            # Prevent infinite rules
            if limit >= 50:
                return await msg.delete()

            stickerset = await get_sticker_set_by_name(client, packname)
            if not stickerset:
                stickerset = await create_sticker_set(
                    client,
                    message.from_user.id,
                    f"{message.from_user.first_name[:32]}'s kang pack",
                    packname,
                    [sticker],
                )
            elif stickerset.set.count >= MAX_STICKERS:
                packnum += 1
                packname = (
                    "f"
                    + str(packnum)
                    + "_"
                    + str(message.from_user.id)
                    + "_by_"
                    + BOT_USERNAME
                )
                limit += 1
                continue
            else:
                try:
                    await add_sticker_to_set(client, stickerset, sticker)
                except StickerEmojiInvalid:
                    return await msg.edit("[ERROR]: INVALID_EMOJI_IN_ARGUMENT")
            limit += 1
            break

        await msg.edit(
            "Sticker Kanged To [Pack](t.me/addstickers/{})\nEmoji: {}".format(
                packname, sticker_emoji
            )
        )
    except (PeerIdInvalid, UserIsBlocked):
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Start", url=f"t.me/{BOT_USERNAME}")]]
        )
        await msg.edit(
            "You Need To Start A Private Chat With Me.",
            reply_markup=keyboard,
        )
    except StickerPngNopng:
        await message.reply_text(
            "Stickers must be png files but the provided image was not a png"
        )
    except StickerPngDimensions:
        await message.reply_text("The sticker png dimensions are invalid.")




async def kang(client, message):
    msg = message
    args = message.text.split()
    packnum = 0
    user = msg.from_user
    packname = f"a{str(user.id)}_by_{client.me.username}"
    packname_found = False
    max_stickers = 120

    while not packname_found:
        try:
            if await sticker_count(client, packname) >= max_stickers:
                packnum += 1
                packname = f"a{str(packnum)}_{str(user.id)}_by_{client.me.username}"
            else:
                packname_found = True
        except TelegramError as e:
            if e.message == "Stickerset_invalid":
                packname_found = True

    kangsticker = "kangsticker.png"
    is_animated = False
    is_video = False
    is_gif = False
    file_id = ""

    if msg.reply_to_message:
        if msg.reply_to_message.sticker:
            if msg.reply_to_message.sticker.is_animated:
                is_animated = True
            elif msg.reply_to_message.sticker.is_video:
                is_video = True
            file_id = msg.reply_to_message.sticker.file_id
        elif msg.reply_to_message.photo:
            file_id = msg.reply_to_message.photo[-1].file_id
        elif msg.reply_to_message.document and msg.reply_to_message.document.mime_type != "video/mp4":
            file_id = msg.reply_to_message.document.file_id
        elif msg.reply_to_message.animation:
            file_id = msg.reply_to_message.animation.file_id
            is_gif = True
        else:
            await msg.reply_text("ʏᴇᴀ, ɪ ᴄᴀɴ'ᴛ ᴋᴀɴɢ ᴛʜᴀᴛ.")

        kang_file = await client.get_file(file_id)
        if not is_animated and not is_video and not is_gif:
            await kang_file.download("kangsticker.png")
        elif is_animated:
            await kang_file.download("kangsticker.tgs")
        elif is_video and not is_gif:
            await kang_file.download("kangsticker.webm")
        else:
            await kang_file.download("kang.mp4")
            convert_gif("kang.mp4")

        sticker_emoji = args[1] if len(args) > 1 else "🙂"

        adding_process = await msg.reply_text("<b>ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...ғᴏʀ ᴀ ᴍᴏᴍᴇɴᴛ</b>", parse_mode="html")

        if not is_animated and not is_video and not is_gif:
            try:
                im = Image.open(kangsticker)
                maxsize = (512, 512)
                if im.width < 512 and im.height < 512:
                    scale = 512 / max(im.width, im.height)
                    size1new = math.floor(im.width * scale)
                    size2new = math.floor(im.height * scale)
                    sizenew = (size1new, size2new)
                    im = im.resize(sizenew)
                else:
                    im.thumbnail(maxsize)

                if not msg.reply_to_message.sticker:
                    im.save(kangsticker, "PNG")

                await client.add_sticker_to_set(user.id, packname, png_sticker=open(kangsticker, "rb"), emojis=sticker_emoji)

                edited_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="⎋ ᴘᴀᴄᴋ ⎋", url=f"t.me/addstickers/{packname}")]])
                await adding_process.edit_text(f"<b>ʏᴏᴜʀ sᴛɪᴄᴋᴇʀ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ!</b>\nᴇᴍᴏᴊɪ ɪs ➼ : {sticker_emoji}", reply_markup=edited_keyboard, parse_mode="html")
            except OSError as e:
                print(e)
                return
            except TelegramError as e:
                if e.message == "Internal Server Error: sticker set not found (500)":
                    edited_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="⎋ ᴘᴀᴄᴋ ⎋", url=f"t.me/addstickers/{packname}")]])
                    await msg.reply_text(f"<b>ʏᴏᴜʀ sᴛɪᴄᴋᴇʀ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ!</b>\nᴇᴍᴏᴊɪ ɪs ➼ : {sticker_emoji}", reply_markup=edited_keyboard, parse_mode="html")
                elif e.message == "Invalid sticker emojis":
                    await msg.reply_text("Invalid emoji(s).")
                elif e.message == "Sticker_png_dimensions":
                    im.save(kangsticker, "PNG")
                    adding_process = await msg.reply_text("<b>ᴡᴀɪᴛ.... ғᴏʀ ᴀ ᴍᴏᴍᴇɴᴛ ..</b>", parse_mode="html")
                    await client.add_sticker_to_set(user.id, packname, png_sticker=open(kangsticker, "rb"), emojis=sticker_emoji)
                    edited_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="⎋ ᴘᴀᴄᴋ ⎋", url=f"t.me/addstickers/{packname}")]])
                    await adding_process.edit_text(f"<b>ʏᴏᴜʀ sᴛɪᴄᴋᴇʀ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ!</b>\nᴇᴍᴏᴊɪ ɪs ➼ : {sticker_emoji}", reply_markup=edited_keyboard, parse_mode="html")
                elif e.message == "Stickers_too_much":
                    await msg.reply_text("Max packsize reached. Press F to pay respect.")
                elif e.message == "Stickerset_invalid":
                    await makepack_internal(client, msg, user, sticker_emoji, packname, packnum, png_sticker=open("kangsticker.png", "rb"))
                    await adding_process.delete()
                print(e)

        # Handle animated or video stickers
        elif is_animated:
            packname = f"animated{str(user.id)}_by_{client.me.username}"
            packname_found = False
            max_stickers = 50
            while not packname_found:
                try:
                    if await sticker_count(client, packname) >= max_stickers:
                        packnum += 1
                        packname = f"animated{str(packnum)}_{str(user.id)}_by_{client.me.username}"
                    else:
                        packname_found = True
                except TelegramError as e:
                    if e.message == "Stickerset_invalid":
                        packname_found = True

            try:
                await client.add_sticker_to_set(user.id, packname, tgs_sticker=open("kangsticker.tgs", "rb"), emojis=sticker_emoji)
                edited_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="⎋ ᴘᴀᴄᴋ ⎋", url=f"t.me/addstickers/{packname}")]])
                await adding_process.edit_text(f"<b>ʏᴏᴜʀ sᴛɪᴄᴋᴇʀ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ!</b>\nᴇᴍᴏᴊɪ ɪs ➼ : {sticker_emoji}", reply_markup=edited_keyboard, parse_mode="html")
            except TelegramError as e:
                if e.message == "Internal Server Error: sticker set not found (500)":
                    edited_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="⎋ ᴘᴀᴄᴋ ⎋", url=f"t.me/addstickers/{packname}")]])
                    await adding_process.edit_text(f"<b>ʏᴏᴜʀ sᴛɪᴄᴋᴇʀ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ!</b>\nᴇᴍᴏᴊɪ ɪs ➼ : {sticker_emoji}", reply_markup=edited_keyboard, parse_mode="html")
                elif e.message == "Invalid sticker emojis":
                    await msg.reply_text("Invalid emoji(s).")
                elif e.message == "Stickerset_invalid":
                    await makepack_internal(client, msg, user, sticker_emoji, packname, packnum, tgs_sticker=open("kangsticker.tgs", "rb"))
                    await adding_process.delete()
                print(e)

        # Handle video stickers
        else:
            packname = f"video{str(user.id)}_by_{client.me.username}"
            packname_found = False
            max_stickers = 50
            while not packname_found:
                try:
                    if await sticker_count(client, packname) >= max_stickers:
                        packnum += 1
                        packname = f"video{str(packnum)}_{str(user.id)}_by_{client.me.username}"
                    else:
                        packname_found = True
                except TelegramError as e:
                    if e.message == "Stickerset_invalid":
                        packname_found = True

            try:
                await client.add_sticker_to_set(user.id, packname, webm_sticker=open("kangsticker.webm", "rb"), emojis=sticker_emoji)
                edited_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="⎋ ᴘᴀᴄᴋ ⎋", url=f"t.me/addstickers/{packname}")]])
                await adding_process.edit_text(f"<b>ʏᴏᴜʀ sᴛɪᴄᴋᴇʀ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ!</b>\nᴇᴍᴏᴊɪ ɪs ➼ : {sticker_emoji}", reply_markup=edited_keyboard, parse_mode="html")
            except TelegramError as e:
                if e.message == "Internal Server Error: sticker set not found (500)":
                    edited_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="⎋ ᴘᴀᴄᴋ ⎋", url=f"t.me/addstickers/{packname}")]])
                    await adding_process.edit_text(f"<b>ʏᴏᴜʀ sᴛɪᴄᴋᴇʀ ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ!</b>\nᴇᴍᴏᴊɪ ɪs ➼ : {sticker_emoji}", reply_markup=edited_keyboard, parse_mode="html")
                elif e.message == "Invalid sticker emojis":
                    await msg.reply_text("Invalid emoji(s).")
                elif e.message == "Stickerset_invalid":
                    await makepack_internal(client, msg, user, sticker_emoji, packname, packnum, webm_sticker=open("kangsticker.webm", "rb"))
                    await adding_process.delete()
                print(e)

    # Cleanup
    try:
        if os.path.isfile("kangsticker.png"):
            os.remove("kangsticker.png")
        elif os.path.isfile("kangsticker.tgs"):
            os.remove("kangsticker.tgs")
        elif os.path.isfile("kangsticker.webm"):
            os.remove("kangsticker.webm")
    except:
        pass




async def makepack_internal(
    client: Client,
    msg,
    user,
    emoji,
    packname,
    packnum,
    png_sticker=None,
    tgs_sticker=None,
    webm_sticker=None,
):
    name = user.first_name
    name = name[:50]  # Limit name length to 50 characters
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="⎋ ᴘᴀᴄᴋ ⎋", url=f"t.me/addstickers/{packname}")]]
    )

    try:
        extra_version = f" {str(packnum)}" if packnum > 0 else ""
        
        # Handling PNG Sticker
        if png_sticker:
            sticker_pack_name = f"{name}'s sticker pack (@{client.me.username}){extra_version}"
            success = await client.create_new_sticker_set(
                user.id,
                packname,
                sticker_pack_name,
                png_sticker=png_sticker,
                emojis=emoji,
            )

        # Handling TGS (animated) Sticker
        if tgs_sticker:
            sticker_pack_name = f"{name}'s animated pack (@{client.me.username}){extra_version}"
            success = await client.create_new_sticker_set(
                user.id,
                packname,
                sticker_pack_name,
                tgs_sticker=tgs_sticker,
                emojis=emoji,
            )

        # Handling WebM (video) Sticker
        if webm_sticker:
            sticker_pack_name = f"{name}'s video pack (@{client.me.username}){extra_version}"
            success = await client.create_new_sticker_set(
                user.id,
                packname,
                sticker_pack_name,
                webm_sticker=webm_sticker,
                emojis=emoji,
            )

    except TelegramError as e:
        print(e)
        if e.message == "Sticker set name is already occupied":
            await msg.reply_text(
                "<b>Your Sticker Pack is already created!</b>"
                "\n\nYou can now reply to images, stickers, and animated stickers with /steal to add them to your pack"
                "\n\n<b>Send /stickers to find any sticker pack.</b>",
                reply_markup=keyboard,
                parse_mode="html",
            )
        else:
            await msg.reply_text(
                f"{client.me.first_name} was blocked by you.",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="ᴜɴʙʟᴏᴄᴋ", url=f"t.me/{client.me.username}"
                            )
                        ]
                    ]
                ),
            )
        return

    if success:
        await msg.reply_text(
            "<b>Your Sticker Pack has been created!</b>"
            "\n\nYou can now reply to images, stickers, and animated stickers with /steal to add them to your pack"
            "\n\n<b>Send /stickers to find sticker packs.</b>",
            reply_markup=keyboard,
            parse_mode="html",
        )
    else:
        await msg.reply_text("Failed to create sticker pack. Possibly due to some error.")

