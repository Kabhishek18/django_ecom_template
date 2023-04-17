from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Products, Categories, Comment, LabelTag, Discount, Ratings


class ProductsAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'status', 'labeltag', 'created_on', 'updated_on')
    list_filter = ("status", "labeltag", 'created_on', 'updated_on')
    readonly_fields = ['thumbnail_preview', 'thumbnail_preview2', 'thumbnail_preview3']
    search_fields = ['name', 'content']
    summernote_fields = ('content', 'precontent')
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
    list_display = ('name', 'slug', 'parent', 'created_on', 'updated_on')
    list_filter = ("status", 'created_on', 'updated_on')
    readonly_fields = ('thumbnail_preview',)
    search_fields = ['name', 'slug', 'parent']
    prepopulated_fields = {'slug': ('name',)}

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


class CommentAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'content', 'product_name', 'status', 'created_on', 'updated_on')
    list_filter = ("status", 'created_on', 'updated_on', 'product_name')
    readonly_fields = ['product_name']
    search_fields = ['name', 'content']
    summernote_fields = ('content',)


class LabelTagAdmin(SummernoteModelAdmin):
    list_display = ('name', 'status', 'created_on', 'updated_on')
    list_filter = ("status", 'created_on', 'updated_on')
    search_fields = ['name', 'content']
    summernote_fields = ('content',)


class DiscountAdmin(SummernoteModelAdmin):
    list_display = ('code', 'percent_off', 'start_date', 'end_date', 'created_on', 'updated_on')
    list_filter = ("code", 'created_on', 'updated_on')
    search_fields = ['code', 'percent_off']
    summernote_fields = 'code'


class RatingsAdmin(SummernoteModelAdmin):
    list_display = ('product_name','username','rating_review', 'status', 'created_on', 'updated_on')
    list_filter = ("product_name",'username',"rating_review","status", 'created_on', 'updated_on')
    search_fields = ['product_name','rating_review','name', 'content']


admin.site.register(Categories, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(LabelTag, LabelTagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Ratings, RatingsAdmin)
