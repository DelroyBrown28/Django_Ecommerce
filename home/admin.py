from django.contrib import admin
from .models import HomePageCustomisation


class HomePageCustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'home_page_title',
        'image',
    )


admin.site.register(HomePageCustomisation)
