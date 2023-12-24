from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from secrets import TOKEN
from commands import start_command, price_command, button_handler


async def error(update, context):
    print(f'caused error {context.error}')





def main():
    print("App running")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(CommandHandler("price", price_command))
    
    
    # app.add_handler(MessageHandler(filters.TEXT, handle_decision))

    # app.add_error_handler(error)

    print("polling")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

