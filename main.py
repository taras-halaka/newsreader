from flet import *


def main(page: Page):
    page.title="some app"


    def hide_left_navigation(self):
        # body.controls.append(Text("menu item was hidden"))
        # body.update()
        # print("Left navigation collapsed")
        navRail.visible = not navRail.visible
        page.update()
        
        
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
                    body       
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
    
    body=Column([ Text("Empty")], alignment=MainAxisAlignment.START, expand=True)
        
    page.appbar=appbar1
    left_menu_selection(page)

    

app(main, view=AppView.WEB_BROWSER)
