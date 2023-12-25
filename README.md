# Sunosh
### Intro
Sunosh is a bot designed to manage the execution of short trades without logging to your personal trade plataform.

### Requirements

For the execution of this plataform is based under the following python libraries:

- `python-telegram-bot`

### File structure

The bot is build with a certain structure to build custom requirements for the user. Therefore, the following files are use.

- `main.py`: The file manages all relation with all other modules. Through the function `main` handles all the handlers for the bot functionality
- `commands.py`: It manages the commands for the bot which will be use in `main.py`. The following commands are explain below:
     - `start_command`: Initialized the bot
     - `authentification`: For authentification
     - `price_command`: Retrives the value of the crypto currency
     - `back_command`: Get the user back to the menu
     - `error_handler`: Manages errors in the code execution
     - `button_handler`: Manages the execution of the menu fuctionalities through the button flow
- `buttons.py`: It manages all the keyboard templates to be use in the different functions as the are executed 
    - `access_keyboard`: Main menu
    - `trader_keyboard`: Menu for the trade executions

### Other requirements

To keep the user information safe, this code requires a personal file named `secrets.py`. In this file the user manages all tokens, user names, encryptation functions and any other sensitive information. 

In the current bot, the following variables are need to be declare in the `secrets.py` file:
- `TOKEN`: Telegram bot token. Is use in the `main.py` file
- `USER`: Telegram bot username. Is use in the `main.py`file

In the current bot, the following function are need to be developed:
- `encrypt(value)`: This function must be developed by the user to protect the user bot due. It returns a `bool` as result of the code designation. Is use in the `commands.py` file
