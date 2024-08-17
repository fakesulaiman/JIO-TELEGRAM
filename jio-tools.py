import pandas as pd
import requests
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler

# Replace 'your_bot_token' with your actual bot token
bot_token = "7265384689:AAFWVlaMxN20Y2LyJsVrO3ldUQd5J8hgMcI"
bot = Bot(token=bot_token)
application = Application.builder().token(bot_token).build()

# Function to send custom SMS using CSV data
async def send_custom_sms(update: Update, context):
    # GitHub থেকে CSV ফাইলের RAW URL
    csv_url = 'https://raw.githubusercontent.com/fakesulaiman/JIO-TELEGRAM/main/Jio-Tools-server.csv'

    # CSV ফাইল থেকে ডেটা লোড করা
    try:
        df = pd.read_csv(csv_url)
        for _, row in df.iterrows():
            number = row['number']
            message = row['message']

            # API call to send SMS
            sms_url = f'https://sms-giveway.vercel.app/send-sms?number={number}&message={message}&key=DH-ALAMINy'
            response = requests.get(sms_url)

            if response.status_code == 200:
                await update.message.reply_text(f"SMS sent to {number}")
            else:
                await update.message.reply_text(f"Failed to send SMS to {number}")

    except Exception as e:
        await update.message.reply_text(f"Failed to process CSV data: {e}")

# Command to clear chat
async def clear_chat(update: Update, context):
    await context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    await update.message.reply_text("Chat cleared!")

# Command to display admin information
async def admin_info(update: Update, context):
    admin_message = "Admin Name: Your Admin Name\nContact: +8801XXXXXXXXX"
    await update.message.reply_text(admin_message)

# Command to greet user with their name
async def greet_user(update: Update, context):
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f"Hello {user_name}!")

# Add command handlers to the application
application.add_handler(CommandHandler("custom_sms", send_custom_sms))
application.add_handler(CommandHandler("clea", clear_chat))
application.add_handler(CommandHandler("admin", admin_info))
application.add_handler(CommandHandler("hello", greet_user))

# Start the bot
if __name__ == "__main__":
    application.run_polling()
