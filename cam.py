import picamera
import os

from telegram.bot import Bot
from telegram.utils.request import Request
from telegram.ext import Updater, CommandHandler


def sendPic():
	camera = picamera.PiCamera()

	# set the resolution
	camera.resolution = (640, 480)

	# take a photo
	camera.capture('photo.jpg')
	camera.close()

	# create a bot object
	request = Request(con_pool_size=8)
	bot = Bot(token='******************', request=request)

	# send the photo
	with open('photo.jpg', 'rb') as photo:
    		bot.send_photo(chat_id='*********', photo=photo)

# create a bot object
updater = Updater(token='******************')
dispatcher = updater.dispatcher

# define a function that will be called when a /start command is received
def photo(update, context):
	if update.message.chat_id != *********:
		context.bot.send_message(chat_id=update.message.chat_id, text="Sorry you wont get a photo. Instead it is sent to myself")
	sendPic()

# create a CommandHandler that will handle the /start command
start_handler = CommandHandler('photo', photo)

# add the handler to the dispatcher
dispatcher.add_handler(start_handler)

# start the bot
updater.start_polling()
