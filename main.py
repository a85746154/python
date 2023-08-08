from kivy.core.text import LabelBase
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

LabelBase.register(name='msjh', fn_regular='fonts/msjh.ttc')

class TextInputApp(App):
    def build(self):
        # 創建一個垂直方向的BoxLayout，並設定其屬性
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # 創建文本輸入框並設定其屬性
        self.text_input = TextInput(hint_text='enter text here中文', multiline=False)
        
        # 創建標籤並設定其屬性，用於顯示即時輸入的文字
        self.label = Label(text='')
        
        # 將文本輸入框和標籤添加到BoxLayout中
        layout.add_widget(self.text_input)
        layout.add_widget(self.label)
        
        # 監聽文本輸入框的內容變化，並更新標籤的內容
        self.text_input.bind(text=self.on_text_input_change)
        
        return layout

    def on_text_input_change(self, instance, value):
        # 當文本輸入框的內容變化時，更新標籤的文字
        self.label.text = f'The text you entered is:{value}'

if __name__ == '__main__':
    TextInputApp().run()
