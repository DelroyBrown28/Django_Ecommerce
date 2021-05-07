from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register 

from .models import HomePageCustomisation, NavbarCustomisation


class HomePageCustomisationAdmin(ModelAdmin):
    model = HomePageCustomisation 
    menu_label = "Home Page Customisation"  
    menu_icon = "fa-exchange" 
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    list_display = ("home_page_title", "image")


class NavbarCustomisationAdmin(ModelAdmin):
    model = NavbarCustomisation 
    menu_label = "Navbar Customisation"  
    menu_icon = "fa-bars" 
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    list_display = ("link_1", "link_2", "link_3", "link_4")


modeladmin_register(HomePageCustomisationAdmin)
modeladmin_register(NavbarCustomisationAdmin)
