from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from ui_handle.views import home_page

from django.conf.urls.static import static

# for static file on server
# from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    # Admin Page
    path('', home_page, name="home-page"),
    path('admin/', admin.site.urls),

    # Main User customize
    path('', include("accounts.urls")),

    # DJ_AUTH_JWT DEFAULT
    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    # USER APIs
    path('user_api/', include('user_api.urls')),

    # path('handle/', handle, name='handle'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # remove debug error
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve,
                {'document_root': settings.MEDIA_ROOT})]
    # re(r'^static/(?P<path>.*)$', serve,
    #     {'document_root': settings.STATIC_ROOT}),
