from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Rectangle(pos=(100, 100), size=(200, 40))

class MyApp(App):

    def build(self):
        return Game()
    

if __name__ == "__main__":
    app = MyApp()
    app.run()