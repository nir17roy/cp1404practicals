# dynamic_labels.py
from kivy.app import App
from kivy.lang import Builder


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_labels(self):
        names = ["Alice", "Bob", "Charlie", "Diana"]
        self.root.ids.labels_box.clear_widgets()
        for name in names:
            self.root.ids.labels_box.add_widget(
                Label(text=name, font_size=18)
            )


from kivy.uix.label import Label

if __name__ == '__main__':
    DynamicLabelsApp().run()
