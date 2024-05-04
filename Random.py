import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__(orientation='vertical', spacing=20)

    def generate_number(self, instance):
        self.random_label.text = str(random.randint(0, 100))

class MyApp(App):
    def build(self):
        root = MyRoot()

        # Creating Kivy widgets
        random_label = Label(text="-", font_size=64)
        generate_button = Button(text="Generate", font_size=32, size=(100, 50))
        generate_button.bind(on_press=root.generate_number)

        # Associating widgets with MyRoot
        root.random_label = random_label

        # Adding widgets to MyRoot
        root.add_widget(Label(text="Random Number", font_size=45, color=(0.92, 0.45, 0, 1)))
        root.add_widget(random_label)
        root.add_widget(generate_button)

        return root

    def on_start(self):
        self.title = 'RandomNum'

if __name__ == '__main__':
    app = MyApp()
    app.run()
