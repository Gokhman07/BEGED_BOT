
from  telegram import  KeyboardButton, ReplyKeyboardMarkup

SMILE = ['😊', '😀', '😇', '🤠', '😎', '🤓',  '😉',' ']
CALLBACK_BUTTON_PICTURE = "Картинка 🏞"
CALLBACK_BUTTON_PEN = "Заполнить анкету 🖌"
CALLBACK_BUTTON_START = "Начать 🎰"
CALLBACK_BUTTON_JOKE = "Анекдот 🎭"

back_but=KeyboardButton('Назад🔙')

def get_keyboard():
    contact_but=KeyboardButton('Отправить контакт', request_contact=True)
    local_but = KeyboardButton('Узнать свою локацию', request_location=True)
    
    my_keyboard = ReplyKeyboardMarkup([['Начать'], [local_but],['Рестораны 🍷☕'],['Отели  🏩🛎'],['Клубы 🍹🍸'],['ТРЦ  🛍🛒'],
                                       ['Религиозные места ☮']
                                       
                                       ], resize_keyboard=True)
    return  my_keyboard

