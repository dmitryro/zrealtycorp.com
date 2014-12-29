from django.contrib import admin
from dashboard.models import Property

class PropertyAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['title','type','image','description']}),)

    list_display = ('title','category','location','price','image','description')

    list_editable = ('title','category','location','price','image','description')

admin.site.register(Property, PropertyAdmin)

