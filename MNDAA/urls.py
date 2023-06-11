
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('default-admin/', admin.site.urls),
    path('',include('Base.urls')),
    path('',include('Myanmar.urls')),
    path('',include('Dashboard.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

