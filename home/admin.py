from django.contrib import admin
from django.contrib.sites.models import Site
from taggit.admin import Tag
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from wagtail.images.models import Image
from wagtail.documents.models import Document
from .models import HomePageCustomisation, NavbarCustomisation


class HomePageCustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'home_page_title',
        'image',
    )


class NavbarCustomisationAdmin(admin.ModelAdmin):
    list_display = (
        'link_1',
        'link_2',
        'link_3',
        'link_4',
    )

 


admin.site.register(HomePageCustomisation)
admin.site.register(NavbarCustomisation)
admin.site.unregister(Site)
admin.site.unregister(Tag)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(Document)
admin.site.unregister(Image)

