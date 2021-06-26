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
line_bot_api = LineBotApi('9BkAFtijid+S87QPydJft3Ghk9MOqhzTtzsuZcbrgJKa0tJYEJTPvTFG7RpUsq4J7sEr7wBrblfKeosNFNd9eqbgIueG1znQpmZ+4IBp6YqxvJ1S68GjxLCxxmbSCm8VbgOFS7y/JZnihGkpZ+KBlwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('0d51997be1f1783bd6e93132a016a290')

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
    text = (event.message.text).lower()
    message = ImageSendMessage(original_content_url = 'https://image.freepik.com//free-vector//bye-bye-flag-grahpic-old-vintage-trendy-flag-with-text-bye-bye-vintage-banner-with-ribbon-flag-grahpic-hand-drawn_136321-1593.jpg',
                               preview_image_url = 'https://image.freepik.com//free-vector//bye-bye-flag-grahpic-old-vintage-trendy-flag-with-text-bye-bye-vintage-banner-with-ribbon-flag-grahpic-hand-drawn_136321-1593.jpg')
    
    templatemessage = TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                thumbnail_image_url='https://example.com/image.jpg',
                                title='Menu',
                                text='Please select',
                                actions=[
                                    PostbackTemplateAction(
                                        label='postback',
                                        text='postback text',
                                        data='action=buy&itemid=1'
                                    ),
                                    MessageTemplateAction(
                                        label='message',
                                        text='message text'
                                    ),
                                    URITemplateAction(
                                        label='uri',
                                        uri='http://example.com/'
                                    )
                                ]
                            )
                        )
    if 'hi' in text or 'hello' in text :
        profile = line_bot_api.get_profile(event.source.user_id)
        #if isinstance(event.source, SourceUser):
            
            #line_bot_api.reply_message(event.reply_token, [ TextSendMessage(text='Display name: ' +profile.display_name),TextSendMessage(text='Status message: ' +profile.status_message)])
        #else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "Hi "+ profile.display_name ))
        
    elif text == 'bye':
        line_bot_api.reply_message(event.reply_token, message)
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "See you soon"))
    elif text == 'message':
        line_bot_api.push_message(push_token, TextSendMessage(text = "hey !!! how are you people"))
    elif text == 'template':
        line_bot_api.reply_message(event.reply_token, templatemessage)
        

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        LocationSendMessage(
            title='Location', address=event.message.address,
            latitude=event.message.latitude, longitude=event.message.longitude
        )
    )

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )
    

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

