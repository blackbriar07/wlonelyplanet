from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('W0kpMYKyDVQexqkB1N7uxHklOy1Q+bh4Qt8AuSuD40pobqiSL4SwR0PCUO/xYXrT7sEr7wBrblfKeosNFNd9eqbgIueG1znQpmZ+4IBp6Yq79knOKgMZBZTD8WFH8G0Xj8kJFBnkOu8SUuXHM5ahaAdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('e23a85130af721661255f935d54705ed')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #msg_from_user = event.message.text
    #if msg_from_user == 'hi' or msg_from_user == 'hello' or msg_from_user == 'Hi' or msg_from_user == 'Hello':
    #    line_bot_api.reply_message(event.reply_token, TestSendMessage(text = "Yo whats up ?")
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

