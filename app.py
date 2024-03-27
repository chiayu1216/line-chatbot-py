from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi('DZMwqG6Z42GF7IGVlNA893Ob9EvriIiAYQl0r52Jbp2eJbA+n7h5t+uNscUu8Y/CF7mM1oOSwi5utrqLpgOaiOTyBv8fsSbTCwkQs2W/qeDVwKHWrI+jsM9XnAoey/6St2k/QCEVcGDLxwOZteN34AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1534028a03cd1c14888cb554f03358f2')


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)