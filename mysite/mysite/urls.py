from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views  # Assuming your views are in the 'main' app

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),  # Fixed the view reference
    path('', include("main.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

