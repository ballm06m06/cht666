
# encoding: utf-8
#heroku buildpacks:clear

from flask import Flask, request, abort
import json
import tempfile, os, sys

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,VideoSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton
)

from cht_package.config import line_channel_secret, line_channel_access_token
from bot.template import skip_list, btn_template, carousel_template
from text_input.olami import OLAMI_textInput
from audio_input.olami_audio import OLAMI_audioInput
from dialogflow.nlp import get_intent, get_district

from cht_package.db_postgres import register_User

from cht_package.audioConvert import toWAV
app = Flask(__name__)

handler = WebhookHandler(line_channel_secret) 
line_bot_api = LineBotApi(line_channel_access_token) 

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

#first add
first_add = False

@app.route('/')
def index():
    return "<p>Hello cht!</p>"

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

# ================= 機器人區塊 Start =================
@handler.add(MessageEvent, message=(TextMessage, ImageMessage, AudioMessage))
def handle_message(event):
    
    
    if isinstance(event.source, SourceUser) or isinstance(event.source, SourceGroup) or isinstance(event.source, SourceRoom):
        profile = line_bot_api.get_profile(event.source.user_id)

     # Text 
    if isinstance(event.message, TextMessage):
        msg = event.message.text #message from user

        global first_add
        if first_add == True:
            
            #register
            first_addFriend(msg, profile.user_id, profile.display_name, profile.picture_url)

            #intro
            return 0

        #quick reply test
        if msg == '123':
            line_bot_api.reply_message(
            event.reply_token,[
            TextSendMessage(
                text=profile.display_name+'你喜歡哪一個呢？',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=PostbackAction(label="postback", data="data1")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="label2", text="text2")
                        ),
                        QuickReplyButton(
                            action=DatetimePickerAction(label="label3",
                                                        data="date_postback",
                                                        mode="date")
                        ),
                        QuickReplyButton(
                            action=CameraAction(label="label4")
                        ),
                        QuickReplyButton(
                            action=CameraRollAction(label="label5")
                        ),
                        QuickReplyButton(
                            action=LocationAction(label="label6")
                        ),
                    ]))]
                    )
            return 0

        #flex test
        elif msg == 'flex':
            
            bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://example.com/cafe.jpg',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://example.com', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Brown Cafe', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            TextComponent(text='4.0', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Place',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Shinjuku, Tokyo',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Time',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="10:00 - 23:00",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # callAction, separator, websiteAction
                    SpacerComponent(size='sm'),
                    # callAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='CALL', uri='tel:000000'),
                    ),
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='WEBSITE', uri="https://example.com")
                    )
                ]
            ),
        )
            message = FlexSendMessage(alt_text="hello", contents=bubble)
            line_bot_api.reply_message(
                event.reply_token,
                message
            )
            return 0

        elif msg == 'btntem':
            line_bot_api.reply_message(
                event.reply_token,
                btn_template('hihi', 'hi', 'https://i.imgur.com/Wiqlff7.png', 'func1', 'func1', 'fun1'\
                , 'func2', 'func2', 'func2', 'func3', 'func3', 'func3')
            )
            return 0
        
        elif msg == 'ctem':
            line_bot_api.reply_message(
                event.reply_token,
                carousel_template()
            )
            return 0
        #get user intent
        get_userIntent(profile.user_id, msg)

    #Audio
    elif isinstance(event.message, AudioMessage):
        ext = 'm4a'
        #print("Audio message id:" + event.message.id)
        #waiting for recognition
        if isinstance(event.source, SourceUser) or isinstance(event.source, SourceGroup) or isinstance(event.source, SourceRoom):
            profile = line_bot_api.get_profile(event.source.user_id)
            
            line_single_push(profile.user_id, '解析中...')
        
        audio_content = line_bot_api.get_message_content(event.message.id)
        
    
        with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
            for chunk in audio_content.iter_content():
                tf.write(chunk)
            tempfile_path = tf.name
        #print('static_tmp_path: '+static_tmp_path)
        #print('tempfile_path: '+tempfile_path) /app/static/tmp/m4a-48lboo6w new
        dist_path = tempfile_path + '.' + ext
        dist_name = os.path.basename(dist_path)
        #print('dist_path: '+dist_path) /app/static/tmp/m4a-48lboo6w.m4a old
        #print('distname: '+dist_name) m4a-48lboo6w.m4a

        new_dist_path = tempfile_path + '.wav'
        new_dist_name = os.path.basename(new_dist_path)
        new_path = os.path.join('static', 'tmp', new_dist_name)
        
        os.rename(tempfile_path, dist_path)

        path = os.path.join('static', 'tmp', dist_name)
        print('.m4a path: '+path)

        new_path = toWAV(path, new_path)
        print('.wav path:'+new_path)

        #OLAMI Audio
        olamiJson = json.loads(OLAMI_audioInput(new_path))
        response = olamiJson["data"]["asr"]["result"]

        """line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='你說的是: '+response))"""
        #get user intent
        get_userIntent(profile.user_id, response)

        os.remove(new_path)
        print('.wav audio file remove ok')
    #Image
    elif isinstance(event.message, ImageMessage):
        ext = 'jpg'
        print("Image message")



