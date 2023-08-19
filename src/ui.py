from flet import *

class UI(UserControl):
    def __init__(self):
        super().__init__()


    def build(self):
        return Column(
             [ElevatedButton("Add1", on_click=lambda e : print(e.control.text,"some")),
              ElevatedButton("Add2", on_click=Counter.add_click),
              ElevatedButton("Add3", on_click=Counter.add_click)]
        )


class Counter(UserControl):
    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        self.counter = 0
        self.text = Text(str(self.counter))
        return Row([self.text, ElevatedButton("Add", on_click=self.add_click)])

appBar2=AppBar(
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

def hide_left_navigation(page:Page):
    # body.controls.append(Text("menu item was hidden"))
    # body.update()
    # print("Left navigation collapsed")
    page.navRail.visible = not page.navRail.visible
    page.update()


class AppBarMain(AppBar):
    def __init_(self):
        super().__init__()
        self.leading=FloatingActionButton(icon=icons.MENU_SHARP, on_click=self.hide_left_navigation),
        self.leading_width=40,
        self.title=Text("Some app bar"),
        self.toolbar_height=40,
        self.center_title=False,
        self.bgcolor=colors.BLUE_300,
        self.actions=[
                    PopupMenuButton(
                        icon=icons.SETTINGS,
                        items=[
                            PopupMenuItem(text="Help"),
                            PopupMenuItem(),  # divider
                            PopupMenuItem(text="Settings"),
                            PopupMenuItem(text="About"),
                            PopupMenuItem(text="Hide NavBar", on_click=self.hide_left_navigation )
                        ]
                    ),
                ]
        return self
                    
        
    def hide_left_navigation(self):
        # body.controls.append(Text("menu item was hidden"))
        # body.update()
        # print("Left navigation collapsed")
        self.page.navRail.visible = not self.page.navRail.visible
        self.page.update()
            
    # def build(self):
    #     return AppBar(leading=FloatingActionButton(icon=icons.MENU_SHARP, on_click=self.hide_left_navigation),
    #                     leading_width=40,
    #                     title=Text("Some app bar"),
    #                     toolbar_height=40,
    #                     center_title=False,
    #                     bgcolor=colors.BLUE_300,
    #                     actions=[
    #                         PopupMenuButton(
    #                             icon=icons.SETTINGS,
    #                             items=[
    #                                 PopupMenuItem(text="Help"),
    #                                 PopupMenuItem(),  # divider
    #                                 PopupMenuItem(text="Settings"),
    #                                 PopupMenuItem(text="About"),
    #                                 PopupMenuItem(text="Hide NavBar", on_click=self.hide_left_navigation )
    #                             ]
    #                         ),
    #                     ]
    #                 )