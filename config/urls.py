from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # 추가 필요

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Team_3E_apart.urls')),  # Team_3E_apart의 URL을 포함
]

# 미디어 파일 서빙
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
