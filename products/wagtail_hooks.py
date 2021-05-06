from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register 

from .models import Product


class ProductAdmin(ModelAdmin):
    model = Product 
    menu_label = "Products"  
    menu_icon = "pick" 
    menu_order = 200 
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    list_display = ("name",)
    list_filter = ("category",)
    search_fields = ("name",)


modeladmin_register(ProductAdmin)