# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Course, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ['name', 'short_description']
    # prepopulated_fields = {'slug': ['name']}
    ordering = ['id']
    search_fields = ['name']

