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

def carousel_template(maintitle1, subtitle1, pic_url1, label11, text11, pb11, label12, text12, pb12, label13, text13, pb13,\
 maintitle2, subtitle2, pic_url2, label21, text21, pb21, label22, text22, pb22, label23, text23, pb23):
    msg = carousel_template_message = TemplateSendMessage(
    alt_text='請選擇',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url=pic_url1,
                title=maintitle1,
                text=subtitle1,
                actions=[
                    PostbackAction(
                        label=label11,
                        text=text11,
                        data=pb11
                    ),
                    PostbackAction(
                        label=label12,
                        text=text12,
                        data=pb12
                    ),
                    PostbackAction(
                        label=label13,
                        text=text13,
                        data=pb13
                    ),
                ]
            ),
            CarouselColumn(
                thumbnail_image_url=pic_url2,
                title=maintitle2,
                text=subtitle2,
                actions=[
                    PostbackAction(
                        label=label21,
                        text=text21,
                        data=pb21
                    ),
                    PostbackAction(
                        label=label22,
                        text=text22,
                        data=pb22
                    ),
                    PostbackAction(
                        label=label23,
                        text=text23,
                        data=pb23
                    ),
                ]
            )
        ]
    )
    )

    return carousel_template_message