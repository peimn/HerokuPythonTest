import os
from flask import Flask
from flask_bcrypt import Bcrypt
import telegram

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

bot = telegram.Bot(app.config.DevelopmentConfig.TOKEN)

# Edit here below
@app.route("/"+sec)
def hello():
    return "Hello World!"

@app.route('/' + sec, methods=['POST'])
def webhook():
    update = telegram.update.Update.de_json(request.get_json(force=True))
    bot.sendMessage(chat_id=update.message.chat_id, text='Hello, there')

    return 'OK'

def setWebhook():
    bot.setWebhook(webhook_url='https://%s:%s/%s' % (app.config.DevelopmentConfig.HOST, app.config.DevelopmentConfig.PORT, sec),
                   certificate=open(CERT, 'rb'))