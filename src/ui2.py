from flet import *

class CustomApp():
    def __init__(self, page):
        super().__init__()
        self.page=page
        self.page.title="some sort of App"

        self.page.appbar=mAppBar().appBar
        mNavRail(self.page)
        # self.page.add(Row(mNavRail(self.page)))        
        self.page.update()

class mAppBar():
    def __init__(self):
        super().__init__()
        self.appBar=AppBar(
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



class mNavRail():
    def __init__(self,source_page):
        super().__init__()
        self.page=source_page
        self.navRail=NavigationRail(
                                selected_index=0,
                                label_type=NavigationRailLabelType.ALL,
                                height=1024,
                                extended=False,

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
                                #on_change=customApp.left_menu_selection
                                on_change=self.left_menu_selection
                            )
        self.page.add(Row(controls=[self.navRail,
                            VerticalDivider(width=1),
                            Column([
                                    TextField(label="Your name"),
                                    ElevatedButton("Login"),
                                        ],
                                   )
                            ]
                          ))
    
    def left_menu_selection(self):
        print("left_menu_selection  - is called ")
        selected=self.navRail.selected_index
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
        self.update()
