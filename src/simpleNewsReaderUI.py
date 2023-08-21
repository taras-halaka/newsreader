from flet import *
from datetime import datetime
#custom content
from src.menu.menu_Left_navigation_Items import MenuItems
from src.pages.page_body_news_ import NewsPage
from src.pages.page_body_checklist_ import CheckListPage
from src.pages.page_body_settings_ import SettingsPage



class SimpleNewsReaderUI():
    def __init__(self,mainpage:Page):
        super().__init__()
#for DEBUG print to console
        self.debug=True
        if self.debug:         print(f" created = {datetime.now()} {type(self)}")
        #define properites 
        self.page=mainpage
        self.body=Container(
                content=Column(
                    [  
                        Text("..Тут могла бути ваша реклама...\n Оберіть пункт з меню навігації")],
                        
                    ))
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
                            PopupMenuItem(text="Help"),# on_click=self.show_snack_bar(f" Help Selected","ok!")),
                            PopupMenuItem(),  # divider
                            PopupMenuItem(text="Settings"),# on_click=self.show_snack_bar(f" Settings Selected","ok!")),
                            PopupMenuItem(text="About"),# on_click=self.show_snack_bar(f" About Selected","ok!")),
                            PopupMenuItem(text="Hide NavBar",on_click=self.togle_navbar)
                        ]),])
        
        
        #get menu content from extra module
        self.menuItems=MenuItems(self.body)
        self.navRail=self.menuItems.navigationRail
        self.navRail.on_change=self.change_body_content
#define page content
 
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

        for item in self.menuItems.items:
            if selected_menu_item == item["label"]:
                self.body=item["content"].body
            else:
                if self.debug: print(f" ---- {item['label']} not matched with menu list item {selected_menu_item}")
                
        #application UI was changed
        self.state_changed=True
        self.updateUI()
        self.show_snack_bar(f"{self.navRail.destinations[self.navRail.selected_index].label}","ok!")
        


    def updateUI(self):
        if self.debug: print(f" -> updateUI()")
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
                    
