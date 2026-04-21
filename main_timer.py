from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import time
import threading
class MyApp(App):
    def start(self,instance):
        def timer():
            global a
            while int(self.a.text)>0:
                self.a.text=str(int(self.a.text)+1)
                time.sleep(1)
        r=threading.Thread(target=timer)
        r.start()
    def build(self):
        layout=FloatLayout()
        self.a=Label(
            text="0",
            pos=(300,1500),
            size_hint=(0.2,0.1)
        )
        d=Button(
            text="старт",
            pos=(400,1250),
            size_hint=(0.3,0.1)
        )
        d.bind(on_press=self.start)
        layout.add_widget(self.a)
        layout.add_widget(b)
        layout.add_widget(c)
        layout.add_widget(d)
        layout.add_widget(e)
        layout.add_widget(f)
        layout.add_widget(g)
        layout.add_widget(h)
        return layout
MyApp().run()