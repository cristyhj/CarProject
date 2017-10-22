from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior 
from kivy.uix.image import Image  
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import FadeTransition

#Builder.load_file('start.kv')

sm = ScreenManager()
screen_menu = Screen(name = "menu")
screen_player = Screen(name = "player")
sm = ScreenManager(transition=FadeTransition())
        

class BtnWidget(ButtonBehavior, Image):
    def on_press(self):
        self.color = (.5,.5,.5,1)

    def on_release(self):
        self.color = (1,1,1,1)

def foo(instance):
    sm.current = 'player'

class MyApp(App):
    def build(self):
        layout = GridLayout(cols = 3)
        
        btn1 = BtnWidget()
        btn1.source = 'images/play.png'
        btn1.bind(on_press=foo)
        btn2 = BtnWidget()
        btn2.source = 'images/pause.png'
        btn3 = BtnWidget()
        btn3.source = 'images/rec.png'
        btn4 = BtnWidget()
        btn4.source = 'images/settings.png'
        btn5 = BtnWidget()
        btn5.source = 'images/menu.png'
        btn6 = BtnWidget()
        btn6.source = 'images/next.png'
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        layout.add_widget(btn6)
        
        btnp = BtnWidget()
        btnp.source = 'images/fullscreen.png'
        screen_player.add_widget(btnp)
        
        screen_menu.add_widget(layout)
        sm.add_widget(screen_menu)
        sm.add_widget(screen_player)
        return sm

if __name__ == '__main__':
    MyApp().run()
    
    
    

