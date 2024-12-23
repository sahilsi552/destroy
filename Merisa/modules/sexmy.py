import random
from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from Merisa import QuantamBot as app
# Unified thumbnail URL
THUMB_URL = "https://i.ibb.co/Dgd586R/file-5790.jpg"

BUTTON = [[InlineKeyboardButton("🔍 Check Your Result", switch_inline_query_current_chat="")]]

@app.on_inline_query()
async def inline_queries(client, inline_query):
    user_id = inline_query.from_user.id
    user_name = inline_query.from_user.first_name
    query = inline_query.query.strip()

    # If a query is provided, use it as the target name; otherwise, set a default
    if query:
        target_name = query
    else:
        target_name = "someone"

    mention = f"[{user_name}](tg://user?id={user_id})"  # Mention sender's name

    # Randomly generated values
    mm = random.randint(1, 100)  # Random percentage
    cm = random.randint(5, 30)  # Random size in cm for Dick/Vagina Depth
    marriage_prob = random.randint(1, 100)  # Random marriage probability
    name_start = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # Random starting letter for a name

    results = []

    # List of responses
    random_responses = [
        {
            "title": "Horny Level",
            "description": "Check how horny you are!",
            "text": f"🔥 {mention} is {mm}% horny!",
        },
        {
            "title": "Gayness Level",
            "description": "Check how gay you are!",
            "text": f"🍷 {mention} is {mm}% gay!",
        },
        {
            "title": "Marriage Probability",
            "description": "Check your marriage probability with someone!",
            "text": f"💍 Marriage probability of {mention} with '{target_name}' is {marriage_prob}%.",
        },
        {
            "title": "Name Starts With",
            "description": "Find out which letter your name starts with!",
            "text": f"🔠 Your name starts with the letter '{name_start}'.",
        },
        {
            "title": "Dick Size",
            "description": "Check the size of your dick!",
            "text": f"🍌 {mention}'s dick size is {cm} cm!",
        },
        {
            "title": "Vagina Depth",
            "description": "Check the depth of your vagina!",
            "text": f"🌹 {mention}'s vagina depth is {cm} cm!",
        },
        {
            "title": "Hotness Level",
            "description": "Check how hot you are!",
            "text": f"🔥 {mention} is {mm}% hot!",
        },
        {
            "title": "MC Level",
            "description": "Check your MC level!",
            "text": f"⚡ {mention} is {mm}% MC!",
        },
        {
            "title": "BC Level",
            "description": "Check your BC level!",
            "text": f"⚡ {mention} is {mm}% BC!",
        },
    ]

    # Create results for inline query
    for response in random_responses:
        results.append(
            InlineQueryResultArticle(
                title=response["title"],
                description=response["description"],
                input_message_content=InputTextMessageContent(
                    response["text"], disable_web_page_preview=True
                ),
                reply_markup=InlineKeyboardMarkup(BUTTON),
                thumb_url=THUMB_URL,  # Unified thumbnail URL
                thumb_width=100,
                thumb_height=100,
            )
        )

    # Display results
    if results:
        await inline_query.answer(results, cache_time=1, is_personal=True)
