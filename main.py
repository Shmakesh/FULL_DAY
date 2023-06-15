import kivymd.icon_definitions
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem, TwoLineIconListItem
from kivymd.uix.label import MDLabel
from kivy.factory import Factory
from kivy.uix.image import Image
from kivymd.uix.list import IRightBodyTouch, ILeftBody
from kivymd.uix.list import OneLineListItem, MDList
from kivymd.uix.list import ThreeLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.card import MDCardSwipe
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
from kivymd import images_path
from kivymd.uix.list import ImageRightWidget
from kivymd.uix.pickers import MDDatePicker
import datetime


KV = '''
#https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
#this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts
# <DrawerClickableItem@MDNavigationDrawerItem>
#     focus_color: "#e7e4c0"
#     text_color: "#4a4939"
#     icon_color: "#FFC4BA"
#     ripple_color: "#c5bdd2"
#     selected_color: "#0c6c4d"
# 
# 
# <DrawerLabelItem@MDNavigationDrawerItem>
#     text_color: "#4a4939"
#     icon_color: "#4a4939"
#     focus_behavior: False
#     selected_color: "#FFC4BA"
#     _no_ripple_effect: True

MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:
   
                MDBottomNavigation:
                    panel_color: "#FFC4BA"
                    selected_color_background: "#FFF6EE"
                    text_color_active: "#756A6E"
        
                    MDBottomNavigationItem:
                        name: 'screen 1'
                        text: 'ПЛАНЕР'
                        icon: 'text-box-edit'
                                
                        MDBoxLayout:
                            orientation: 'vertical'
                            md_bg_color: '#C8C9DC'
                            MDTopAppBar:
                                title: "FULL DAY"
                                elevation: 2
                                pos_hint: {"top": 1}
                                md_bg_color: "#FFC4BA"
                                specific_text_color: "#4a4939"
                                # left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                                # image = ImageRightWidget(source='fullday.PNG')
                                
                            ScrollView:
                            
                                MDList:
                                    padding: '10dp'
                                    
                                    MDTextField:
                                        id: date
                                        hint_text: 'Дата'
                                        # on_focus: if self.focus: app.date_dialog.open()  
                                        icon_left: 'calendar'
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        icon_left_color_focus: "#756A6E"  
                                    
                                    MDTextField:
                                        hint_text: "06:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
            
                                    MDTextField:
                                        hint_text: "07:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "08:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True    
                                    MDTextField:
                                        hint_text: "09:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "10:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "11:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "12:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "13:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "14:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "15:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "16:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "17:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "18:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "19:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "20:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "21:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "22:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "23:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                    MDTextField:
                                        hint_text: "00:00"
                                        mode: "rectangle"
                                        line_color_focus: "#756A6E"
                                        hint_text_color_focus: "#756A6E"
                                        text_color_focus: "#756A6E"
                                        multiline: True
                                                                                
                    MDBottomNavigationItem:
                        name: 'screen 2'
                        text: 'ЦЕЛИ'
                        icon: 'trophy-variant'
                    
                        MDScreen:
                            md_bg_color: '#DBB9C8'
                            MDTopAppBar:
                                title: "FULL DAY"
                                elevation: 2
                                pos_hint: {"top": 1}
                                md_bg_color: "#FFC4BA"
                                specific_text_color: "#4a4939"
                                # left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                            
                    
                    MDBottomNavigationItem:
                        name: 'screen 3'
                        text: 'ТРЕКЕР'
                        icon: 'file-table-box-outline'
                    
                        MDScreen:
                            md_bg_color: '#BBACC1'
                            MDTopAppBar:
                                title: "FULL DAY"
                                elevation: 2
                                pos_hint: {"top": 1}
                                md_bg_color: "#FFC4BA"
                                specific_text_color: "#4a4939"
                                # left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                           
                    MDBottomNavigationItem:
                        name: 'screen 4'
                        text: 'ИДЕИ'
                        icon: 'plus-thick'
                    
                        MDScreen:
                            md_bg_color: '#FFC4BA'
                            
                            MDTabs:
                                id: tabs
                                text_color_normal: "#756A6E"
                                text_color_active: "#756A6E"
                                background_color: '#BBACC1'
                                on_tab_switch: app.on_tab_switch(*args)
                                Tab:
                                    id: tab1
                                    name: 'weekend'
                                    icon: 'lightbulb-on'
                                    title: "Идеи для выходных"
                                    MDScrollView:
                                        MDList:
                                            OneLineIconListItem:
                                                text: "Сходить в театр"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Устроить фотосессию"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Приготовить нечто особенное/новое"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить в парк развлечений"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Отправиться на велопрогулку"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Устроить киномарафон"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить на мастер-класс в гончарную мастерскую"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить на концерт"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить на мастер-класс в кулинарную студию"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Посетить галерею/выставку"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить на мастер-класс по рисованию"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить в SPA"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить на шоппинг"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить на пробное занятие по танцам"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Посетить планетарий"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить на мастер-класс по созданию парфюма/помады"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить на мастер-класс по кастому"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить на мастер-класс по созданию украшений"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Отправиться в мини-путешествие за город"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить в ресторан с подружками"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Устроить ночную прогулку по городу"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Устроить пикник в парке"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Прогулка на воздушном шаре"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Конная прогулка"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Прогулка на катамаране"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Побыть наедине с собой"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить с друзьями на квест"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Посетить комнату разрушений"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "star-outline"
                                                    icon_color: "#756A6E"
                                                    
                                Tab:
                                    id: tab2
                                    name: 'look'
                                    icon: 'hanger'
                                    title: "Образ дня"
                                    MDScrollView:
                                        MDList:
                                            OneLineIconListItem:
                                                text: "Классический стиль"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Женственный стиль"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Анимализм"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Бельевой стиль"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Стиль Кантри"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Восточный стиль"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Винтажный стиль"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Стиль Гаучо"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Гранж"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Городской шик"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Стиль Преппи"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Авангардный стиль"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Минимализ"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Стиль Эко"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Стиль oversize"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "tshirt-crew-outline"
                                                    icon_color: "#756A6E"
                                                
                                Tab:
                                    id: tab3
                                    name: 'evening'
                                    title: "Вечер с собой"
                                    icon: 'face-woman-shimmer'
                                    MDScrollView:
                                        MDList:
                                            OneLineIconListItem:
                                                text: "Изолируйся от всего"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "human-female"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Устрой себе вечер красоты"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "human-female"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Прочитай книгу, которую давно откладывала"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "human-female"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Преобрази свою комнату"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "human-female"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Посмотри уютный фильм"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "human-female"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Приготовь себе вкусный ужин"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "human-female"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Разбери гардероб, придумай новые луки"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "human-female"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Научись новому"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "human-female"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Послушай музыку"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "human-female"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Пригласи себя на свидание"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "human-female"
                                                    icon_color: "#756A6E"
                                      
                                Tab
                                    id: tab4
                                    name: 'feeling'
                                    title: "Полезные привычки"
                                    icon: 'account-heart'
                                    MDScrollView:
                                        MDList:
                                            OneLineIconListItem:
                                                text: "Следить за осанкой"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Принимать витамин D"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Наносить санскрин"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Спорт"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Прогулки на природе"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Медитации"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "регулярное посещение врачей"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Очки с защитой от экранов"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Мягкое очищение кожи всего тела"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Массаж кожи головы"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Пилинг для кожи головы"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Детокс от экранов перед сном"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Режим сна"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сон на шелковой наволочке"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Пить воду"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "spa-outline"
                                                    icon_color: "#756A6E"
                                Tab
                                    id: tab6
                                    name: 'reed'
                                    title: "Чтобы почитать"
                                    icon: 'book-open-page-variant'
                                    MDScrollView:
                                        MDList:
                                            TwoLineIconListItem:
                                                text: "К себе нежно. Ольга Примаченко"
                                                secondary_text: "Книги про уверенность в себе"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Просто будь собой. Сара Найт"
                                                secondary_text: "Книги про уверенность в себе"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Код уверенности. Роберт Келси"
                                                secondary_text: "Книги про уверенность в себе"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Люби себя. Камал Равикант"
                                                secondary_text: "Книги про уверенность в себе"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "К себе нежно"
                                                secondary_text: "Книги про уверенность в себе"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Исцели свои травмы. Беверли Энгл"
                                                secondary_text: "Книги про уверенность в себе"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "1984. Дж. Оруэлл"
                                                secondary_text: "Книги, которые изменят взгляд на мир"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "О дивный новый мир. Олдос Хаксли"
                                                secondary_text: "Книги, которые изменят взгляд на мир"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "451 градус по Фаренгейту. Рэй Брэдбери"
                                                secondary_text: "Книги, которые изменят взгляд на мир"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Процесс. Франц Кафка"
                                                secondary_text: "Книги, которые изменят взгляд на мир"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Вещи, которые они несли с собой. Тим О'Брайен"
                                                secondary_text: "Книги, которые изменят взгляд на мир"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Убить пересмешника. Хапер Ли"
                                                secondary_text: "Книги, которые каждый должен прочитать"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Великий Гэтсби. Ф. Скотт Фицджеральд"
                                                secondary_text: "Книги, которые каждый должен прочитать"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Унесенные ветром. Маргарет Митчелл"
                                                secondary_text: "Книги, которые каждый должен прочитать"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Цвет пурпурный. Элис Уокер"
                                                secondary_text: "Книги, которые каждый должен прочитать"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Грозовой перевал. Эмили Бронте"
                                                secondary_text: "Книги, которые каждый должен прочитать"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Магия утра"
                                                secondary_text: "Книги по психологии и саморазвитию"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Сила воли. как развить и укрепить. Келли Макгонигал"
                                                secondary_text: "Книги по психологии и саморазвитию"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Почему никто не рассказал мне это в 20. Тина Силинг"
                                                secondary_text: "Книги по психологии и саморазвитию"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Никогда-нибудь. Как выйти из тупика и найти себя"
                                                secondary_text: "Книги по психологии и саморазвитию"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Потолок. Психология оптимального переживания"
                                                secondary_text: "Книги по психологии и саморазвитию"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Есть, молиться, любить. Элизабет Гилберт"
                                                secondary_text: "Романы"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Дневник памяти. Николас Спаркс"
                                                secondary_text: "Романы"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "До встречи с тобой. Джоджо Мойес"
                                                secondary_text: "Романы"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Один среди туманов. Карен Уайт"
                                                secondary_text: "Романы"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Мой лучший враг. Эли Фрей"
                                                secondary_text: "Романы"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "book-outline"
                                                    icon_color: "#756A6E"
                                
                                Tab
                                    id: tab8
                                    name: 'summer'
                                    title: "Дела на лето"
                                    icon: 'tsunami'
                                    MDScrollView:
                                        MDList:
                                            OneLineIconListItem:
                                                text: "Прочитать книгу в парке"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Медленно прогуляться по городу, радуясь солнцу"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            TwoLineIconListItem:
                                                text: "Провести генеральную уборку дома"
                                                secondary_text: "помыть окна, сменить шторы на легкие занавески"
                                                text_color: "#756A6E"
                                                secondary_text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сходить на летнюю фотосессию"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сменить прическу/покрасить волосы"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Нарисовать картину"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Съездить на прогулку в лес"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Послушать щебетание птиц"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Пообедать в кафе на открытой веранде"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Приобрести новый аромат духов"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Завести новый трекер привычек"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Открыть сезон катания на велосипеде/роликах"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Сделать яркий летний маникюр"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Поменять заставку на телефоне и компьютере"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Посетить ботанический сад/дендрарий"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Поставить дома букетик сирени"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Устроить летнюю вечеринку"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Приготовить мороженое или фруктовый лед"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Перечитать любимую книгу детства"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Покататься на лошадях"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Научиться делать легкий мейк"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                            OneLineIconListItem:
                                                text: "Обновить гардероб"
                                                text_color: "#756A6E"
                                                IconLeftWidget:
                                                    icon: "bug-outline"
                                                    icon_color: "#756A6E"
                                Tab
                                    id: tab6
                                    name: 'food'
                                    title: "Рецепты"
                                    icon: 'baguette'
        # MDNavigationDrawer:
        #     id: nav_drawer
        #     md_bg_color: '#FFC4BA'
        #     radius: (0, 16, 16, 0)

            # MDNavigationDrawerMenu:
            # 
            #     MDNavigationDrawerHeader:
            #         title: "FULL DAY"
            #         title_color: "#756A6E"
            #         spacing: "4dp"
            #         padding: "12dp", 0, 0, "56dp"

                # DrawerClickableItem:
                #     icon: "face-woman-shimmer"
                #     text: "Аккаунт"
                # 
                # DrawerClickableItem:
                #     icon: "cog"
                #     text: "Настройки"
                # 
                # MDNavigationDrawerDivider:
                # 
                # MDNavigationDrawerLabel:
                #     text: "О нас"
                # 
                # DrawerClickableItem:
                #     icon: "account-multiple"
                #     text: "Об авторах"
                # 
                # DrawerClickableItem:
                #     icon: "wrench"
                #     text: "Исходный код"
                         
        
'''
class Tab(MDFloatLayout, MDTabsBase):
    pass
class Demo(MDFloatLayout):
    pass
# class Content(MDBoxLayout):
#     '''Custom content'''
class FULLDAY(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)
    def on_tab_switch(
        self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        print("Tab clicked!")


FULLDAY().run()