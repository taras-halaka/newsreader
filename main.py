from flet import *


def main(page: Page):
    page.title="some app"


    def hide_left_navigation(self):
        # body.controls.append(Text("menu item was hidden"))
        # body.update()
        # print("Left navigation collapsed")
        navRail.visible = not navRail.visible
        navRail.update()
    
    
    navRail=NavigationRail(
        selected_index=0,
        label_type=NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, label="First"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.BOOKMARK_BORDER),
                selected_icon_content=Icon(icons.BOOKMARK),
                label="Second",
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon_content=Icon(icons.SETTINGS),
                label_content=Text("Settings"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )

        
        
    appbar1=AppBar(
        leading=FloatingActionButton(icon=icons.MENU_SHARP, on_click=hide_left_navigation),
        
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
                    PopupMenuItem(text="Hide NavBar", on_click=hide_left_navigation )
                ]
            ),
        ]
    )
    body=Column([ Text("Body as component!")], alignment=MainAxisAlignment.START, expand=True)
    
    page.appbar=appbar1
    page.add(
        Row(
            [
                navRail,
                VerticalDivider(width=3),
                body
                
            ],
            expand=True,
        )
    )
    

app(main, view=AppView.WEB_BROWSER)
