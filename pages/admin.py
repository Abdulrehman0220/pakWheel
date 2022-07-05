from django.contrib import admin

# Register your models here.
from pages.models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'First_Name', 'Last_Name', 'Designations', 'Date', 'image')
    list_display_links = ('id', 'First_Name',)
    search_fields = ('First_Name', 'Designations')
    list_filter = ('Designations',)


admin.site.register(Team, TeamAdmin)