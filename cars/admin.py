from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    def pic(self, object):
        return format_html('<img src ="{}" width = "40px" style="border-radius:50px"/>'.format(object.car_photo.url))

    pic.short_description = 'Car pic'
    list_display = ('id', 'pic', 'car_title', 'year', 'city', 'is_featured',)
    list_display_links = ('id', 'pic', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'year', 'city')
    list_filter = ('city','model','car_title')

admin.site.register(Car, CarAdmin)
