from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health

from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from emassage import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^emassage/api/', include(router.urls))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
