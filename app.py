from flask import Flask, request, abort
import os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('9P6VQZJkVC+bcxbV8unWIrY/bp2Uy9X988Y3OWLx62EVTrW3JegN5pO9mpeF0H0E7sEr7wBrblfKeosNFNd9eqbgIueG1znQpmZ+4IBp6YqsWtwdRQzNtu5KKuxo3NBrBtyZdQYuP139mKoays3tsQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('e00dc2b8e64c1337c7995a7b1adc14d6')

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
    profile = line_bot_api.get_profile(event.source.user_id)
    message = ImageSendMessage(original_content_url = 'https://image.freepik.com//free-vector//bye-bye-flag-grahpic-old-vintage-trendy-flag-with-text-bye-bye-vintage-banner-with-ribbon-flag-grahpic-hand-drawn_136321-1593.jpg',
                               preview_image_url = 'https://image.freepik.com//free-vector//bye-bye-flag-grahpic-old-vintage-trendy-flag-with-text-bye-bye-vintage-banner-with-ribbon-flag-grahpic-hand-drawn_136321-1593.jpg')
    
    ImageCarouselmessage = TemplateSendMessage(
                                alt_text='ImageCarousel template',
                                template=ImageCarouselTemplate(
                                    columns=[
                                        ImageCarouselColumn(
                                            image_url='https://terrigen-cdn-dev.marvel.com/content/prod/1x/theavengers_lob_crd_03.jpg',
                                            action=PostbackTemplateAction(
                                                label='Avengers',
                                                text='Calling avengers',
                                                data='action=buy&itemid=1'
                                            )
                                        ),
                                        ImageCarouselColumn(
                                            image_url='https://media.comicbook.com/2018/01/the-cw-arrowverse-1079043.jpeg',
                                            action=PostbackTemplateAction(
                                                label='DC',
                                                text='Calling DC superheroes',
                                                data='action=buy&itemid=2'
                                            )
                                        )
                                    ]
                                )
                            )
    ImageCarouselmessage_health = TemplateSendMessage(
                                alt_text='ImageCarousel template',
                                template=ImageCarouselTemplate(
                                    columns=[
                                        ImageCarouselColumn(
                                            image_url='https://images-na.ssl-images-amazon.com/images/I/71YfSBUDHYL._AC_SL1500_.jpg',
                                            action=PostbackTemplateAction(
                                                label='Blood pressure',
                                                text='Thank you',
                                                data='action=buy&itemid=1'
                                            )
                                        ),
                                        ImageCarouselColumn(
                                            image_url='https://5.imimg.com/data5/YT/QD/MY-41264905/blood-glucose-monitor-500x500.jpg',
                                            action=PostbackTemplateAction(
                                                label='Sugar Monitor',
                                                text='Thank you',
                                                data='action=buy&itemid=2'
                                            )
                                        )
                                    ]
                                )
                            )
    
    ImageCarouselmessage1 = TemplateSendMessage(
                                alt_text='ImageCarousel template',
                                template=ImageCarouselTemplate(
                                    columns=[
                                        ImageCarouselColumn(
                                            image_url='https://is5-ssl.mzstatic.com/image/thumb/Purple124/v4/d5/6c/ad/d56cadca-8767-c011-2fa8-b374bff03bbb/source/512x512bb.jpg',
                                            action=PostbackTemplateAction(
                                                label='Truth and Dare',
                                                text='The questions continue..',
                                                data='action=buy&itemid=1'
                                            )
                                        ),
                                        ImageCarouselColumn(
                                            image_url='https://winn-hub.com/assets/img/content/gallery/large/701.jpg',
                                            action=PostbackTemplateAction(
                                                label='Who knows who better',
                                                text='The questions continue..',
                                                data='action=buy&itemid=2'
                                            )
                                        )
                                    ]
                                )
                            )
    
    confirmmessage = TemplateSendMessage(
                            alt_text='Confirm template',
                            template=ConfirmTemplate(
                                text= "Hi "+ profile.display_name + ". What's up ? how are you feeling ?",
                                actions=[
                                    PostbackTemplateAction(
                                        label='Great',
                                        text='I am feeling great',
                                        data='action=buy&itemid=1'
                                    ),
                                    MessageTemplateAction(
                                        label='Not that great',
                                        text= 'Not great'
                                        
                                    )
                                ]
                            )
                        )
    '''
    confirmmessage1 = TemplateSendMessage(
                            alt_text='Confirm template',
                            template=ConfirmTemplate(
                                text= "Uhh... Not that great without you. Would you like to talk about it ? ",
                                actions=[
                                    PostbackTemplateAction(
                                        label='Yes',
                                        text='yes. I will surely do.',
                                        data='action=buy&itemid=1'
                                    ),
                                    MessageTemplateAction(
                                        label='No',
                                        text='Sorry. not in the mood.'
                                    )
                                ]
                            )
                        )
    '''

    confirmmessage_great = TemplateSendMessage(
                            alt_text='Confirm template',
                            template=ConfirmTemplate(
                                text= "Sorry to hear that. Would you like to talk about it ?",
                                actions=[
                                    PostbackTemplateAction(
                                        label='Yes',
                                        text='Yes',
                                        data='action=buy&itemid=1'
                                    ),
                                    MessageTemplateAction(
                                        label='No',
                                        text='No'
                                    )
                                ]
                            )
                        )
    confirmmessage_notgreat = TemplateSendMessage(
                            alt_text='Confirm template',
                            template=ConfirmTemplate(
                                text= "Its good to hear that. You can spread your Happiness with others. Would you like to hangout with someone ?",
                                actions=[
                                    PostbackTemplateAction(
                                        label='Yes',
                                        text='yes',
                                        data='action=buy&itemid=1'
                                    ),
                                    MessageTemplateAction(
                                        label='No',
                                        text='no'
                                    )
                                ]
                            )
                        )
    confirmmessage_sick = TemplateSendMessage(
                            alt_text='Confirm template',
                            template=ConfirmTemplate(
                                text= "Are you feeling sick ? ",
                                actions=[
                                    PostbackTemplateAction(
                                        label='Yes',
                                        text='sick',
                                        data='action=buy&itemid=1'
                                    ),
                                    MessageTemplateAction(
                                        label='No',
                                        text='Not sick'
                                    )
                                ]
                            )
                        )
    confirmmessage_stressed = TemplateSendMessage(
                            alt_text='Confirm template',
                            template=ConfirmTemplate(
                                text= "Are you feeling stressed ?",
                                actions=[
                                    PostbackTemplateAction(
                                        label='Yes',
                                        text='Stressed',
                                        data='action=buy&itemid=1'
                                    ),
                                    MessageTemplateAction(
                                        label='No',
                                        text='Not stressed'
                                    )
                                ]
                            )
                        )

    confirmmessage_lonely = TemplateSendMessage(
                            alt_text='Confirm template',
                            template=ConfirmTemplate(
                                text= "Are you feeling lonely ?",
                                actions=[
                                    PostbackTemplateAction(
                                        label='Yes',
                                        text='lonely',
                                        data='action=buy&itemid=1'
                                    ),
                                    MessageTemplateAction(
                                        label='No',
                                        text='Not lonely'
                                    )
                                ]
                            )
                        )
    
    messageb = TemplateSendMessage(
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
    bmessage = TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                thumbnail_image_url='https://www.e-spincorp.com//wp-content//uploads//2017//10//industry-media-entertainment.jpg',
                                title='What would you like to do ? ..',
                                text='That is Awesome. Please select',
                                actions=[
                                    URITemplateAction(
                                        label='Watch some Movies',
                                        uri='https://www.netflix.com//tw-en//'
                                    ),
                                    URITemplateAction(
                                        label='listen to music',
                                        uri='https://www.youtube.com//watch?v=xNV38nq1fqc&t=1850s//'
                                    ),
                                    PostbackTemplateAction(
                                        label='See your health status',
                                        text='Health Status',
                                        data='action=buy&itemid=1'
                                    )                               
                                                                             
                                ]
                            )
                        )
    message_stressed = TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                thumbnail_image_url='https://www.e-spincorp.com//wp-content//uploads//2017//10//industry-media-entertainment.jpg',
                                title='What would you like to do ? ..',
                                text='That is Awesome. Please select',
                                actions=[
                                    URITemplateAction(
                                        label='Watch some Movies',
                                        uri='https://www.netflix.com//tw-en//'
                                    ),
                                    URITemplateAction(
                                        label='listen to music',
                                        uri='https://www.youtube.com//watch?v=xNV38nq1fqc&t=1850s//'
                                    )                            
                                                                             
                                ]
                            )
                        )

    message_lonely = TemplateSendMessage(
                            alt_text='Buttons template',
                            template=ButtonsTemplate(
                                thumbnail_image_url='https://www.relocationsrs.com.mx/wp-content/uploads/2019/11/blog3-720x340.jpg',
                                title='You can socialize physically or virtually. please select',
                                text='That is Awesome. Please select',
                                actions=[
                                   PostbackTemplateAction(
                                        label='Call a friend to hangout physically',
                                        text='Calling a friend',
                                        data='action=buy&itemid=1'
                                    ),
                                    URITemplateAction(
                                        label='Social Networking site',
                                        uri='https://www.facebook.com/'
                                    ),
                                    PostbackTemplateAction(
                                        label='Please click on the camera option to hangout virtually',
                                        text='Virtual Hangout',
                                        data='action=buy&itemid=1'
                                    )                             
                                                                             
                                ]
                            )
                        )
    '''
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
                                        ]
                                    ),
                                    
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
    '''
    ImageCarouselmeddoc = TemplateSendMessage(
                                alt_text='ImageCarousel template',
                                template=ImageCarouselTemplate(
                                    columns=[
                                        ImageCarouselColumn(
                                            image_url='https://ichef.bbci.co.uk/news/976/cpsprodpb/15DA3/production/_115370598_tv038457905.jpg',
                                            action=URITemplateAction(
                                                    label='Medicine',
                                                    uri='https://www.medlife.com/'
                                            )
                                        ),
                                        ImageCarouselColumn(
                                            image_url='https://bralowmedicalgroup.com/wp-content/uploads/2018/06/blog.jpg',
                                            action=URITemplateAction(
                                                    label='Doctor',
                                                    uri='https://mdlnext.mdlive.com/'
                                            )
                                        )
                                    ]
                                )
                            )
    
    message_sick = TemplateSendMessage(
                            alt_text='Carousel template',
                            template=CarouselTemplate(
                                columns=[
                                    CarouselColumn(
                                        thumbnail_image_url='https://dailyiowan.com/wp-content/uploads/2019/09/friends-900x600.jpeg',
                                        title='Fever',
                                        text='Do you want medicine or doctor ?',
                                        actions=[
                                            PostbackTemplateAction(
                                                label='Take temperature',
                                                text='Your temperature is 90.6 F',
                                                data='action=buy&itemid=2'
                                            ),
                                            URITemplateAction(
                                                label='Medicine online',
                                                uri='https://www.netmeds.com/prescriptions/dolo-650mg-tablet-15-s/'
                                            ),
                                            URITemplateAction(
                                                label='Consult a doctor',
                                                uri='https://mdlnext.mdlive.com/'
                                            )
                                        ]
                                    ),
                                    CarouselColumn(
                                        thumbnail_image_url='https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/best-mobile-games-2020-1607968493.jpg',
                                        title='Cold/Cough',
                                        text='Do you want medicine or doctor ?',
                                        actions=[
                                            PostbackTemplateAction(
                                                label='Take temperature',
                                                text='Your temperature is 89.6 F',
                                                data='action=buy&itemid=2'
                                            ),
                                            URITemplateAction(
                                                label='Medicine online',
                                                uri='https://www.netmeds.com/prescriptions/cold-nova-capsule-10-s/'
                                            ),
                                            URITemplateAction(
                                                label='Consult a doctor',
                                                uri='https://mdlnext.mdlive.com/'
                                            )
                                        ]
                                    ),
                                    
                                 CarouselColumn(
                                        thumbnail_image_url='https://vgywm.com/wp-content/uploads/2019/07/apple-music-note-800x420.jpg',
                                        title='Others',
                                        text='Please visit a doctor or consult one',
                                        actions=[
                                            URITemplateAction(
                                                label='Consult a doctor',
                                                uri='https://mdlnext.mdlive.com/'
                                            ),                                            
                                           PostbackTemplateAction(
                                                label='Doctor Clinic',
                                                text='Please click on the doctor clinic in the quick reply',
                                                data='action=buy&itemid=2'
                                            )        
                                        ]
                                 )
                                ]
                            )
                        )
    '''
    message_sick = TemplateSendMessage(
                            alt_text='Carousel template',
                            template=CarouselTemplate(
                                columns=[
                                    CarouselColumn(
                                        thumbnail_image_url='https://medlineplus.gov/images/Fever.jpg',
                                        title='Fever',
                                        text='Do you want medicine or doctor ?',
                                        actions=[
                                            PostbackTemplateAction(
                                                label='Take temperature',
                                                text='Your temperature is 90.6 F',
                                                data='action=buy&itemid=2'
                                            ),
                                            URITemplateAction(
                                                label='Medicine online',
                                                uri='https://www.netmeds.com/prescriptions/dolo-650mg-tablet-15-s'
                                            ),
                                            URITemplateAction(
                                                label='Consult a doctor',
                                                uri='https://mdlnext.mdlive.com/'
                                            )
                                            
                                        ]
                                    ),
                                    CarouselColumn(
                                        thumbnail_image_url='https://sobeyspharmacy.com/wp-content/uploads/2016/03/CoughCold-page.png',
                                        title='Cold/Cough',
                                        text='Do you want medicine or doctor ?',
                                        actions=[
                                            PostbackTemplateAction(
                                                label='Take temperature',
                                                text='Your temperature is 89.6 F',
                                                data='action=buy&itemid=2'
                                            ),
                                            URITemplateAction(
                                                label='Medicine online',
                                                uri='https://www.netmeds.com/prescriptions/cold-nova-capsule-10-s'
                                            ),
                                            URITemplateAction(
                                                label='Consult a doctor',
                                                uri='https://mdlnext.mdlive.com/'
                                            )
                                        ]
                                    ),
                                    
                                 CarouselColumn(
                                        thumbnail_image_url='https://vgywm.com/wp-content/uploads/2019/07/apple-music-note-800x420.jpg',
                                        title='Others',
                                        text='Please visit a doctor or consult one',
                                        actions=[
                                             URITemplateAction(
                                                label='Consult a doctor',
                                                uri='https://mdlnext.mdlive.com/'
                                            ),                                            
                                           PostbackTemplateAction(
                                                label='Doctor Clinic',
                                                text='Please click on the doctor clinic in the quick reply',
                                                data='action=buy&itemid=2'
                                            )                                         
                                            
                                        ]
                                 )
                                ]
                            )
                        )
    '''
    
    if 'hi' in text or 'hello' in text :
        line_bot_api.reply_message(event.reply_token, confirmmessage)
    elif 'great' in text:
        line_bot_api.reply_message(event.reply_token, confirmmessage_great)
        #line_bot_api.reply_message(event.reply_token, bmessage)
    elif 'right' in text:
        line_bot_api.reply_message(event.reply_token, bmessage)
    elif 'health' in text:
        line_bot_api.reply_message(event.reply_token, ImageCarouselmessage_health)
    elif text == 'not great':
        line_bot_api.reply_message(event.reply_token, confirmmessage_notgreat)
    elif text == 'yes':
        line_bot_api.reply_message(event.reply_token, confirmmessage_sick)
    elif text == 'not sick':
        line_bot_api.reply_message(event.reply_token, confirmmessage_stressed)
    elif text == 'sick' :
        line_bot_api.reply_message(event.reply_token, message_sick)
    elif text == 'stressed' :
        line_bot_api.reply_message(event.reply_token, message_stressed)
    elif text == 'not stressed':
        line_bot_api.reply_message(event.reply_token, confirmmessage_lonely)
    elif text == 'lonely':
        line_bot_api.reply_message(event.reply_token, message_lonely)
    elif 'hangout' in text:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "Please click the virtual camera option to virtually meet friends"))
    elif 'bye' in text:
        line_bot_api.reply_message(event.reply_token, message)
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "See you soon"))
    elif 'message' in text:
        line_bot_api.push_message(event.source.user_id, TextSendMessage(text = "hey !!! how are you people"))
    elif 'chat' in text:
        #line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "oh yes"))
        line_bot_api.reply_message(event.reply_token, ImageCarouselmessage)
    elif 'surely' in text:
        line_bot_api.reply_message(event.reply_token, ImageCarouselmessage)
    elif text == 'carousel':
        line_bot_api.reply_message(event.reply_token, message_carousel)
    elif 'confirm' in text:
        line_bot_api.reply_message(event.reply_token, confirmmessage)
    elif 'imagec' in text:
        line_bot_api.reply_message(event.reply_token, ImageCarouselmessage)
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
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
