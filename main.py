from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
import threading
import time
import os

class Timer(Screen):
    def start1(self, instance):
        def timer1():
            global a
            while int(self.a.text) > 0:
                self.a.text = str(int(self.a.text) - 1)
                time.sleep(1)
        
        threading.Thread(target=timer1, daemon=True).start()

    def start2(self, instance):
        def timer2():
            global a
            while int(self.a.text) > 0:
                self.a.text = str(int(self.a.text) + 1)
                time.sleep(1)
        self.a.text = str(int(self.a.text) + 1)
        threading.Thread(target=timer2, daemon=True).start()
        self.a.text = str(int(self.a.text) - 1)
    def plys10(self, instance):
        self.a.text = str(int(self.a.text) + 5)

    def plys1(self, instance):
        self.a.text = str(int(self.a.text) + 1)

    def plys30(self, instance):
        self.a.text = str(int(self.a.text) + 30)

    def minys30(self, instance):
        if int(self.a.text) > 29:
            self.a.text = str(int(self.a.text) - 30)

    def minys10(self, instance):
        if int(self.a.text) > 4:
            self.a.text = str(int(self.a.text) - 5)

    def minys1(self, instance):
        if int(self.a.text) > 0:
            self.a.text = str(int(self.a.text) - 1)

    def __init__(self, **kwargs):
        layout = FloatLayout()
        
        super().__init__(**kwargs)
    
        self.a = Label(
            text="0",
            pos_hint={'x': 0.375, 'y': 0.6},
            size_hint=(0.2, 0.1)
        )
        
        self.g = Label(
            text="0",
            pos_hint={'x': 0.375, 'y': 0.7},
            size_hint=(0.2, 0.1)
        )
    
        def update_clock():
            global g
            while True:
                current_time = time.strftime("%H:%M")
                self.g.text = current_time
            
                try:
                    with open('clock.txt', 'r') as clock:
                        for line in clock:
                            if current_time == line.strip():
                                self.g.text += " будильник сработал"
                except FileNotFoundError:
                    pass
                time.sleep(1)

        threading.Thread(target=update_clock, daemon=True).start()
    
        b = Button(
            text="+5",
            pos_hint={'x': 0.7, 'y': 0.4},
            size_hint=(0.2, 0.1)
        )
        
        c = Button(
            text="-5",
            pos_hint={'x': 0.1, 'y': 0.4},
            size_hint=(0.2, 0.1)
        )
        
        d = Button(
            text="таймер/старт",
            pos_hint={'x': 0.375, 'y': 0.5},
            size_hint=(0.25, 0.1)
        )
        
        e = Button(
            text="+1",
            pos_hint={'x': 0.7, 'y': 0.3},
            size_hint=(0.2, 0.1)
        )
        f=Button(
            text="-1",
            pos_hint=({'x':0.1,'y':0.3}),
            size_hint=(0.2,0.1)
        )
        g=Button(
            text="-30",
            pos_hint=({'x':0.1,'y':0.5}),
            size_hint=(0.2,0.1)
        )
        h=Button(
            text="+30",
            pos_hint=({'x':0.7,'y':0.5}),
            size_hint=(0.2,0.1)
        )
        i=Button(
            text="секундомер/старт",
            pos_hint=({'x':0.375,'y':0.4}),
            size_hint=(0.25,0.1)
        )
        j=Button(
            text="установить будилиник",
            pos_hint=({'x':0.375,'y':0.3}),
            size_hint=(0.25,0.1)
        )
        b.bind(on_press=self.plys10)
        c.bind(on_press=self.minys10)
        d.bind(on_press=self.start1)
        e.bind(on_press=self.plys1)
        f.bind(on_press=self.minys1)
        h.bind(on_press=self.plys30)
        g.bind(on_press=self.minys30)
        i.bind(on_press=self.start2)
        j.bind(on_press=self.alarm)
        layout.add_widget(self.a)
        layout.add_widget(b)
        layout.add_widget(c)
        layout.add_widget(d)
        layout.add_widget(e)
        layout.add_widget(f)
        layout.add_widget(g)
        layout.add_widget(h)
        layout.add_widget(i)
        layout.add_widget(self.g)
        layout.add_widget(j)
        self.add_widget(layout)
    def alarm(self, *args):
        self.manager.current = 'alarm'

class AlarmLayout(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        title = Label(
            text="Установщик будильников",
            pos_hint={'x': 0.1, 'y': 0.8},
            size_hint=(0.9, 0.1)
        )
        layout.add_widget(title)
        self.cloks_label = Label(
            text="Часы:",
            pos_hint={'x': 0.2, 'y': 0.7},
            size_hint=(0.2, 0.1)
        )
        layout.add_widget(self.cloks_label)
        self.alarm_cloks = TextInput(
            text="",
            pos_hint={'x': 0.4, 'y': 0.7},
            size_hint=(0.3, 0.1)
        )
        layout.add_widget(self.alarm_cloks)
        self.min_label = Label(
            text="Минуты:",
            pos_hint={'x': 0.2, 'y': 0.6},
            size_hint=(0.2, 0.1)
        )
        layout.add_widget(self.min_label)
        self.alarm_min = TextInput(
            text="",
            pos_hint={'x': 0.4, 'y': 0.6},
            size_hint=(0.3, 0.1)
        )
        layout.add_widget(self.alarm_min)
        self.set_button = Button(
            text="Установить будильник",
            pos_hint={'x': 0.4, 'y': 0.5},
            size_hint=(0.3, 0.1)
        )
        self.set_button.bind(on_press=self.save_alarm)
        layout.add_widget(self.set_button)

        self.add_widget(layout)

    def save_alarm(self, instance):
        hours = self.alarm_cloks.text.strip()
        minutes = self.alarm_min.text.strip()
        if not (hours.isdigit() and minutes.isdigit()):
            pass
        else:
            h = int(hours)
            m = int(minutes)
            if not (0 <= h <= 23 and 0 <= m <= 59):
                pass
            else:
                try:
                    with open("clock.txt", "a") as file:
                        time_str = f"{str(h).zfill(2)}:{str(m).zfill(2)}"
                        file.write(time_str + "\n")
                except Exception as e:
                    pass
        self.timer()

    def timer(self, *args):
        self.manager.current = 'home'
class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        alarm = AlarmLayout(name='alarm')
        timer = Timer(name='home')
        screen_manager.add_widget(timer)
        screen_manager.add_widget(alarm)
        return screen_manager
if __name__=="__main__":
	MyApp().run()