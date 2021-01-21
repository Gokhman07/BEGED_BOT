#from pymongo import  MongoClient
#from settings import  MONGO_DB, MONGODB_LINK
import pymysql
#import pymysql.python
import emoji
from  telegram import  KeyboardButton, ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
import tempfile
#import wand 
import io
from  io import BytesIO
#import pandas
from PIL import Image
#from wand.image import Image
import math

i=0
edit_good=''

def build_cats(bot, update):

      
    
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888bpm4d" )


        cursor = mydb.cursor()
        cursor.execute(f"SELECT title FROM categories")
        data= (cursor.fetchall())
        cursor.close()
        mydb.close()
        ls=[]
        for cat in data:
            ls.append([cat[0]])
     
        ls.append("🛒")
    
      
        my_keyboard = ReplyKeyboardMarkup(ls,resize_keyboard=True)  # добавляем кнопки
        return my_keyboard

def build_regex_cats():
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888bpm4d" )
    
      


        cursor = mydb.cursor()
        cursor.execute(f"SELECT title FROM categories")
        data= (cursor.fetchall())
        cursor.close()
        mydb.close()
        ls=""
        for cat in data:
           
            ls=ls+cat[0]+'|'
        ls=ls[:-1]
    
    
       
        return ls

def build_regex_subcats():

    
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888a" )


        cursor = mydb.cursor()
        cursor.execute(f"SELECT name FROM subcategories")
        data= (cursor.fetchall())
        cursor.close()
        mydb.close()
        ls=""
        for cat in data:
          
            ls=ls+cat[0]+'|'
        ls=ls[:-1]
    
    
   
        return ls

  

def build_keyboard(title):
    mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888bpm4d" )
    
    cursor=conn.cursor()

    sql = f"SELECT title FROM PLACES JOIN PLACES_TYPE ON(PLACES.type_id=PLACES_TYPE.id) WHERE PLACES_TYPE.name='{types[title]}'"
  
    cursor.execute(sql)
    
    sql_results= cursor.fetchall()
    
    result=sql_results


def build_subcats(bot, update):

    
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888bpm4d" )            
       
        cursor = mydb.cursor()
        cursor.execute(f"SELECT name FROM subcategories JOIN categories ON subcategories.categ_id=categories.id  WHERE categories.title='{bot.message.text}'")
        data= (cursor.fetchall())
        cursor.close()
        mydb.close()
        ls=[]
        ls.append("🔙")
        for cat in data:
            ls.append([cat[0]])
        ls.append("🛒")
    
    
       
       
        my_keyboard = ReplyKeyboardMarkup(ls,resize_keyboard=True)  # добавляем кнопки
        bot.message.reply_text("Good choice",reply_markup=my_keyboard)

def build_goods(bot, update):

    
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888bpm4d" )

        
        cursor = mydb.cursor()
        cursor.execute(f"SELECT title FROM goods JOIN subcategories ON goods.sub_id=subcategories.id  WHERE subcategories.name='{bot.message.text}'")
        data= (cursor.fetchall())
        cursor.close()
        mydb.close()
       
        ls=[]
        back=f"🔙"
        ls.append([back])
     
        for cat in data:
            ls.append([cat[0]])

        ls.append("🛒")
    
       
        my_keyboard = ReplyKeyboardMarkup(ls,resize_keyboard=True)  # добавляем кнопки
        bot.message.reply_text("Good choice",reply_markup=my_keyboard)

def add_order(bot, update):
  
          
    
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888bpm4d" )
        query = bot.callback_query
   
        data=(query['message']['reply_markup'])
       
       
        good_name=query['message']['reply_markup']['inline_keyboard'][:][:][0][0]['text'][:-2]
        
        cursor = mydb.cursor()
        cursor.execute(f"SELECT  id from orders WHERE good='{good_name}' and user_id ='{query['message']['chat']['id']}'")
        data=cursor.fetchall()
     
        if data !=():
            update.bot.edit_message_caption(
            caption='This good was already in the cart😊!',
        chat_id=query.message.chat.id,
        message_id=query.message.message_id)
            return


        cursor.execute(f"INSERT INTO `orders`(user_id,good,quantity) VALUES ('{query['message']['chat']['id']}','{good_name}', {1})")
        mydb.commit()
        cursor.close()
        mydb.close()
        update.bot.edit_message_caption(
        caption='Your good was added to cart😊!',
        chat_id=query.message.chat.id,
        message_id=query.message.message_id)

       
def get_goods(bot, update):

    
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888bpm4d" )

        
        cursor = mydb.cursor()
        cursor.execute(f"SELECT title, price, img FROM goods  WHERE title='{bot.message.text}'")
        data= (cursor.fetchall())
        cursor.close()
        mydb.close()
      
       
    
   
       # добавляем кнопки
        bot.message.reply_text(f'Title: {data[0][0]}\nPrice:{data[0][1]}')
        file_like2 = io.BytesIO(data[0][2])
        img1=Image.open(file_like2)
      
        global good
        good=bot.message.text
        
        inl_keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(f'{bot.message.text} 🛒', callback_data='get_goods'), ]])
        file_like2.seek(0)
        update.bot.send_photo(chat_id=bot.message.chat.id, photo=file_like2,reply_markup=inl_keyboard)
        
        
