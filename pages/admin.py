from django.contrib import admin
from .models import DynamicPage

@admin.register(DynamicPage)
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}