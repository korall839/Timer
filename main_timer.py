from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import time
import threading
import Alarm

class MyApp(App):
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

    def build(self):
        layout = FloatLayout()
    
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
        b.bind(on_press=self.plys10)
        c.bind(on_press=self.minys10)
        d.bind(on_press=self.start1)
        e.bind(on_press=self.plys1)
        f.bind(on_press=self.minys1)
        h.bind(on_press=self.plys30)
        g.bind(on_press=self.minys30)
        i.bind(on_press=self.start2)
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
        return layout

if __name__=="__main__":
	MyApp().run()