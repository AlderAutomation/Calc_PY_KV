from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

kv = """
BoxLayout:
    orientation: "vertical"
    padding: "20dp"
    spacing: "20dp"

    Label: 
        text: "This app is made by Matthew at AlderAutomation using Python and Kivy. Please feel free to visit us at alderautomation.ca and most major socials"
        text_size: self.width, None
        size_hint: 1, None 
        height: self.texture_size[1]
        pos_hint: {"center_x":0.5}
        halign: "center"

    Button: 
        text: "Back"
        size_hint: None, None
        height: "50dp"
        width: "150dp"
        pos_hint: {"center_x":0.5}
        on_press: quit()
"""

class about_window(BoxLayout):
    pass


class AboutApp(App): 
    def build(self):
        return Builder.load_string(kv)


if __name__=="__main__":
    AboutApp().run()