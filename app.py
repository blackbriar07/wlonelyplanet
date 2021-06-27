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
line_bot_api = LineBotApi('Tjt5lI9vDuapIysKHteqYa10gFLB+QFMYzv0UlvxfA7VcFh3Dz0/FcdmnAuEJ15G7sEr7wBrblfKeosNFNd9eqbgIueG1znQpmZ+4IBp6Yp9y6qKfqDvC1EvtMnVSecTWVWjPfoLqWax0zHARyv0mgdB04t89/1O/w1cDnyilFU=')
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
                                thumbnail_image_url='https://direct.rhapsody.com//imageserver//images//alb.298814091//500x500.jpg',
                                title='Hangouts Menu',
                                text='Please select',
                                actions=[
                                    PostbackTemplateAction(
                                        label='Group hangouts',
                                        text='looking for group......',
                                        data='action=buy&itemid=1'
                                    ),
                                    MessageTemplateAction(
                                        label='Solo hangout',
                                        text='looking for a solo person'
                                    ),
                                    URITemplateAction(
                                        label='listen to music',
                                        uri='https://www.youtube.com/watch?v=xNV38nq1fqc&t=1850s//'
                                    )
                                    
                                         
                                ]
                            )
                        )
   
    message_carousel = TemplateSendMessage(
                            alt_text='Carousel template',
                            template=CarouselTemplate(
                                columns=[
                                    CarouselColumn(
                                        thumbnail_image_url='https://dailyiowan.com/wp-content/uploads/2019/09/friends-900x600.jpeg',
                                        title='Hangouts',
                                        text='Want to hangout with a group or a solo person ..',
                                        actions=[
                                            PostbackTemplateAction(
                                                label='Group',
                                                text='looking for a group..',
                                                data='action=buy&itemid=1'
                                            ),
                                            MessageTemplateAction(
                                                label='Solo',
                                                text='looking for a person..'
                                            ),
                                            URITemplateAction(
                                                label='Access facebooks',
                                                uri='https://www.facebook.com/'
                                            )
                                        ]
                                    ),
                                    CarouselColumn(
                                        thumbnail_image_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/best-mobile-games-2020-1607968493.jpg',
                                        title='Games',
                                        text='Choose your online game',
                                        actions=[
                                            PostbackTemplateAction(
                                                label='Chess',
                                                text='opening chess',
                                                data='action=buy&itemid=2'
                                            ),
                                            MessageTemplateAction(
                                                label='Online soccer',
                                                text='opening FIFA'
                                            ),
                                            URITemplateAction(
                                                label='Sports News',
                                                uri='https://www.skysports.com/'
                            )
                                 CarouselColumn(
                                        thumbnail_image_url='https://vgywm.com/wp-content/uploads/2019/07/apple-music-note-800x420.jpg',
                                        title='Music',
                                        text='Choose your own music',
                                        actions=[
                                            URITemplateAction(
                                                label='Rock Music',
                                                uri='https://www.youtube.com/watch?v=26nsBfLXwSQ/'
                                            ),
                                           URITemplateAction(
                                                label='Contemporary Music',
                                                uri='https://www.youtube.com/watch?v=M6USc22nFnY/'
                                            ),
                                            URITemplateAction(
                                                label='Soothing Music',
                                                uri='https://www.youtube.com/watch?v=lFcSrYw-ARY/'
                                            )
                                        ]
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
        
    elif 'bye' in text:
        line_bot_api.reply_message(event.reply_token, message)
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "See you soon"))
    elif 'message' in text:
        line_bot_api.push_message(event.source.user_id, TextSendMessage(text = "hey !!! how are you people"))
    elif text == 'template':
        line_bot_api.reply_message(event.reply_token, templatemessage)
    elif text == 'carousel':
        line_bot_api.reply_message(event.reply_token, message_carousel)
    else :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "I am not being trained to understand you"))
        

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
    

@handler.add(MessageEvent, message = ImageMessage)
def handle_image_message(event):
    message = ImageSendMessage(original_content_url = 'https://www.atlasandboots.com/wp-content/uploads/2019/05/ama-dablam2-most-beautiful-mountains-in-the-world.jpg',
                               preview_image_url = 'https://www.atlasandboots.com/wp-content/uploads/2019/05/ama-dablam2-most-beautiful-mountains-in-the-world.jpg')
    
    line_bot_api.reply_message(event.reply_token,[TextSendMessage(text = "I am not being trained to understand you"), message])
    
    
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

