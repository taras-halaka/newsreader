from flet import icons,NavigationRail,NavigationRailDestination,NavigationRailLabelType
from src.news_body import NewsPage
from src.checklist_body import CheckListPage
from src.settings_body import SettingsPage

class MenuItems():
    def __init__(self,body):
        super().__init__()

        #import variable from callable source
        self.body=body
        #menu items
        self.news = {
            "label":"News1",
            "icon":icons.NEWSPAPER, 
            "selected_icon":icons.NEWSPAPER_ROUNDED, 
            "content":NewsPage(self.body),
        }
        self.checklist = {
            "label":"CheckList1",
            "icon":icons.FACT_CHECK_OUTLINED, 
            "selected_icon":icons.FACT_CHECK, 
            "content":CheckListPage(self.body)
        }
        self.setings = {
            "label":"Settings1",
            "icon":icons.SETTINGS_OUTLINED, 
            "selected_icon":icons.SETTINGS,
            "content":SettingsPage(self.body) 
        }
        #array of menu items in sequence
        self.items = [self.setings,self.checklist,self.news,self.news,]
        #define main props
        self.navigationRail=NavigationRail(
                                selected_index=0,
                                label_type=NavigationRailLabelType.ALL,
                                min_width=100,
                                min_extended_width=400,
                                group_alignment=-0.9,
                                destinations=[
                                ],
                            )
        # add menu items from array of dict
        for item in self.items:
            self.navigationRail.destinations.append(
                                    NavigationRailDestination(
                                        icon=item["icon"], 
                                        selected_icon=item["selected_icon"], 
                                        label=item["label"]
                                    )           
            )