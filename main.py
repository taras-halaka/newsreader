from flet import *
from src.simpleNewsReaderUI import SimpleNewsReaderUI

def main(page: Page):
    
    SimpleNewsReaderUI(page)
    
    
app(main, view=AppView.FLET_APP)
