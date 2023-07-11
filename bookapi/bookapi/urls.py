from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from books.views import *
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register("books",BookViewSet)
router.register("categories", CategoryViewSet)
router.register("space", SpaceViewSet)
router.register("science", ScienceViewSet)
router.register("medieval", MedievalViewSet)
router.register("engineering", EngineeringViewSet)
router.register("medicine", MedicineViewSet)
router.register("programming", ProgrammingViewSet)
router.register("technology", TechnologyViewSet)
router.register("biology", BiologyViewSet)
router.register("art", ArtViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
