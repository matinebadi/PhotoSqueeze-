import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from PIL import Image

class ImageCompressorApp(App):
    def build(self):
        Window.size = (400, 450)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="Hello! I can compress your image while keeping the same dimensions.\nPlease select the desired quality:",
                           size_hint_y=None, height=100, halign='center', valign='middle')
        self.label.bind(size=self.label.setter('text_size'))
        self.layout.add_widget(self.label)

        self.slider_label = Label(
            text="Selected Quality: 100%",
            size_hint_y=None, height=40, halign='center', valign='middle')
        self.slider_label.bind(size=self.slider_label.setter('text_size'))
        self.layout.add_widget(self.slider_label)

        self.slider = Slider(min=1, max=100, value=100)
        self.slider.bind(value=self.on_slider_value_change)
        self.layout.add_widget(self.slider)

        self.upload_button = Button(text="Upload Image", size_hint_y=None, height=50)
        self.upload_button.bind(on_release=self.show_filechooser)
        self.layout.add_widget(self.upload_button)

        self.footer = Label(
            text="© 2024 Image Compression by Matin Ebadi\nAll rights reserved.",
            size_hint_y=None, height=50, halign='center', valign='middle')
        self.footer.bind(size=self.footer.setter('text_size'))
        self.layout.add_widget(self.footer)

        return self.layout

    def on_slider_value_change(self, instance, value):
        self.slider_label.text = f"Selected Quality: {int(value)}%"

    def show_filechooser(self, instance):
        content = FileChooserIconView(path=os.path.expanduser("~"))
        content.bind(on_submit=self.compress_image)
        self.popup = Popup(title="Select an Image", content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    def compress_image(self, filechooser, selection, touch):
        if selection:
            file_path = selection[0]
            try:
                image = Image.open(file_path)
                quality = int(self.slider.value)
                self.open_save_popup(image, quality)
                self.popup.dismiss()
            except Exception as e:
                self.show_error("Error", str(e))

    def open_save_popup(self, image, quality):
        save_popup_content = BoxLayout(orientation='vertical')
        save_path_input = TextInput(hint_text="Enter save name", size_hint_y=None, height=30)
        save_popup_content.add_widget(save_path_input)
        directory_chooser = FileChooserIconView(path=os.path.expanduser("~"))
        save_popup_content.add_widget(directory_chooser)

        save_button = Button(text="Save Compressed Image", size_hint_y=None, height=50)
        save_button.bind(on_release=lambda x: self.save_image(image, save_path_input.text, directory_chooser.path, quality))
        save_popup_content.add_widget(save_button)

        save_popup = Popup(title="Save Compressed Image", content=save_popup_content, size_hint=(0.9, 0.6))
        save_popup.open()

    def save_image(self, image, filename, directory):
        if not filename.endswith(".jpg"):
            filename += ".jpg"
        if image.mode == 'RGBA':
            image = image.convert('RGB')
        save_path = os.path.join(directory, filename)
        try:
            image.save(save_path, 'JPEG')
            self.show_info("Success", f"Image saved successfully at {save_path}")
        except Exception as e:
            self.show_error("Error", str(e))


        def open_save_popup(self, image, quality):
            save_popup_content = BoxLayout(orientation='vertical')
            save_path_input = TextInput(hint_text="Enter save name", size_hint_y=None, height=30)
            save_popup_content.add_widget(save_path_input)
            directory_chooser = FileChooserIconView(path=os.path.expanduser("~"))
            save_popup_content.add_widget(directory_chooser)

            save_button = Button(text="Save Compressed Image", size_hint_y=None, height=50)
            save_button.bind(on_release=lambda x: self.save_image(image, save_path_input.text, directory_chooser.path, quality))
            save_popup_content.add_widget(save_button)

            save_popup = Popup(title="Save Compressed Image", content=save_popup_content, size_hint=(0.9, 0.6))
            save_popup.open()

    def save_image(self, image, filename, directory, quality):
        if not filename.endswith(".jpg"):
            filename += ".jpg"
        save_path = os.path.join(directory, filename)


        try:
            image.save(save_path, 'JPEG', quality=quality)
            self.show_success("Success", f"Image saved to {save_path}")
        except Exception as e:
            self.show_error("Error", str(e))

    def show_warning(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.5, 0.5))
        popup.open()

    def show_error(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.5, 0.5))
        popup.open()

    def show_success(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.5, 0.5))
        popup.open()

if __name__ == '__main__':
    ImageCompressorApp().run()