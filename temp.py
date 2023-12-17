from secrets import TOKEN, USER
from telegram import ReplyKEyboardMarkup
from telegram.ext import  (Application, CommandHandler, MessageHandler,
                           filters, ContextTypes)

async def start_command(update, context):
    await update.message.reply_text("Hello thanks to chat") 

def handle_responses(text):
    if "hello" in text:
        return "Hi"
    return "Please try again"

async def handle_message(update, context):
    message = update.message.text
    response = handle_responses(message)
    await update.message.reply_text(response)

async def error(update, context):
    print(f'Update: {update} caused error {context.error}')


if __name__ == "__main__":
    print("App running")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("polling")
    app.run_polling(poll_interval=3)