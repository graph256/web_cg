from django.contrib import admin
from django.contrib.auth.models import Group
from slugify import slugify
from .models import Program, Course, CourseAllocation, Upload, CoursePost

admin.site.register(Program)
admin.site.register(CourseAllocation)
admin.site.register(Upload)
admin.site.register(CoursePost)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': (slugify('title'),)}

