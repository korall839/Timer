from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import time
import threading
class MyApp(App):
    def start1(self,instance):
        def timer1():
            global a
            self.a.text=str(int(self.a.text)+1)
            while int(self.a.text)>0:
                self.a.text=str(int(self.a.text)-1)
                time.sleep(1)
        r=threading.Thread(target=timer1)
        r.start()
    def start2(self,instance):
        def timer2():
            global a
            while int(self.a.text)>0:
                self.a.text=str(int(self.a.text)+1)
                time.sleep(1)
        r=threading.Thread(target=timer2)
        self.a.text=str(int(self.a.text)+1)
        r.start()
        self.a.text=str(int(self.a.text)-1)
    def plys10(self,instance):
        self.a.text=str(int(self.a.text)+5)
    def plys1(self,instance):
        self.a.text=str(int(self.a.text)+1)
    def plys30(self,instance):
        self.a.text=str(int(self.a.text)+30)
    def minys30(self,instance):
        if int(self.a.text)>29:
            self.a.text=str(int(self.a.text)-30)
    def minys10(self,instance):
        if int(self.a.text)>4:
            self.a.text=str(int(self.a.text)-5)
    def minys1(self,instance):
        if int(self.a.text)>0:
            self.a.text=str(int(self.a.text)-1)
    def build(self):
        layout=FloatLayout()
        self.a=Label(
            text="0",
            pos=(200,400),
            size_hint=(0.2,0.1)
        )
        b=Button(
            text="+5",
            pos=(400,200),
            size_hint=(0.2,0.1)
        )
        c=Button(
            text="-5",
            pos=(100,200),
            size_hint=(0.2,0.1)
        )
        d=Button(
            text="таймер/старт",
            pos=(200,300),
            size_hint=(0.3,0.1)
        )
        e=Button(
            text="+1",
            pos=(400,100),
            size_hint=(0.2,0.1))
        f=Button(
            text="-1",
            pos=(100,100),
            size_hint=(0.2,0.1)
        )
        g=Button(
            text="-30",
            pos=(100,300),
            size_hint=(0.2,0.1)
        )
        h=Button(
            text="+30",
            pos=(400,300),
            size_hint=(0.2,0.1)
        )
        i=Button(
            text="секундомер/старт",
            pos=(200,200),
            size_hint=(0.3,0.1)
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
        return layout
MyApp().run()
