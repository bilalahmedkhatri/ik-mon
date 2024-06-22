from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import MainUserView, get_data


urlpatterns = [
    path('user/', MainUserView.as_view()),
    path('usr-sys-det', get_data),
    # path('user/<int:pk>', MainUserView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
