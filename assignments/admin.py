from django.contrib import admin
from .models import Course, Professor, Assignment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'full_name', 'format', 'professor')
    list_filter = ('format', 'professor')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'due_date', 'is_complete')
    list_filter = ('course', 'is_complete')