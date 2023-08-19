from flet import *
from src.ui import *

def main(page: Page):
    page.title="some app"
    customApp=CustomApp()
    page.appbar=customApp.appBar
    page.add(
        Row(
            [
                customApp.navRail,
                VerticalDivider(width=1),
                UI()       
            ],
            expand=True,
        )
    )             
    page.update()
    
app(main, view=AppView.FLET_APP)
