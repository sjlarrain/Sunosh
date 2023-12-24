
from buttons import access_keyboard, trader_keyboard

async def start_command(update, context):
    await update.message.reply_text("Command Menu:", reply_markup=access_keyboard())


async def price_command(update, context):
    await update.message.reply_text("Trader options", reply_markup=trader_keyboard())

async def button_handler(update, context):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")