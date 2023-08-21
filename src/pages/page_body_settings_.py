from datetime import datetime
from flet import *


class SettingsPage():
    def __init__(self,body):
        super().__init__()
        #link to source page obj
        self.body=body
        self.body=SettingsBody()
        
        

# Define custom component of page content
class SettingsBody(UserControl):
    def __init__(self):
        super().__init__()
        print(f" {type(self)}")
        
    def build(self):
        return Container(content=Column(
                        [TextField(label="Settings"),
                        ElevatedButton("Apply?",on_click=lambda _: print(f" created = {type(self)}")),],
                        ),
                        margin=10,
                        padding=10,
                        alignment=alignment.top_left,
                        bgcolor=colors.GREEN_200,
                        border_radius=10,
                        expand=True,
                        height=200,
                        width=300,
                        tooltip="News page tooltip"
                         )
 
 
        