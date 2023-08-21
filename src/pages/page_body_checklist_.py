from datetime import datetime
from flet import *

class CheckListPage():
    def __init__(self,body):
        super().__init__()
        #link to source obj
        self.body=body
        self.body=CheckListPageBody()
        

# Define custom component of page content
class CheckListPageBody(UserControl):
    def __init__(self):
        super().__init__()
  
    def build(self):
        return Container(content=Column(
                        [TextField(label="CheckList"),
                        ElevatedButton("Check?",on_click=lambda _: print(f" created = {type(self)}")),],
                        ),
                        margin=10,
                        padding=10,
                        alignment=alignment.top_left,
                        bgcolor=colors.AMBER_200,
                        border_radius=10,
                        expand=True,
                        height=200,
                        width=300,
                        tooltip="CheckList page tooltip"
                         )
 
 
        