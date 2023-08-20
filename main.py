from flet import *
from src.ui import *

def main(page: Page):
    page.title="some app"
    CustomApp(page)
    page.update()
    
app(main, view=AppView.FLET_APP)
