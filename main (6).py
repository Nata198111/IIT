import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Set up logger
logger = logging.getLogger(__name__)

# Define a function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.first_name}! I'm your Telegram bot. Welcome!"
    )

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token
    # Replace "YOUR_BOT_TOKEN" with the token you received from BotFather
    application = Application.builder().token("7967508158:AAGRwhc3HbyVlvZqW5erTyN9oP9OF7bBseI").build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()
    logger.info("Bot started polling")

if __name__ == '__main__':
    main()