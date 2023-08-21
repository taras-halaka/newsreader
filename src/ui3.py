from flet import *


class SimpleNewsReaderUI():
    def __init__(self,mainpage:Page):
        super().__init__()
        print(f" created = {type(self)}")
        #define properites 
        self.page=mainpage
        self.state_changed=False

        #define navigation menu content
        self.page.appbar=AppBar(
                    leading=FloatingActionButton(
                        icon=icons.MENU_SHARP,
                        on_click=lambda _: print(f"leading icon clicked")),
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
                            PopupMenuItem(text="Hide NavBar")
                        ]),])
         #define left navigation menu content
        self.navRail=NavigationRail(
                                selected_index=0,
                                label_type=NavigationRailLabelType.ALL,
                                #height=1024,
                                #extended=False,

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
                                #on_change=self.left_menu_selection
                            )
        #define page content
        self.body=Container(content=Column([TextField(label="Your name"),
                        ElevatedButton("Login",on_click=lambda _: print(f" created = {type(self)}")),],
                        ),
                        margin=10,
                        padding=10,
                        alignment=alignment.top_left,
                        bgcolor=colors.AMBER,
                        border_radius=10,
                        expand=True,
                        height=200,
                        width=300,
                        tooltip=Text("some tooltip")
                         )
 
 
 
        #conetnet to page
        self.page.add(Row(controls=[
                            self.navRail,
                            VerticalDivider(width=1),
                            self.body
                            ],
                          alignment=MainAxisAlignment.START,
                          expand=True   
                          ))
        self.page.snack_bar=SnackBar(
                        content=Text("Hello, world!"),
                        action="Alright!",
                    )        
        self.page.update()

        
        
        



