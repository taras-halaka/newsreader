from flet import *

class CustomApp():
    def __init__(self, page):
        super().__init__()
        self.page=page
        self.page.title="some sort of App"

        self.appbar=mAppBar().appBar
        self.page.appbar=self.appbar
        
        self.navRail=mNavRail()
        self.mBody=mBody()
        
        self.page.add(Row(controls=[self.navRail,
                            VerticalDivider(width=1),
                            self.mBody
                            ],
                          alignment=MainAxisAlignment.START,   
                          ))
        self.page.snack_bar=SnackBar(
                        content=Text("Hello, world!"),
                        action="Alright!",
                    )
        # self.page.add(Row(mNavRail(self.page)))        
        self.page.update()

    def simpleAlert(self, text=None):
        if text:
            print(f"got message = {text}")
            self.page.snack_bar.conent(Text(text))
        else:
            print(f" no text was defined")
        self.page.snack_bar.open = True
        self.page.update()
    
    def defineActions(self):
        self.appBar.leading.on_click=self.simpleAlert



#
# Top Navigation Bar definition
#
class mAppBar():
    def __init__(self):
        super().__init__()
        self.appBar=AppBar(
                    leading=FloatingActionButton(icon=icons.MENU_SHARP, on_click=CustomApp.simpleAlert),
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
                            PopupMenuItem(text="Hide NavBar",on_click=CustomApp.simpleAlert)
                        ]
                    ),
                ]
)
        
        
#
#  content of app frame body definition
#        
class mBody(UserControl):
    def __init__(self):
        super().__init__()
    
    def build(self):
        return Container(content=Column([ TextField(label="Your name"),
                        ElevatedButton("Login",on_click=CustomApp.simpleAlert),],
                        ),
                        margin=10,
                        padding=10,
                        alignment=alignment.top_left,
                        bgcolor=colors.AMBER,
                        width=150,
                        height=250,
                        border_radius=10,
                         )

#
#  Left Navigation Menu Definition
#
class mNavRail(UserControl):
    def __init__(self):
        super().__init__()
    
    def build(self):
        return NavigationRail(
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

    
    def left_menu_selection(self):
        CustomApp.simpleAlert
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
