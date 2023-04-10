from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Products,Categories,Comment,LabelTag

class ProductsAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'status','labeltag','created_on','updated_on')
    list_filter = ("status","labeltag",'created_on','updated_on')
    readonly_fields = ['thumbnail_preview','thumbnail_preview2','thumbnail_preview3'] 
    search_fields = ['name', 'content']
    summernote_fields = ('content','precontent' )
    prepopulated_fields = {'slug': ('name',)}
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview
    def thumbnail_preview_2(self, obj):
        return obj.thumbnail_preview2
    def thumbnail_preview_3(self, obj):
        return obj.thumbnail_preview3
    
    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview_2.short_description = 'Thumbnail Preview 2'
    thumbnail_preview_3.short_description = 'Thumbnail Preview 3'
    thumbnail_preview.allow_tags = True
    thumbnail_preview_2.allow_tags = True
    thumbnail_preview_3.allow_tags = True

    

class CategoryAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'parent','created_on','updated_on')
    list_filter = ("status",'created_on','updated_on')
    readonly_fields = ('thumbnail_preview',) 
    search_fields = ['name', 'slug','parent']
    prepopulated_fields = {'slug': ('name',)}
    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True



class CommentAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email','content', 'proname','status','created_on','updated_on')
    list_filter = ("status",'created_on','updated_on','proname')
    readonly_fields = ['proname'] 
    search_fields = ['name', 'content']
    summernote_fields = ('content',)

class LabelTagAdmin(SummernoteModelAdmin):
    list_display = ('name','status','created_on','updated_on')
    list_filter = ("status",'created_on','updated_on')
    search_fields = ['name', 'content']
    summernote_fields = ('content',)


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(LabelTag, LabelTagAdmin)
admin.site.register(Comment, CommentAdmin)