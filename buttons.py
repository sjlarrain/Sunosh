from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def access_keyboard():
    options = [
        [
            InlineKeyboardButton("Price", callback_data="/price"),
            InlineKeyboardButton("Trader", callback_data="/trader"),
        ],
        [InlineKeyboardButton("Return", callback_data="/return")],
    ]
    
    reply_markup = InlineKeyboardMarkup(options)
    return reply_markup

def trader_keyboard():
    options = [
        [InlineKeyboardButton("Buy", callback_data="/buy"),
        InlineKeyboardButton("Sell", callback_data="/sell"),
        InlineKeyboardButton("Back", callback_data="/back")
        ]]
    reply_markup = InlineKeyboardMarkup(options)
    return reply_markup


