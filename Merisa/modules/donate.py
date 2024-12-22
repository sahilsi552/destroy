from pyrogram import Client, filters, types
from Merisa import QuntamBot as app


@app.on_message(filters.command("donate"))
async def message_handler(client: Client, message: types.Message):
    try:
        # Extract the amount from the command (e.g., /donate 100)
        amount = int(message.command[1])  
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
    except (IndexError, ValueError):
        await message.reply("Please specify a valid amount. Usage: /support <amount>")
        return

    # Send the invoice
    await client.send_invoice(
        chat_id=message.chat.id,
        title="Donate",
        description="Support me",
        currency="XTR",  
        prices=[types.LabeledPrice(label="Star", amount=amount)],
        payload="stars"
    )

@app.on_pre_checkout_query()
async def pre_checkout_query_handler(_: Client, query: types.PreCheckoutQuery):
    await query.answer(ok=True)
