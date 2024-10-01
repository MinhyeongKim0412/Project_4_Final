from django.contrib import admin
from django.urls import path, include
from Team_3E_apart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('apart/', include('Team_3E_apart.urls')),
]

# 미디어 파일 서빙
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)