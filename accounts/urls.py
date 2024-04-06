from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import MainUserView


urlpatterns = [
    path('m_user/', MainUserView.as_view()),
    # path('m_user/<int:pk>', MainUserView.as_view()),
    # path('', )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
