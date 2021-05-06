from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register 

from .models import HomePageCustomisation


class HomePageCustomisationAdmin(ModelAdmin):
    model = HomePageCustomisation 
    menu_label = "Home Page Customisation"  
    menu_icon = "fa-exchange" 
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    list_display = ("home_page_title", "image")


modeladmin_register(HomePageCustomisationAdmin)