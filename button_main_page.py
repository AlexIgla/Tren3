from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image


class MainApp(App):
    def build(self):
        # Добавляем виджет
        layout = FloatLayout()
        # Добавляем изображение
        image = Image(source='E:/Tren_Alex/shvarc_image.jpg',
                      allow_stretch=True,
                      keep_ratio=False)
        layout.add_widget(image)
        # Добавляем кнопки
        button1 = Button(text='Календарь',
                         size_hint=(.25, .1),
                         pos_hint={'center_x': .2, 'center_y': .3})
        layout.add_widget(button1)
        button2 = Button(text='Выбор тренировок',
                         size_hint=(.25, .1),
                         pos_hint={'center_x': .2, 'center_y': .2})
        layout.add_widget(button2)
        button3 = Button(text='Комплекс тренировок',
                         size_hint=(.25, .1),
                         pos_hint={'center_x': .2, 'center_y': .1})
        layout.add_widget(button3)

        return layout