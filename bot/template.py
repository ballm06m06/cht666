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
import datetime
from cht_package.fishstatus import fish_dict, fish_0


#跳脫不進入olami (template's text save here)
skip_list = ['func1', 'func2', 'func3', '檢視魚塭狀態', '魚塭異常總覽' , '近期天氣查詢']

def btn_template(maintitle, subtitle, pic_url, label1, text1, pb1, label2, text2, pb2, label3, text3, pb3):

    msg = buttons_template_message = TemplateSendMessage(
    alt_text='請選擇',
    template=ButtonsTemplate(
        thumbnail_image_url= pic_url,
        title=maintitle,
        text=subtitle,
        actions=[
            PostbackAction(
                label=label1,
                text=text1,
                data=pb1
            ),
            PostbackAction(
                label=label2,
                text=text2,
                data=pb2
            ),
            PostbackAction(
                label=label3,
                text=text3,
                data=pb3
            ),
        ]
        )
    )
    return msg

def carousel_template():
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item1.jpg',
                    title='this is menu1',
                    text='description1',
                    actions=[
                        PostbackAction(
                            label='postback1',
                            text='postback text1',
                            data='action=buy&itemid=1'
                        ),
                        MessageAction(
                            label='message1',
                            text='message text1'
                        ),
                        URIAction(
                            label='uri1',
                            uri='http://example.com/1'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://example.com/item2.jpg',
                    title='this is menu2',
                    text='description2',
                    actions=[
                        PostbackAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        ),
                        MessageAction(
                            label='message2',
                            text='message text2'
                        ),
                        URIAction(
                            label='uri2',
                            uri='http://example.com/2'
                        )
                    ]
                )
            ]
        )
    )
    return carousel_template_message


