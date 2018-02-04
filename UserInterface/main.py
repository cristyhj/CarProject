#!/usr/bin/python

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button, ButtonBehavior
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.audio import SoundLoader, Sound
from kivy.uix.listview import ListView
from kivy.adapters.models import SelectableDataItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.selectableview import SelectableView
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.filechooser import FileChooserIconView

import os

from os import listdir
kv_path = '/home/sysop/CarProject/UserInterface/kvfiles/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)

fifo_file = '/tmp/fifofile'
sm = ScreenManager(transition=FadeTransition())


class VideoScreen(Screen):
    video_player = ObjectProperty()
    video_sm = ObjectProperty()
    media_chooser = ObjectProperty()

    def open_file(self):
        self.video_sm.current = 'files'
    
    def go_back(self):
        self.video_player.state = 'stop'
        sm.current = 'main'


class VideoFileChooser(FileChooserIconView):
    def on_submit(self, selection, touch):
        father = self.parent.parent.parent.parent
        father.video_sm.current = 'video'
        father.video_player.source = selection[0]
        father.video_player.state = 'play'


class MusicFileChooser(FileChooserIconView):
    def on_submit(self, selection, touch):
        father = self.parent
        if (father.sound.source != father.media_chooser.selection[0]):
            father.open_file()
        father.sound.play()
        father.playpause_sm.current = 'pause_button'

class MainScreen(Screen):
    pass


class MediaScreen(Screen):
    the_container = ObjectProperty()


class MyButton(ButtonBehavior, Image):
    def on_press(self):
        self.color = (.5, .5, .5, 1)

    def on_release(self):
        self.color = (1, 1, 1, 1)


class Container(GridLayout):
    def start_navit(self):
        fd = os.open(fifo_file, os.O_WRONLY)
        os.write(fd, b'start navi')
        os.close(fd)
        exit(0)

    def start_media(self):
        sm.current = 'media'

    def start_dashboard(self):
        fd = os.open(fifo_file, os.O_WRONLY)
        os.write(fd, b'start main')
        os.close(fd)
        exit(0)

    def start_video(self):
        sm.current = 'video'

    def settings(self):
        pass


class VideoContainer(VideoPlayer):
    pass

class MySound(Sound):
    def on_play(self):
        print 'da'
        print self.get_pos()

class MediaContainer(GridLayout):
    progress_slider = ObjectProperty()
    media_chooser = ObjectProperty()
    label_time = ObjectProperty()
    label_playing = ObjectProperty()
    playpause_sm = ObjectProperty()
    sound = MySound()

    from_touch = False

    def open_file(self):
        self.sound.stop()
        self.sound = SoundLoader.load(self.media_chooser.selection[0])
        self.progress_slider.min = 0
        self.progress_slider.max = self.sound.length
        self.label_playing.text = os.path.basename(self.media_chooser.selection[0])
    
    def update(self, dt):
        tm = self.sound.get_pos()
        self.progress_slider.value = tm
        seconds = int(tm % 60)
        minutes = int(tm / 60)
        if (seconds < 10):
            seconds = '0' + str(seconds)
        else:
            seconds = str(seconds)
        if (minutes < 10):
            minutes = '0' + str(minutes)
        else:
            minutes = str(minutes)
        self.label_time.text = minutes + ':' + seconds
    
    def play(self):
        if (self.sound.source != self.media_chooser.selection[0]):
            self.open_file()
        self.sound.play()
        self.playpause_sm.current = 'pause_button'
    
    def pause(self):
        self.sound.stop()
        self.playpause_sm.current = 'play_button'

    def next_song(self):
        files = self.media_chooser.files
        crr = files.index(self.sound.source)
	print len(files)
        path = files[(crr + 1) % len(files)]
        self.sound.stop()
        self.sound = SoundLoader.load(path)
        self.progress_slider.min = 0
        self.progress_slider.max = self.sound.length
        self.label_playing.text = os.path.basename(path)
        self.sound.play()
        self.playpause_sm.current = 'pause_button'

    def set_slider(self):
        if (self.from_touch):
            self.sound.seek(self.progress_slider.value)
        
    def go_back(self):
        sm.current = 'main'

    def on_touch_down(self, touch):
        self.from_touch = True
        return super(MediaContainer, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        self.from_touch = False
        return super(MediaContainer, self).on_touch_down(touch)


class MainApp(App):
    def build(self):
        sc1 = MainScreen(name="main")
        sc2 = MediaScreen(name="media")
        sc3 = VideoScreen(name="video")
        Clock.schedule_interval(sc2.the_container.update, 1)
        sm.add_widget(sc1)
        sm.add_widget(sc2)
        sm.add_widget(sc3)
        return sm


if __name__ == "__main__":
    app = MainApp()
    app.run()
