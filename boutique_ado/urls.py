from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('page-editor/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('checkout_success/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
