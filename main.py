from flet import *
from src.ui import *


def main(page: Page):
    page.title="some app"



        
        
    def left_menu_selection(self):
        page.controls.clear()
        print(f" navRail.selected_index = {navRail.selected_index}")
        if navRail.selected_index == 0:
            body=Column([ Text("Body as News!")], alignment=MainAxisAlignment.START, expand=True)
            print(f" News")
        elif navRail.selected_index == 1:
            body=Column([ Text("check lists!")], alignment=MainAxisAlignment.START, expand=True)
            print(f" CheckList")
        elif navRail.selected_index == 2:
            body=Column([ Text("settings!")], alignment=MainAxisAlignment.START, expand=True) 
            print(f"Settings")     
        
        page.add(
            Row(
                [
                    navRail,
                    VerticalDivider(width=1),
                    body,
                    UI()       
                ],
                expand=True,
            )
        )             
        page.update()
        print("menu item seelction updated")
    
    navRail=NavigationRail(
        selected_index=0,
        label_type=NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.NEWSPAPER, selected_icon=icons.NEWSPAPER, label="News"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.FACT_CHECK_OUTLINED),
                selected_icon_content=Icon(icons.FACT_CHECK),
                label="CheckLists",
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon_content=Icon(icons.SETTINGS),
                label_content=Text("Settings"),
            ),
        ],
        #on_change=lambda e: print("Selected destination:", e.control.selected_index),
        on_change=left_menu_selection
    )

        
    
    body=Column([ Text("Empty")], alignment=MainAxisAlignment.START, expand=True)
        
    #page.appbar=AppBarMain(page)
    # appBarMain=AppBarMain()
    # print("\n \n",appBarMain,"\n")
    #page.appbar=AppBar3()
    page.appbar=appBar2
    page.update()
    left_menu_selection(page)
    

    

#app(main, view=AppView.WEB_BROWSER)
app(main, view=AppView.FLET_APP)
