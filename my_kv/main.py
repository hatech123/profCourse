import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.boxlayout import BoxLayout
class Filechooser(BoxLayout):
    def select(self,*args):
        try: self.label.text = args[1][0]
        except: pass
class FileApp(App):
    def build(self):
        return Filechooser()

if __name__ == "__main__":
    FileApp().run()