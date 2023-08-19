from flet import *

class UI(UserControl):
    def __init__(self):
        super().__init__()


    def build(self):
        return Column(
             [ElevatedButton("Add1", on_click=lambda e : print(e.control.text,"some")),
              ElevatedButton("Add2", on_click=Counter.add_click),
              ElevatedButton("Add3", on_click=Counter.add_click)]
        )


class Counter(UserControl):
    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        self.counter = 0
        self.text = Text(str(self.counter))
        return Row([self.text, ElevatedButton("Add", on_click=self.add_click)])
