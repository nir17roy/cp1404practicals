# squaring.py
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class SquaringApp(App):
    result = StringProperty()

    def build(self):
        self.title = "Squaring Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_square(self):
        try:
            value = float(self.root.ids.input_number.text)
            self.result = str(value ** 2)
        except ValueError:
            self.result = "Invalid input"


if __name__ == '__main__':
    SquaringApp().run()
