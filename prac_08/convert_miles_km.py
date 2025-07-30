# convert_miles_km.py
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class MilesConverterApp(App):
    result = StringProperty()

    def build(self):
        self.title = "Miles to Kilometers Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            kilometers = miles * 1.60934
            self.result = f"{kilometers:.2f} km"
        except ValueError:
            self.result = "Invalid input"


if __name__ == '__main__':
    MilesConverterApp().run()
