from django.contrib import admin
from django.contrib.admin.decorators import register
from post.models import Category, Post, Tag
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields ={'slug': ('title', )}

# admin.site.register(Tag, TagAdmin)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'views', 'get_photo')
    prepopulated_fields= {'slug': ('title', )}
    fields = ('title', 'slug', 'author', 'category', 'content', 'tags', 'views', 'photo', 'get_photo')
    list_filter = ('author', 'category', 'created_at')
    readonly_fields = ('views', 'get_photo' )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Фото'