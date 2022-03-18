from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext import CallbackContext
import logging

TOKEN = "5206805580:AAG_9NXRkinVcLS0PyOnv3ksjvToRyAWIF0"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


def echo(update, context):
    received_text = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=received_text)


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

updater.start_polling()

