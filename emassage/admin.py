from django.contrib import admin
from .models import Course, Category, Lesson, Question, Choice

# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Choice)
