from flet import *
from src.ui import *

def main(page: Page):
    page.title="some app"
    page.appbar=staticAppBar
    page.add(
        Row(
            [
                staticNavRail,
                VerticalDivider(width=1),
                UI()       
            ],
            expand=True,
        )
    )             
    page.update()
    left_menu_selection()
app(main, view=AppView.FLET_APP)
