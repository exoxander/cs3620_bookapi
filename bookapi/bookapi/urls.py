from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from books.views import BookViewSet, CategoryViewSet
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register("books",BookViewSet)
router.register("categories", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
