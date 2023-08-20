from flet import *

class CustomApp():
    def __init__(self, page):
        super().__init__()
        self.page=page
        self.page.title="some sort of App"

        self.page.appbar=mAppBar().appBar
        self.page.add(
                        Column([
                            TextField(label="Your name"),
                            ElevatedButton("Login")
                        ])
                    )        
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
