from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register 

from .models import HomePageCustomisation, NavbarCustomisation
from products.models import Product
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)



class HomePageCustomisationAdmin(ModelAdmin):
    model = HomePageCustomisation 
    menu_label = "Home Page"  
    menu_icon = "fa-exchange" 
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    list_display = ("home_page_title", "image")


class NavbarCustomisationAdmin(ModelAdmin):
    model = NavbarCustomisation 
    menu_label = "Navbar"  
    menu_icon = "fa-bars" 
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    list_display = ("link_1", "link_2", "link_3", "link_4")
    
    
class ProductAdmin(ModelAdmin):
    model = Product 
    menu_label = "Products"  
    menu_icon = "fa-product-hunt"
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    list_display = ("name", "price")
    

    
    
class CustomisationGroup(ModelAdminGroup):
    menu_label = 'Custom Pages'
    menu_icon = 'fa-paint-brush'
    menu_order = 200
    items = (NavbarCustomisationAdmin, HomePageCustomisationAdmin, ProductAdmin)


# modeladmin_register(HomePageCustomisationAdmin)
# modeladmin_register(NavbarCustomisationAdmin)
modeladmin_register(CustomisationGroup)

