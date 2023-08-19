from flet import *


def main(page: Page):
    page.title="some app"


    def hide_left_navigation(self):
        # if navRail.visible:
        #     message='visible'
        # else:
        #     message='hidden'
        # print(f"hide naviation was changed from {message} to :")
        navRail.visible = not navRail.visible
        navRail.update()
    
    
    navRail=NavigationRail(
        selected_index=0,
        label_type=NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=FloatingActionButton(icon=icons.MENU, text="Navigation", on_click=hide_left_navigation),
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
        leading=Icon(icons.MENU_BOOK),
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
    
    
    page.appbar=appbar1
    page.add(
        Row(
            [
                navRail,
                VerticalDivider(width=3),
                Column([ Text("Body!")], alignment=MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )
    

app(main, view=AppView.WEB_BROWSER)
