from telegram import ReplyKeyboardMarkup, Bot
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from secrets import TOKEN
from parameters import decision_tree
# Define the decision tree as a dictionary

# Function to generate a keyboard based on the current node in the decision tree
def generate_keyboard(node):
    options = decision_tree[node]['options'].keys()
    keyboard = [[option] for option in options]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

# Command handler to start the decision tree
async def start_command(update, context):
    await update.message.reply_text(decision_tree['start']['question'], reply_markup=generate_keyboard('start'))

# Message handler to handle user input and navigate the decision tree
async def handle_decision(update, context):
    user_choice = update.message.text.lower()
    current_node = context.user_data.get('current_node', 'start')

    if user_choice in decision_tree[current_node]['options']:
        next_node = user_choice
        await update.message.reply_text(decision_tree[next_node]['question'], reply_markup=generate_keyboard(next_node))
        context.user_data['current_node'] = next_node
    else:
        await update.message.reply_text("Invalid choice. Please select a valid option.")

async def error(update, context):
    print(f'Update: {update} caused error {context.error}')


def main():
    print("App running")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    
    app.add_handler(MessageHandler(filters.TEXT, handle_decision))

    app.add_error_handler(error)

    print("polling")
    app.run_polling(poll_interval=3)

if __name__ == '__main__':
    main()
