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


def btn_template(maintitle, subtitle, pic_url, label1, text1, label2, text2, label3, text3):

    msg = buttons_template_message = TemplateSendMessage(
    alt_text='請選擇',
    template=ButtonsTemplate(
        thumbnail_image_url= pic_url,
        title=maintitle,
        text=subtitle,
        actions=[
            MessageAction(
                label=label1,
                text=text1
            ),
            MessageAction(
                label=label2,
                text=text2
            ),
            MessageAction(
                label=label3,
                text=text3
            ),
        ]
        )
    )
    return msg
