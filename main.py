from flet import *
from src.ui2 import *

def main(page: Page):
    
    CustomApp(page)
    
    
app(main, view=AppView.FLET_APP)
