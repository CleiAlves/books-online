from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)