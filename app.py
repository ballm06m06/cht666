# encoding: utf-8
from flask import Flask, request, abort
import json
import tempfile, os
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import  *

from cht_package.config import line_channel_secret , line_channel_access_token

from text_input.olami import OLAMI_textInput

from cht_package.postgreSQL import register_User

from cht_package.audioConvert import toWAV

app = Flask(__name__)

handler = WebhookHandler(line_channel_secret) 
line_bot_api = LineBotApi(line_channel_access_token) 

static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

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
    
    # Text 
    if isinstance(event.message, TextMessage):
        msg = event.message.text #message from user
    
        #OLAMI TEXT
        olamiJson = json.loads(OLAMI_textInput(msg))
        response = olamiJson["data"]["nli"][0]["desc_obj"]["result"]
        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=response))

    #Audio
    elif isinstance(event.message, AudioMessage):
        ext = 'm4a'
        print("Audio message id:" + event.message.id)

        audio_content = line_bot_api.get_message_content(event.message.id)
        
        with tempfile.NamedTemporaryFile(dir=static_tmp_path, prefix=ext + '-', delete=False) as tf:
            for chunk in audio_content.iter_content():
                tf.write(chunk)
            tempfile_path = tf.name
        print('static_tmp_path: '+static_tmp_path)
        #print('tempfile_path: '+tempfile_path) /app/static/tmp/m4a-48lboo6w new
        dist_path = tempfile_path + '.' + ext
        dist_name = os.path.basename(dist_path)
        #print('dist_path: '+dist_path) /app/static/tmp/m4a-48lboo6w.m4a old
        #print('distname: '+dist_name) m4a-48lboo6w.m4a
        
        #os.rename(tempfile_path, dist_path)

        path = os.path.join('static', 'tmp', dist_name)
        
        new_path = toWAV(dist_path, tempfile_path)
        
        print('聲音路徑：'+ new_path)

        os.remove(new_path)
    #Image
    elif isinstance(event.message, ImageMessage):
        ext = 'jpg'
        print("Image message")



@handler.add(FollowEvent)
def handle_follow(event):
    #Register
    if isinstance(event.source, SourceUser) or isinstance(event.source, SourceGroup) or isinstance(event.source, SourceRoom):
        profile = line_bot_api.get_profile(event.source.user_id)
        #print(profile.display_name)

        if register_User(profile.user_id, profile.display_name, profile.picture_url):
            line_bot_api.reply_message(event.reply_token,[
                TextSendMessage(text=profile.display_name+' 歡迎加入'),
                StickerSendMessage(package_id=2,sticker_id=176),
            ] )



# ================= 機器人區塊 End =================

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
