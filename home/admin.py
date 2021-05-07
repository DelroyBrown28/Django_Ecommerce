from django.contrib import admin
from .models import HomePageCustomisation, NavbarCustomisation


class HomePageCustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'home_page_title',
        'image',
    )


class NavbarCustimisationAdmin(admin.ModelAdmin):
    list_display = (
        'link_1',
        'link_2',
        'link_3',
        'link_4',
    )


admin.site.register(HomePageCustomisation)
admin.site.register(NavbarCustomisation)
