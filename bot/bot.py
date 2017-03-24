from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from planet import *
from wordcount import *

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
    answer = ''

    if message.startswith ('/wordcount'):
        answer = count_words_in_message(update.message.text)
        print(1, answer)
    else:
        answer = get_sign_by_planet(update.message.text)
        print(2, answer)

    print(3, answer)
    
    bot.sendMessage(update.message.chat_id, answer)

main()