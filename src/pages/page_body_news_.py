from datetime import datetime
from flet import *

class NewsPage():
    def __init__(self,body):
        super().__init__()
        #link to source obj
        self.body=body
        self.body=NewsPageBody()
        
        

# Define custom component of page content
class NewsPageBody(UserControl):
    def __init__(self):
        super().__init__()
        print(f" {type(self)}")
        
    def build(self):
        return Container(content=Column(
                        [TextField(label="News"),
                        ElevatedButton("Update?",on_click=lambda _: print(f" created = {type(self)}")),],
                        ),
                        margin=10,
                        padding=10,
                        alignment=alignment.top_left,
                        bgcolor=colors.BLUE_100,
                        border_radius=10,
                        expand=True,
                        height=200,
                        width=300,
                        tooltip="News page tooltip"
                         )
 
 
        