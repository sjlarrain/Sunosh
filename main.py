from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from secrets import TOKEN
from commands import (start_command, price_command, button_handler, error_handler,
                      authentification
)
from trader import ExchangeManager

def main():
    print("App running")
    trader = ExchangeManager("btc-clp")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(CommandHandler("price", price_command))
    app.add_handler(MessageHandler(filters.TEXT, authentification))
    # app.add_error_handler(error_handler)

    print("polling")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

