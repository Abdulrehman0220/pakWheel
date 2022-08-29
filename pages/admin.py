import img as img
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from pages.models import Team


class TeamAdmin(admin.ModelAdmin):
    def pic(self,object):
        return format_html('<img src ="{}" width = "40px" style="border-radius:50px"/>'.format(object.image.url))
    list_display = ('id', 'First_Name', 'Last_Name', 'Designations', 'Date', 'pic')
    list_display_links = ('id', 'First_Name','Last_Name','pic')
    search_fields = ('First_Name', 'Designations')
    list_filter = ('Designations',)


admin.site.register(Team, TeamAdmin)
