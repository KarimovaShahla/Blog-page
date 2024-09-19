from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']

class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'title', 'category', 'created_at', 'updated_at', 'edit_link', 'delete_link']

    def thumbnail(self, obj):
        # Birinci tapılan şəkli göstərir
        if obj.image_1:
            return format_html('<img src="{}" style="width: 50px; height:auto;">', obj.image_1.url)
        elif obj.image_2:
            return format_html('<img src="{}" style="width: 50px; height:auto;">', obj.image_2.url)
        elif obj.image_3:
            return format_html('<img src="{}" style="width: 50px; height:auto;">', obj.image_3.url)
        return "No Image"
    thumbnail.short_description = 'Photo'

    def edit_link(self, obj):
        url = reverse('admin:my_app_advertisements_change', args=[obj.pk])
        return format_html('<a href="{}" class="button edit-button">Edit</a>', url)
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        url = reverse('admin:my_app_advertisements_delete', args=[obj.pk])
        return format_html('<a href="{}" class="button delete-button">Delete</a>', url)
    delete_link.short_description = 'Delete'

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['platform', 'likes', 'white_photo', 'black_photo', 'link', 'edit_link', 'delete_link']

    def white_photo(self, obj):
        if obj.image1 and hasattr(obj.image1, 'url'):
            return format_html('<img src="{}" style="width: 50px; height:auto;" />', obj.image1.url)
        return "No Image"
    white_photo.short_description = 'White Photo'

    def black_photo(self, obj):
        if obj.image2 and hasattr(obj.image2, 'url'):
            return format_html('<img src="{}" style="width: 50px; height:auto;" />', obj.image2.url)
        return "No Image"
    black_photo.short_description = 'Black Photo'

    def edit_link(self, obj):
        url = reverse('admin:my_app_socialmedia_change', args=[obj.pk])
        return format_html('<a href="{}" class="button edit-button">Edit</a>', url)
    edit_link.short_description = 'Edit'

    def delete_link(self, obj):
        url = reverse('admin:my_app_socialmedia_delete', args=[obj.pk])
        return format_html('<a href="{}" class="button delete-button">Delete</a>', url)
    delete_link.short_description = 'Delete'

    class Media:
        css = {
            'all': ('css/custom_admin.css',)  # Xüsusi stil əlavə edildi
        }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Advertisements, AdvertisementsAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
