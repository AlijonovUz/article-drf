from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from api.handlers import handler404 as json_404
from api.handlers import handler500 as json_500

handler404 = json_404
handler500 = json_500

urlpatterns = [
    path("api/v1/", include("api.urls")),
    path('auth/', include("accounts.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
