from flet import *
from src.ui3 import *

def main(page: Page):
    
    SimpleNewsReaderUI(page)
    
    
app(main, view=AppView.FLET_APP)
