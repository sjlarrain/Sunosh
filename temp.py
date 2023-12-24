from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from secrets import TOKEN
from parameters import menu_decision_tree, task_decision_tree
# Define the decision tree as a dictionary

# Function to generate a keyboard based on the current node in the decision tree
def generate_keyboard(node, context):
    print(f"Keyboard", context.user_data["written"])
    if not context.user_data["written"]:
        decision_tree = context.user_data.get("menu", menu_decision_tree)
        print(decision_tree, "Decision")
        if "options" in decision_tree.keys():
            options = decision_tree[node]['options'].keys()
            keyboard = [[option] for option in options]
            context.user_data["written"] = False
            return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    else:
        context.user_data["written"] = True
        return None

# Command handler to start the decision tree
async def start_command(update, context):
    context.user_data["menu"] = menu_decision_tree
    decision_tree = menu_decision_tree
    context.user_data["written"] = True
    await update.message.reply_text(decision_tree['start']['question'], reply_markup=generate_keyboard('start', context))


# Message handler to handle user input and navigate the decision tree
async def handle_decision(update, context):
    user_choice = update.message.text.lower()
    current_node = context.user_data.get('current_node', 'start')
    decision_tree = context.user_data.get("menu", menu_decision_tree)
    answer_type = context.user_data.get("written", True)

    if answer_type:
        next_node = decision_tree[current_node]["next_state"]
        context.user_data['current_node'] = next_node
        context.user_data["written"] = decision_tree[current_node]["next_type"]
        await update.message.reply_text(decision_tree[next_node]["question"], reply_markup=generate_keyboard(next_node, context))
       
    else:
        if user_choice in decision_tree[current_node]['options']:
            next_node = decision_tree[current_node]["next_step"]
            await update.message.reply_text(decision_tree[next_node]['question'], reply_markup=generate_keyboard(next_node, context))
            context.user_data['current_node'] = next_node
        elif user_choice == "task":
            next_node = user_choice
            decision_tree = task_decision_tree
            await update.message.reply_text(decision_tree[next_node]["question"], reply_markup=generate_keyboard(next_node, context))
        else:
            await update.message.reply_text("Invalid choice. Please select a valid option.")

async def error(update, context):
    print(f'caused error {context.error}')


def main():
    print("App running")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    
    app.add_handler(MessageHandler(filters.TEXT, handle_decision))

    # app.add_error_handler(error)

    print("polling")
    app.run_polling(poll_interval=3)

if __name__ == '__main__':
    main()
