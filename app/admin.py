from django.contrib import admin
from .models import Item, Image

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'author', 'date', 'id')
    search_fields = ['name', 'price', 'author', 'date']


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'image')
    search_fields = ['item', ]


admin.site.register(Item, ItemAdmin)
admin.site.register(Image, ImageAdmin)
