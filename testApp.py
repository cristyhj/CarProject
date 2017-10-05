from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty


from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '600')


class Ac(Widget):
    angle = NumericProperty()

    def on_touch_move(self, touch):
        self.parent.speed = touch.x
        if((150 - self.parent.speed / 240 * 360)<9) and ((150 - self.parent.speed / 240 * 360)>-255):
             self.angle = 150 - self.parent.speed / 240 * 360

class ceas1(Widget):
    pass


class MyWidget(Widget):
    alpha = NumericProperty()
    ac = ObjectProperty(None)
    ceas1 = ObjectProperty(None)



class testApp(App):
    def build(self):
        cs1 = ceas1()
        return cs1


if __name__ == '__main__':
    testApp().run()
