from django.contrib import admin
from .models import Project, Category

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'addr_donate')

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)

