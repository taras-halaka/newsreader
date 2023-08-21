from datetime import datetime
from flet import *

class CheckListPage():
    def __init__(self,body):
        super().__init__()
        
#for DEBUG print to console
        self.debug=True
        if self.debug:         print(f" created = {datetime.now()} {type(self)}")
        
        self.body=body
        self.body=CheckListPageBody()
        


class CheckListPageBody(UserControl):
    def __init__(self):
        super().__init__()
  
    def build(self):
        return Container(content=Column([TextField(label="Your name"),
                        ElevatedButton("Login",on_click=lambda _: print(f" created = {type(self)}")),],
                        ),
                        margin=10,
                        padding=10,
                        alignment=alignment.top_left,
                        bgcolor=colors.RED_400,
                        border_radius=10,
                        expand=True,
                        height=200,
                        width=300,
                        tooltip="CheckList page tooltip"
                         )
 
 
        