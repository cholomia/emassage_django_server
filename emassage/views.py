from django.shortcuts import render
from rest_framework import renderers, viewsets
from .serializers import CourseSerializer
from .models import Course


# Create your views here.

class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
