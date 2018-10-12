# encoding: utf-8
from flask import Flask, request, abort

import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import  *

from cht_package.config import line_channel_secret , line_channel_access_token

from text_input.olami import OLAMI_textInput



app = Flask(__name__)

handler = WebhookHandler(line_channel_secret) 
line_bot_api = LineBotApi(line_channel_access_token) 


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
        print("Audio message")

    #Image
    elif isinstance(event.message, ImageMessage):
        ext = 'jpg'
        print("Image message")
    
    

# ================= 機器人區塊 End =================

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
