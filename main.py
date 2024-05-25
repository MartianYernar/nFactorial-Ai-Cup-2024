import telebot
import time
from telebot import types
import requests
from bs4 import BeautifulSoup
from bot import get_news
from bot import get_links
from bot import get_cryp
from ultralytics import YOLO
# import numpy


config = '6993472927:AAEiaBZKSK68KAE74jUezlxL6boW8KG_jKM'
bot = telebot.TeleBot(config)

model = YOLO('best.pt')

@bot.message_handler(commands=['start'])
def welcome(message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		item1 = types.KeyboardButton("🪙 Crypto News Analysis")
		item2 = types.KeyboardButton("💹 Crypto Stock Analysis")
		markup.add(item1, item2)

		bot.send_message(message.chat.id, "Welcome {0.first_name}, CryptoHelper is a bot that will help you to make decisions to sell or to buy cryptocurrency 💸".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text(message):
	if message.chat.type == 'private':
		if message.text == '🪙 Crypto News Analysis':
									# news = get_news()
									links = get_links()
									cryps = get_cryp()
									for i in range(5):
										bot.send_message(message.chat.id, cryps[i].text + ' ↗️' + '\n' + '\n' + links[i]['href'])
				
		elif message.text == '💹 Crypto Stock Analysis':
			sent = bot.send_message(message.chat.id, "Please, send me picture of stock, charts")
			bot.register_next_step_handler(sent, handle_photo)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):

    photo_file_id = message.photo[-1].file_id
    # Get the File object from the file ID
    file_info = bot.get_file(photo_file_id)
    # Download the photo
    downloaded_file = bot.download_file(file_info.file_path)
    
    # Define a path to save the photo
    with open("received_photo.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

	  
    results = model("received_photo.jpg")
    for result in results:
       id = result.probs.top1
    name = result.names[id]
#     names_dict = results[0].names
#     probs = results[0].probs.to_list()
#     res = names_dict[numpy.argmax(probs)]
    if name == "DOWN":
        name="Sell ↘️"
    elif name == "UP":
        name="Buy ↗️"
    
    bot.reply_to(message, name)


# @bot.callback_query_handler(func=lambda callback: callback.data)
# def check_callback(callback):
#     if callback.data == 'News':
#         bot.send_message(callback.message.chat.id, "Bitcoin ⬇️") 
#     elif callback.data == 'Stock':
#         bot.send_message(callback.message.chat.id, "CAD/USD ⬆️")


if __name__ == "__main__":
		bot.polling(none_stop=True)