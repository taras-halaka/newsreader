from flet import *
from datetime import datetime
#custom content
from src.menuItems import MenuItems
from src.news_body import NewsPage
from src.checklist_body import CheckListPage
from src.settings_body import SettingsPage



class SimpleNewsReaderUI():
    def __init__(self,mainpage:Page):
        super().__init__()
#for DEBUG print to console
        self.debug=True
        if self.debug:         print(f" created = {datetime.now()} {type(self)}")
        #define properites 
        self.page=mainpage
        self.body=Container(content=Column([TextField(label="...Empty space...")]))
        self.state_changed=False


#define TOP navigation menu content
        self.page.appbar=AppBar(
                    leading=FloatingActionButton(
                        icon=icons.MENU_SHARP,
                        on_click=self.togle_navbar
                        ),
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
                            PopupMenuItem(text="Hide NavBar",on_click=self.togle_navbar)
                        ]),])
        
        
#define LEFT navigation menu content
        # self.navRail=NavigationRail(
        #                         selected_index=0,
        #                         label_type=NavigationRailLabelType.ALL,
        #                         #height=1024,
        #                         #extended=False,

        #                         min_width=100,
        #                         min_extended_width=400,
        #                         group_alignment=-0.9,
        #                         destinations=[
        #                             NavigationRailDestination(
        #                                 icon=icons.NEWSPAPER, 
        #                                 selected_icon=icons.NEWSPAPER_ROUNDED, 
        #                                 label="News"
        #                             ),
        #                             NavigationRailDestination(
        #                                 icon_content=Icon(icons.FACT_CHECK_OUTLINED),
        #                                 selected_icon_content=Icon(icons.FACT_CHECK),
        #                                 label="CheckLists",
        #                             ),
        #                             NavigationRailDestination(
        #                                 icon=icons.SETTINGS_OUTLINED,
        #                                 selected_icon_content=Icon(icons.SETTINGS),
        #                                 label="Settings",
        #                             ),
        #                         ],
        #                         #on_change=lambda e: print("Selected destination:", e.control.selected_index),
        #                         #on_change=customApp.left_menu_selection
        #                         #on_change=lambda _:print(f" left menu selected {self.navRail.selected_index}")
        #                         on_change=self.change_body_content
        #                     )
        
        #get menu content from extra module
        self.menuItems=MenuItems(self.body)
        self.navRail=self.menuItems.navigationRail
        self.navRail.on_change=self.change_body_content
#define page content
        # self.body=Container(content=Column([TextField(label="Your name"),
        #                 ElevatedButton("Login",on_click=lambda _: print(f" created = {type(self)}")),],
        #                 ),
        #                 margin=10,
        #                 padding=10,
        #                 alignment=alignment.top_left,
        #                 bgcolor=colors.AMBER,
        #                 border_radius=10,
        #                 expand=True,
        #                 height=200,
        #                 width=300,
        #                 tooltip="some tooltip"
        #                  )
    
 
 
#add conetnet to page

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
        



#function definitions:


# navigation bar toggle

    def togle_navbar(self,_args):
            self.navRail.visible = not self.navRail.visible
            if self.navRail.visible:
                 self.show_snack_bar("INFO: Left Menu Opened ","ok!")
            else:
                 self.show_snack_bar("INFO: Left Menu Closed ","ok!")
            self.navRail.update() 
            
            
# show notification in snackbar
            
    def show_snack_bar(self,msg=None,action=None):
        if msg:
            self.page.snack_bar.content= Text(f"{msg}")
        if action:
            self.page.snack_bar.action= action
        self.page.snack_bar.open = True
        self.page.snack_bar.update()
             
        
        
# change body content
    def change_body_content(self, _args ):
        selected_menu_item=self.navRail.destinations[self.navRail.selected_index].label
        if self.debug: print(f"  >>{selected_menu_item} >>called change_body_content:")
        #news_page_content=NewsPage(self.body)
        #CheckListPage(self.body)
        if selected_menu_item == self.menuItems.items[0]["label"]:
            news_page_content= self.menuItems.items[0]["content"] #SettingsPage(self.body) 
        if selected_menu_item == self.menuItems.items[1]["label"]:
            news_page_content= self.menuItems.items[1]["content"] #SettingsPage(self.body) 
        if selected_menu_item == self.menuItems.items[2]["label"]:
            news_page_content= self.menuItems.items[2]["content"] #SettingsPage(self.body) 
        if selected_menu_item == self.menuItems.items[3]["label"]:
            news_page_content= self.menuItems.items[3]["content"] #SettingsPage(self.body) 

        self.body=news_page_content.body
        #application UI was changed
        self.state_changed=True
        self.updateUI()
        self.show_snack_bar(f"{self.navRail.destinations[self.navRail.selected_index].label}","ok!")
        


    def updateUI(self):
        if self.debug:
            print(f" -> updateUI()")
        if self.state_changed:
            self.page.clean()
            self.page.add(Row(controls=[
                                self.navRail,
                                VerticalDivider(width=1),
                                self.body
                                ],
                            alignment=MainAxisAlignment.START,
                            expand=True   
                            ))        
            self.page.update()
            self.state_changed=False
                    
