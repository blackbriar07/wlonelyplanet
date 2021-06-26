from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('4wiAT/cN++uvxW2INvKlHBAdblgn9kjJlYqgi53RFOiv05riKDHv9cVSEuIM12CR7sEr7wBrblfKeosNFNd9eqbgIueG1znQpmZ+4IBp6YqT3XVC8tUNsqMiwIXcEL/2qXLZEp4+UWjQzfbx8WcbkgdB04t89/1O/w1cDnyilFU=')
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

@handler.add(MessageEvent, message = TextMessage)
def handle_text_message(event):
    text = event.message.text
    if text == 'hi' or text == 'hello':
        profile = line_bot_api.get_profile(event.source.user_id)
        #if isinstance(event.source, SourceUser):
            
            #line_bot_api.reply_message(event.reply_token, [ TextSendMessage(text='Display name: ' +profile.display_name),TextSendMessage(text='Status message: ' +profile.status_message)])
        #else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "Hi "+ profile.display_name))
    elif text == 'bye':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "leaving"))
'''
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = (event.message.text).lower()
    if 'hello' in msg_from_user:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="hello !! How are you ?"))
    elif 'I am good' in msg_from_user:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="thats awesome"))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="I did not understand "))
'''
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()

