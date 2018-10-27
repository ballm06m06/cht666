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
                    thumbnail_image_url='https://example.com/item1.jpg',
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
                    thumbnail_image_url='https://example.com/item2.jpg',
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
                    thumbnail_image_url='https://example.com/item2.jpg',
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

#檢視魚塭狀態
def get_all_data():
     bubble = BubbleContainer(
            direction='ltr',
            
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='魚塭狀態', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://i.imgur.com/QiTvzLn.png'),
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
          
            return message