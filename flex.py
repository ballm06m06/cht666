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
                                    TextComponent(text="吳郭魚", size="xl", wrap=True, gravity="center"),
                                    SeparatorComponent(gravity="center"),
                                    ImageComponent(size= "xs", aspectRatio="20:13", aspectMode="fit", url="https://i.imgur.com/6C044b5.png", align="end", gravity="center") 
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
                                    
                                    TextComponent(text="8.9", siz="sm", color="#111111", align="end")
                                ]
                            ),
                            # water-do
                            BoxComponent(
                                layout='horizontal',
                                margin='md',
                                spacing='sm',
                                contents=[
                                    
                                    TextComponent(text="溶氧量(mg/L)", size="sm", color="#555555", flex=0),
                                    
                                    TextComponent(text="3.5", siz="sm", color="#111111", align="end")
                                ]
                            ),
                            # water-tmp
                            BoxComponent(
                                layout='horizontal',
                                margin='md',
                                spacing='sm',
                                contents=[
                                    
                                    TextComponent(text="水溫(°C)", size="sm", color="#555555", flex=0),
                                    
                                    TextComponent(text="23", siz="sm", color="#111111", align="end")
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
                            TextComponent(text="2018-10-28 14:20", size="xs", color="#aaaaaa", align="end")
                        ]
                    )
                )

                message = FlexSendMessage(alt_text="魚塭狀態", contents=bubble)