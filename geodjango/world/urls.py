from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'worldborders', WorldBorderViewSet)
router.register(r'voivodships', VoivodshipsViewSet)
router.register(r'districts', DistrictsViewSet)
router.register(r'ariports', AriportsViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]