import requests
from bs4 import BeautifulSoup
from utility import get_keyboard
from  telegram import  KeyboardButton, ReplyKeyboardMarkup, ParseMode, Location, Venue, InlineKeyboardMarkup
from  telegram.ext import ConversationHandler
from glob import glob

from  random import  choice
import wand
from emoji import  emojize
from mysqldb import *


#from utility import SMILE, back_but




def sms(bot, update):
    print(f'Зашел {bot.message.chat.first_name}')
    smile =emojize(choice(SMILE),use_aliases=True)
   
    bot.message.reply_text((f'Hi {bot.message.chat.first_name}😀 !!!\n  I am your shop assistant {smile}!!!' ),
    reply_markup=build_cats(bot, update))
  
def main_keyboard(bot, update):
    
  
    bot.message.reply_text("Main menu", reply_markup=build_cats(bot, update))



def make_keyboard(bot,update):
   result=[]
   print(bot.message.text)
   result= build_keyboard(bot.message.text)

    
   reply_keyboard = []
   reply_keyboard.append("🔙")
   for el in result:
       print(el)
       reply_keyboard.append(el)
    
   
   

   # создаем клавиатуру
   bot.message.reply_text(
        f"{bot.message.text}",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard , resize_keyboard=True))


   
  














