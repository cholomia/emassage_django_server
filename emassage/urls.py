from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from emassage import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
