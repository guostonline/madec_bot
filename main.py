from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import asyncio

TOKEN = "6558880037:AAHMgJAI44nDdHewD8xp2mTslkbH2NmJ394"


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(update.effective_chat.id, text="Hi this is help!")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(update.effective_chat.id,
                                   text=f"Hi {update.message.from_user.first_name} how can I help you ")


if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()
    # List of commandes
    help_hundler = CommandHandler("help", help)
    start_hundler = CommandHandler("start", start)

    # Activate commands
    application.add_handler(help_hundler)
    application.add_handler(start_hundler)
    application.run_polling()
