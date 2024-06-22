from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from ui_handle.views import home_page

from django.conf.urls.static import static

from django.views.static import serve

urlpatterns = [
    # Admin Page
    path('', home_page, name="home-page"),
    path('admin/', admin.site.urls),

    # Main customize User Model
    path('accounts/', include("accounts.urls")),
    path('api-auth/', include('rest_framework.urls')),  # DRF

    # USER APIs
    path('user_api/', include('user_api.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # remove debug error
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve,
                {'document_root': settings.MEDIA_ROOT})]
