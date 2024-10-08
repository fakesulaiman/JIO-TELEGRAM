import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define a function that will handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

# Define a function that will handle any text messages
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello, World!')

def main() -> None:
    # Read the bot token from the environment variable
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handler for /start
    dispatcher.add_handler(CommandHandler('start', start))

    # Register message handler for all text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot by polling updates from Telegram
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
