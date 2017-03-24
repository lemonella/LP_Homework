import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from planet import *
from wordcount import *

# setting up the logging module
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

def main():
    updater = Updater("315853602:AAHhawei6okVUMQkcLgR13VC4Zi6BpWG944")
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("wordcount", count_words))
   
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()

def greet_user (bot, update):
    print('Вызван / start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def show_error (bot, update, error):
    print(error)

def count_words(bot, update):
    bot.sendMessage(update.message.chat_id, count_words_in_message(update.message.text))

def talk_to_me(bot, update):
    bot.sendMessage(update.message.chat_id, get_sign_by_planet(update.message.text))

main()