def get_cart(bot, update):

    
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888bpm4d" )

        
        cursor = mydb.cursor()
        cursor.execute(f"SELECT orders.good, orders.quantity, goods.price FROM orders JOIN goods ON orders.good =goods.title   WHERE user_id='{bot.message.chat.id}'")
        data= (cursor.fetchall())
        cursor.close()
        mydb.close()
       
        ls_info=[]
        cart_sum=0
        if data:
            for order in data:
                ls_info.append(f'{order[0]}:\n{order[1]} quan.: {order[2]}*{order[1]} = {order[2]*order[1]}')
                cart_sum=cart_sum+order[2]
        
            ls_orders='\n\n'.join(ls_info)
            inl_keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton('Edit cart  📝', callback_data="edit"), 
            InlineKeyboardButton('Delete all ❌', callback_data="deleteall"),]])
        
            text_info=f"Your orders:\n\n{ls_orders}\n\nSum of order: {round(cart_sum,3),}"

            bot.message.reply_text(text_info,reply_markup=inl_keyboard)
        else:  bot.message.reply_text("You don`t have orders yet(") 


def delete_cart(bot, update):

    
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888bpm4d" )

        query = bot.callback_query
        cursor = mydb.cursor()
      
        cursor.execute(f"DELETE FROM orders   WHERE user_id='{query.message.chat.id}'")
        mydb.commit()
        cursor.close()
        mydb.close()
             

        update.bot.edit_message_text(
        text='Your cart is empty 😊!',
        chat_id=query.message.chat.id,
        message_id=query.message.message_id)

def edit_cart(bot, update, quer=0):

    
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        
        database="s352k345888bpm4d" )
        global i
        global edit_good
        query = bot.callback_query
        cursor = mydb.cursor()
        cursor.execute(f"SELECT orders.good, orders.quantity, goods.price, goods.img FROM orders JOIN goods ON orders.good =goods.title   WHERE user_id='{query.message.chat.id}'")
        data=list((cursor.fetchall())) 
        cursor.close()
        mydb.close()
      
        ls_info=[]
      
         
        
        if i < len(data):
            
            file_like2 = io.BytesIO(data[i][3])
            img1=Image.open(file_like2)
            file_like2.seek(0)
            edit_good=data[i][0]
            inl_keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton('-1', callback_data="minus"), 
            InlineKeyboardButton(f'✍️ {data[i][1]}', callback_data='handle_write'),
            InlineKeyboardButton('+1', callback_data="plus"),],[
            InlineKeyboardButton('⬅️', callback_data="left"), 
            InlineKeyboardButton(f'{i+1}/{len(data)}', callback_data='handle_write'),
            InlineKeyboardButton('➡️', callback_data="right"),]])
            caption=f'{data[i][0]}:\n{data[i][1]} quan.: {data[i][2]}*{data[i][1]} = {data[i][2]*data[i][1]}'
         
            if quer==0:
                update.bot.send_photo(chat_id=query.message.chat.id, photo=file_like2,caption=caption
,reply_markup=inl_keyboard)
            else:  
                    update.bot.edit_message_media(media=InputMediaPhoto(file_like2),chat_id=query.message.chat.id,
        message_id=query.message.message_id,)
                    update.bot.edit_message_caption(caption=caption,
        reply_markup=inl_keyboard,
        chat_id=query.message.chat.id,
        message_id=query.message.message_id)
                    

            

def plus_quan(bot, update):
        global edit_good
    
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        
        database="s352k345888bpm4d" )

        query = bot.callback_query
       
        
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888bpm4d" )

        query = bot.callback_query
        cursor = mydb.cursor()
   
        
        cursor.execute(f"UPDATE orders SET quantity=quantity+1 WHERE user_id={query.message.chat.id} and good='{edit_good}'")
        mydb.commit()
        
        cursor.execute(f"SELECT quantity FROM orders WHERE user_id={query.message.chat.id} and good='{edit_good}'")
        data=cursor.fetchone()
    
        cursor.close()
        mydb.close()

        edit_cart(bot, update,quer=query)



def minus_quan(bot, update):
        global edit_good
    
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        
        database="s352k345888bpm4d" )

        query = bot.callback_query
      
        
        mydb = pymysql.connect(
        host="esilxl0nthgloe1y.chr7pe7iynqr.eu-west-1.rds.amazonaws.com",
        user="ay1092ivipeccfsg",
        password="ylydt486n6y4z8nj",
        database="s352k345888bpm4d" )


        

        query = bot.callback_query
        cursor = mydb.cursor()
  
        
        cursor.execute(f"SELECT quantity FROM orders WHERE user_id={query.message.chat.id} and good='{edit_good}'")
        data=cursor.fetchone()

        if data[0]==1:
            return
        cursor.execute(f"UPDATE orders SET quantity=quantity-1 WHERE user_id={query.message.chat.id} and good='{edit_good}'")
        mydb.commit()
        
        cursor.execute(f"SELECT quantity FROM orders WHERE user_id={query.message.chat.id} and good='{edit_good}'")
        data=cursor.fetchone()
        
        cursor.close()
        mydb.close()

        edit_cart(bot, update,quer=query)

def on_right(bot, update):
        query = bot.callback_query
        global i
        i=i+1
        edit_cart(bot, update, quer=query)

def on_left(bot, update):
        query = bot.callback_query
        global i
        if i>0:
          i=i-1
        edit_cart(bot, update, quer=query)
            
       
    
   
       
       
        

        
        
       

       
    
  
