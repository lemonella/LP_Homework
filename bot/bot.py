from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from planet import *

def main():
    updater = Updater("315853602:AAHhawei6okVUMQkcLgR13VC4Zi6BpWG944")
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()

def greet_user (bot, update):
    print('Вызван / start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def show_error (bot, update, error):
    print(error)

def talk_to_me(bot, update):
    sign = get_sign_by_planet(update.message.text)
    bot.sendMessage(update.message.chat_id, sign)

main()