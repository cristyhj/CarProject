from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior 
from kivy.uix.image import Image  
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import FadeTransition
import subprocess
import os
from transdata import *

#Builder.load_file('start.kv')

sm = ScreenManager()
screen_menu = Screen(name = "menu")
screen_player = Screen(name = "music_player")
sm = ScreenManager(transition=FadeTransition())
persistent_data = TransData()


class BtnWidget(ButtonBehavior, Image):
    def on_press(self):
        self.color = (.5, .5, .5, 1)

    def on_release(self):
        self.color = (1, 1, 1, 1)
        
    def cb_music_player(instance):
        sm.current = 'music_player'

    def cb_back(instance):
        sm.current = 'menu'
        
    def cb_obd(instance):
        subprocess.Popen('../DashBoard/main.py', shell=True)
        #os.system('cd ..')
        #os.system('cd .. && python main.py')
        
    def cb_power_off(instance):
        exit()


class MyApp(App):
    def build(self):
        layout = GridLayout(cols = 3)
        
        btn_music_player = BtnWidget()
        btn_music_player.source = 'images/music.png'
        btn_music_player.bind(on_press=BtnWidget.cb_music_player)
        
        btn_navit = BtnWidget()
        btn_navit.source = 'images/open.png'
        
        btn_obd = BtnWidget()
        btn_obd.source = 'images/egalizator.png'
        btn_obd.bind(on_press=BtnWidget.cb_obd)
        
        btn4 = BtnWidget()
        btn4.source = 'images/settings.png'
        
        btn5 = BtnWidget()
        btn5.source = 'images/menu.png'
        
        btn_power_off = BtnWidget()
        btn_power_off.source = 'images/poweroff.png'
        btn_power_off.bind(on_press=BtnWidget.cb_power_off)
        
        layout.add_widget(btn_music_player)
        layout.add_widget(btn_navit)
        layout.add_widget(btn_obd)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        layout.add_widget(btn_power_off)
        
        btnp = BtnWidget()
        btnp.source = 'images/reload.png'
        btnp.bind(on_press=BtnWidget.cb_back)
        screen_player.add_widget(btnp)
        
        screen_menu.add_widget(layout)
        sm.add_widget(screen_menu)
        sm.add_widget(screen_player)
        return sm


if __name__ == '__main__':
    MyApp().run()
    
    
    

