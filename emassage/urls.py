from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CourseViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
