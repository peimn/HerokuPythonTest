import os
from flask import Flask
from flask_bcrypt import Bcrypt
import telegram
from telegram.ext import Updater

sec = 'asdaskjdhaufsf897987'
# Initialize application
app = Flask(__name__, static_folder=None)

# app configuration
app_settings = os.getenv(
    'APP_SETTINGS',
    'app.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

# Initialize Bcrypt
bcrypt = Bcrypt(app)

PORT = int(os.environ.get('PORT', '8443'))

#bot = telegram.Bot('765185530:AAGaBUP8CiLfzPhpfni2NcUfpUnPodm7oAg')
updater = Updater('765185530:AAGaBUP8CiLfzPhpfni2NcUfpUnPodm7oAg')
# add handlers
# updater.start_webhook(listen="0.0.0.0",
#                       port=PORT,
#                       url_path='765185530:AAGaBUP8CiLfzPhpfni2NcUfpUnPodm7oAg')
updater.bot.set_webhook("https://python20.herokuapp.com/" + '765185530:AAGaBUP8CiLfzPhpfni2NcUfpUnPodm7oAg')
updater.idle()

# Edit here below
@app.route("/"+sec)
def hello():
    return "Hello World!"

@app.route('/' + sec, methods=['POST'])
def webhook():
    update = telegram.update.Update.de_json(request.get_json(force=True))
    bot.sendMessage(chat_id=update.message.chat_id, text='Hello, there')

    return 'OK'