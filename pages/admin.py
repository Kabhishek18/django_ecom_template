from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import DynamicPage


@admin.register(DynamicPage)
class PageAdmin(SummernoteModelAdmin):
    list_display = ('title','slug', 'status', 'created_on', 'updated_on')
    list_filter = ("status", 'created_on', 'updated_on')
    search_fields = ['title', 'content','meta_tag']
    summernote_fields = ('content',)