def main_carosel(name):
        carousel_template_message = TemplateSendMessage(
        alt_text='歡迎使用',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/1pXEHa7.jpg',
                    title=name+' 您好!',
                    text='歡迎使用Fish Farmer \n 請選擇以下的服務',
                    actions=[
                        MessageAction(
                            label='檢視魚塭狀態',
                            text='檢視魚塭狀態'
                        ),
                        MessageAction(
                            label='魚塭異常總覽',
                            text='魚塭異常總覽'
                        ),
                        MessageAction(
                            label='近期天氣查詢',
                            text='近期天氣查詢'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/Ro3oQBA.jpg',
                    title='設定',
                    text='請選擇以下的服務',
                    actions=[
                        URIAction(
                            label='魚種設定',
                            uri='http://example.com/2'
                        ),
                        MessageAction(
                            label='設定定時推播',
                            text='設定定時推播'
                        ),
                        MessageAction(
                            label='設定人生',
                            text='設定人生'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/44QGjEq.jpg',
                    title='關於我們',
                    text='一群為Hackthon而生的孩子們',
                    actions=[
                        URIAction(
                            label='Facebook',
                            uri='http://example.com/2'
                        ),
                        URIAction(
                            label='Instagram',
                            uri='http://example.com/2'
                        ),
                       URIAction(
                            label='作品集',
                            uri='http://example.com/2'
                        )
                    ]
                )
            ]
        )
        )
        return carousel_template_message


def get_totalFishStatus(count, list, ph, do, tmp):

    score_count = 0
    result = []
    result_url=""
    ok_url="https://i.imgur.com/6C044b5.png"
    warn_url="https://i.imgur.com/z4TThML.png"
    fatal_url="https://i.imgur.com/eVUPJvP.png"

    for i in range(0,len(list)):
        print(list[i])
        
        if float(tmp) >= float(fish_dict[i][0]) and float(tmp) <= float(fish_dict[i][1]):
            print('溫度正常')
        elif float(tmp) >= float(fish_dict[i][0]-5) and float(tmp) <= float(fish_dict[i][1]+5):
            print('溫度警告')
            score_count+=1
        else:
            print('溫度嚴重警告')
            score_count+=4
            
        if float(ph) >= float(fish_dict[i][2]) and float(ph) <= float(fish_dict[i][3]):
            print('ph正常')
        elif float(ph) >= float(fish_dict[i][2]-1) and float(ph) <= float(fish_dict[i][3]+1):
            print('ph警告')
            score_count+=1
        else:
            print('ph嚴重警告')
            score_count+=4

        if float(do) >= float(fish_dict[i][4]) and float(do) <= 12:
            print('do正常')
        elif float(do) >= float(fish_dict[i][4]-1) and float(do) <= 15:
            print('do警告')
            score_count+=1
        else:
            print('do嚴重警告')
            score_count+=4

        if score_count == 0:
            result_url = ok_url
        elif score_count >=1 and score_count <=4:
            result_url = warn_url
        else:
            result_url = fatal_url

    i = datetime.datetime.now()
    mdatetime = '%s-%s-%s' % (i.year, i.month, i.day) +'  '+ str(i.hour-4)+':'+str(i.minute)
    print(i.strftime('%H:%M'))
    print('%s-%s-%s' % (i.year, i.month, i.day))

    if count == 1:
        bubble = BubbleContainer(
            direction='ltr',
            body=BoxComponent(
            layout='vertical',
            contents=[                    
            # title
            BoxComponent(
            layout='vertical',
            contents=[
                TextComponent(text='魚塭狀態', weight='bold', size='sm', color='#1DB446'),
                TextComponent(text='魚塭資訊回傳', weight='bold', size='xxl', margin='md'),
                TextComponent(text='新北市板橋區', size='xs', color='#aaaaaa', margin='sm', wrap=True),
                SeparatorComponent(margin='xxl'),
                TextComponent(text='種類', size="md", weight="bold", wrap=True, spacing='sm', margin='md'),
                ]
            ),

            # fish 
            BoxComponent(
            layout='horizontal',
            margin='md',
            spacing='sm',
            contents=[             
            TextComponent(text=fish_dict[list[0]][5], size="xl", wrap=True, gravity="center"),
            SeparatorComponent(gravity="center"),
            ImageComponent(size= "xs", aspectRatio="20:13", aspectMode="fit", url=result_url, align="end", gravity="center") 
            ]
            ),
                            
            SeparatorComponent(margin='xxl'),
            TextComponent(text="水質資訊", size="md", weight="bold", wrap=True, spacing='sm', margin='md'),

            # water-ph
            BoxComponent(
                layout='horizontal',
                margin='md',
                spacing='sm',
                contents=[
                                    
                    TextComponent(text="ph值", size="sm", color="#555555", align="start"),
                    TextComponent(text=ph, siz="sm", color="#111111", align="end")
                ]
            ),
            # water-do
            BoxComponent(
            layout='horizontal',
            margin='md',
            spacing='sm',
            contents=[
                TextComponent(text="溶氧量(mg/L)", size="sm", color="#555555", flex=0),
                TextComponent(text=do, siz="sm", color="#111111", align="end")
                ]
            ),

            # water-tmp
            BoxComponent(
                layout='horizontal',
                margin='md',
                spacing='sm',
                contents=[
                    TextComponent(text="水溫(°C)", size="sm", color="#555555", flex=0),
                    TextComponent(text=tmp, siz="sm", color="#111111", align="end")
                ]
                )
            ]
            ),

            #
            footer=BoxComponent(
                layout='vertical',
                margin='md',
                spacing='md',
                contents=[
                    TextComponent(text="日期時間", size="xs", color="#aaaaaa", flex=0),
                    TextComponent(text=mdatetime, size="xs", color="#aaaaaa", align="end")
                ]
                )
        )
        message = FlexSendMessage(alt_text="魚塭狀態", contents=bubble)
        return message
        
'''    elif count == 2:
    elif count == 3:
    elif count == 4:
    elif count == 5:
    elif count == 6:
    elif count == 7:
    elif count == 8:
    elif count == 9:
    elif count == 10:'''