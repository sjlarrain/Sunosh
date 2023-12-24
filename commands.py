
from buttons import access_keyboard, trader_keyboard
from secrets import encrypt

async def start_command(update, context):
    if not "AUTH" in context.user_data.keys():
        await update.message.reply_text("Please Auth")
    else:
        await update.message.reply_text("Command Menu:", reply_markup=access_keyboard())

async def authentification(update, context):
    context.user_data["AUTH"] = encrypt(update.message.text)
    if context.user_data["AUTH"]:
        await update.message.reply_text("You're authenticated", reply_markup=access_keyboard())
    else:
        await update.message.reply_text("Authentification failed. Please log again")

async def price_command(update, context):
    await update.message.reply_text("The value of BCH is 10.000")
    await update.message.reply_text("Trader options", reply_markup=trader_keyboard())

async def back_command(update, context):
    await start_command(update, context)

async def error_handler(update, context):
    print(f"Caused error{context.error}")
    await update.message.reply_text("Invalid option or text. Please select:", reply_markup=access_keyboard())



async def button_handler(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Selected option: {query.data}")
    if query.data == "/price":
        await price_command(query, context)
    else:
        await start_command(query, context)