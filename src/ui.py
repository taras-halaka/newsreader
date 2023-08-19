from flet import *

class UI(UserControl):
    def __init__(self):
        super().__init__()
        self.counter=0
        
    def add_click(self, e):
        self.counter += 1
        self.update()


    def build(self):
        return Column(
             [
                ElevatedButton("Add1", on_click=self.add_click),
                Text(f" clicked {str(self.counter)}") 
             ]
        )

staticAppBar=AppBar(
    leading=FloatingActionButton(icon=icons.MENU_SHARP, on_click=lambda e: print("page.controls")),
    leading_width=40,
    title=Text("Some app bar"),
    toolbar_height=40,
    center_title=False,
    bgcolor=colors.BLUE_300,
    actions=[
                    PopupMenuButton(
                        icon=icons.SETTINGS,
                        items=[
                            PopupMenuItem(text="Help"),
                            PopupMenuItem(),  # divider
                            PopupMenuItem(text="Settings"),
                            PopupMenuItem(text="About"),
                            PopupMenuItem(text="Hide NavBar",on_click=lambda e: print("hide"))
                        ]
                    ),
                ]
)

def left_menu_selection():
    selected=staticNavRail.selected_index
    print(f" navRail.selected_index = {selected}")
    if selected == 0:
        body=Column([ Text("Body as News!")], alignment=MainAxisAlignment.START, expand=True)
        print(f" News")
    elif selected == 1:
        body=Column([ Text("check lists!")], alignment=MainAxisAlignment.START, expand=True)
        print(f" CheckList")
    elif selected == 2:
        body=Column([ Text("settings!")], alignment=MainAxisAlignment.START, expand=True) 
        print(f"Settings")     
    

staticNavRail=NavigationRail(
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