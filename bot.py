

# Импортируем необходимые компоненты
import logging
import os
#from Wand.image import Image

from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.ext import Filters

from settings import TG_TOKEN
from handlers import *

from utility import get_keyboard

import sqlite3
from mysqldb import *


PORT = int(os.environ.get('PORT', 5000))
updater=Updater(TG_TOKEN,use_context=True)
updater.start_webhook(listen="0.0.0.0",
port=int(PORT),
url_path=TG_TOKEN)
updater.bot.setWebhook('https://odessaguide.herokuapp.com/' + TG_TOKEN) 



logging.basicConfig(format='%(asctime)s-$(levelname)s-$(message)s',
                    level=logging.INFO,
                    filename='bot.log')


ls_cats=build_regex_cats()
ls_subcats=build_regex_subcats()
#нкцию main, которая соединяется с платформой Telegram
def main():

   
    my_bot = Updater(TG_TOKEN, use_context=True)
    logging.info('Start bot')
    
   
    
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))  # обработчик команды start
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('🔙'),  main_keyboard))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('🛒'),  get_cart))
   
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex(ls_cats), build_subcats))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex(ls_subcats), build_goods))
    
   
    my_bot.dispatcher.add_handler(CallbackQueryHandler(add_order, pattern='get_goods'))

    my_bot.dispatcher.add_handler(CallbackQueryHandler(delete_cart, pattern='deleteall'))

    my_bot.dispatcher.add_handler(CallbackQueryHandler(edit_cart, pattern='edit'))

    my_bot.dispatcher.add_handler(CallbackQueryHandler(plus_quan, pattern='plus'))

    my_bot.dispatcher.add_handler(CallbackQueryHandler(on_right, pattern='right'))

    my_bot.dispatcher.add_handler(CallbackQueryHandler(on_left, pattern='left'))

    my_bot.dispatcher.add_handler(CallbackQueryHandler(minus_quan, pattern='minus'))

    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), sms))  # обрабатываем текс кнопки
   
    my_bot.dispatcher.add_handler(MessageHandler(Filters.location, get_location))  # обработчик полученной геопозиции
    
    
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, get_goods))

    
   # my_bot.dispatcher.add_handler(CallbackQueryHandler(inline_button_pressed))

  
    #my_mot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))  # обработчик текстового сообщения
    my_bot.start_polling()  # проверяет о наличии сообщений с платформы Telegram
    #my_bot.start_webhook(listen="0.0.0.0",

    #port=int(PORT),
   # url_path=TG_TOKEN)
    #my_bot.bot.setWebhook('https://mighty-savannah-13294.herokuapp.com/'+TG_TOKEN)

    my_bot.idle()  # бот будет работать пока его не остановят


if __name__ == "__main__":
    main()
