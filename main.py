from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
import random

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 400)


class CalculatorApp(App):
    def update_label(self):
        self.lbl.text = self.formula
    def add_number(self, instance):
        if self.formula == '0':
            self.formula = ''
        self.formula += str(instance.text)
        self.update_label()

    def calc_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = self.lbl.text

    def add_operation(self, instance):
        self.formula += str(instance.text)
        self.update_label()
    def build(self):
        self.formula = '0'
        b1 = BoxLayout(orientation='vertical', padding=5)
        layout = GridLayout(cols=4, spacing=3, size_hint=(1, .6))

        self.lbl = Label(text='0', text_size=(350, 400 * .4 - 50),
                            font_size=40, halign='right', valign='center',
                            size_hint=(1, .4))

        b1.add_widget(self.lbl)

        layout.add_widget(Button(text='7', on_press=self.add_number))
        layout.add_widget(Button(text='8', on_press=self.add_number))
        layout.add_widget(Button(text='9', on_press=self.add_number))
        layout.add_widget(Button(text='*', on_press=self.add_operation))

        layout.add_widget(Button(text='4', on_press=self.add_number))
        layout.add_widget(Button(text='5', on_press=self.add_number))
        layout.add_widget(Button(text='6', on_press=self.add_number))
        layout.add_widget(Button(text='-', on_press=self.add_operation))

        layout.add_widget(Button(text='1', on_press=self.add_number))
        layout.add_widget(Button(text='2', on_press=self.add_number))
        layout.add_widget(Button(text='3', on_press=self.add_number))
        layout.add_widget(Button(text='+', on_press=self.add_operation))

        layout.add_widget(Widget())
        layout.add_widget(Button(text='0', on_press=self.add_number))
        layout.add_widget(Button(text='.', on_press=self.add_operation))
        layout.add_widget(Button(text='=', on_press=self.calc_result))

        b1.add_widget(layout)

        return b1

if __name__ == '__main__':
    CalculatorApp().run()
