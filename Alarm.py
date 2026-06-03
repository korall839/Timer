from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os

class AlarmLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(AlarmLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text="Установщик будильников", size_hint=(1, 0.2)))
        self.cloks_label = Label(text="Часы:")
        self.add_widget(self.cloks_label)
        self.alarm_cloks = TextInput(multiline=False, size_hint=(1, 0.1))
        self.add_widget(self.alarm_cloks)
        self.min_label = Label(text="Минуты:")
        self.add_widget(self.min_label)
        self.alarm_min = TextInput(multiline=False, size_hint=(1, 0.1))
        self.add_widget(self.alarm_min)
        self.set_button = Button(text="Установить будильник")
        self.set_button.bind(on_press=self.save_alarm)
        self.add_widget(self.set_button)
    def save_alarm(self, instance):
        try:
            hours = self.alarm_cloks.text
            minutes = self.alarm_min.text
            if int(hours)//25==0 and int(hours)>0 and int(minutes)//61==0 and int(minutes)>0:
                if not hours.isdigit() or not minutes.isdigit():
                    pass
                with open("clock.txt", "w") as file:
                    if len(hours)<2 and len(hours)>0 and len(minutes)<2 and len(minutes)>0:
                        file.write(f"{'0'+hours}:{'0'+minutes}")
                    elif len(minutes)<2 and len(minutes)>0:
                        file.write(f"{hours}:{'0'+minutes}")
                    elif len(hours)<2 and len(hours)>0:
                        file.write(f"{'0'+hours}:{minutes}")
                    else:
                        file.write(f"{hours}:{minutes}")
        except Exception as e:
            pass
class AlarmApp(App):
    def build(self):
        return AlarmLayout()
if __name__ == "__main__":
    AlarmApp().run()
