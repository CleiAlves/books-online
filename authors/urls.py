from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.author_register, name='authors'),
    path('edit/<int:author_id>/', views.edit_author, name='edit_author'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)