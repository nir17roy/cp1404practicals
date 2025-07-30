# box_layout_demo.py
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class BoxLayoutDemo(App):
    message = StringProperty()

    def build(self):
        self.title = "BoxLayout Demo"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def handle_greet(self):
        name = self.root.ids.input_name.text
        self.message = f"Hello {name}"

    def handle_clear(self):
        self.root.ids.input_name.text = ""
        self.message = ""


if __name__ == '__main__':
    BoxLayoutDemo().run()