@handler.add(FollowEvent)
def handle_follow(event):

    global first_add
    first_add = True

    #Register
    if isinstance(event.source, SourceUser) or isinstance(event.source, SourceGroup) or isinstance(event.source, SourceRoom):
        profile = line_bot_api.get_profile(event.source.user_id)
        #print(profile.display_name)
       
        line_bot_api.reply_message(event.reply_token,[
            TextSendMessage(text=profile.display_name+'您好！我是您的小幫手元元'),
            StickerSendMessage(package_id=1,sticker_id=410),
            TextSendMessage(text='為了提供更精確的服務\n元元需要您的所在地\n(例:新竹市)',
                quick_reply=QuickReply(
                    items=[
                        QuickReplyButton(
                            action=MessageAction(label="臺北市", text="臺北市")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="桃園市", text="桃園市")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="新竹市", text="新竹市")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="臺中市", text="臺中市")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="臺南市", text="臺南市")
                        ),
                        QuickReplyButton(
                            action=MessageAction(label="高雄市", text="高雄市")
                        )
                    ]))
            ] )


#handle postback
@handler.add(PostbackEvent)
def handle_postback(event):

    msg = event.postback.data
    print('post back:'+msg)

    if msg == 'ping':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='pong'))
    elif msg == 'datetime_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['datetime']))
    elif msg == 'date_postback':
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.postback.params['date']))

#push text
def line_single_push(id,txt):
    line_bot_api.push_message(id, 
        TextSendMessage(text=txt))
    
#push sticker    
def line_single_sticker(id, packed_id, sticker_id):
    line_bot_api.push_message(id, 
        StickerSendMessage(package_id=packed_id,
    sticker_id=sticker_id))

#push video    
def line_single_video(id, content, preview):
    line_bot_api.push_message(id, 
        VideoSendMessage(original_content_url=content,
    preview_image_url=preview))

#multicast
def line_multicast(mlist, txt):
    line_bot_api.multicast(mlist, TextSendMessage(text=txt))

#register
def first_addFriend(msg, id , name, url):

    area_code = 100
    global first_add

    while True:
        
        area_code = get_district(msg)

        if area_code != 100 and area_code != 'none':
            print(name+' district code: '+ str(area_code))
            first_add = False

             #註冊完給intro
            if register_User(id, name, url, int(area_code)):
                
                line_single_push(id, '感謝您提供的資訊')
                line_single_sticker(id, 1, 106)
            break

        else:
            line_single_push(id, '為了提供更精確的服務，以獲得完善的體驗\n元元需要您的所在地\n(例:新竹市)')
            line_single_sticker(id, 1, 4)
        return
        
#get user intent
def get_userIntent(id, msg):
    
    intent = get_intent(msg)

    #特定text不進入OLAMI
    if msg in skip_list: 
        return 0

    elif intent == '水質資訊':
        line_single_push(id, 'intent:水質資料')
            
    elif intent == '溫度':
        line_single_push(id, 'intent:溫度')

    elif intent == '酸鹼度':
        line_single_push(id, 'intent:酸鹼度')
        
    elif intent == '溶氧量':
        line_single_push(id, 'intent:溶氧量')
    
    elif intent == '氣象':
        line_single_push(id, 'intent:氣象')
        '''try:
            #OLAMI get weather info
            olamiJson = json.loads(OLAMI_textInput(msg))
            #response = olamiJson["data"]["nli"][0]["desc_obj"]["result"]
            test = olamiJson["data"]["nli"][0]["data_obj"][0]
            line_single_push(id, test)

        except Exception as e:
            print('get weather info exception:'+str(e))'''

    # intent: none >> OLAMI(天氣、閒聊...)
    else:
        #OLAMI TEXT
        olamiJson = json.loads(OLAMI_textInput(msg))
        response = olamiJson["data"]["nli"][0]["desc_obj"]["result"]
        #test = olamiJson["data"]["nli"][0]["data_obj"][0]


        line_single_push(id, response)
            
        return 0 
    
   


# ================= 機器人區塊 End =================

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
