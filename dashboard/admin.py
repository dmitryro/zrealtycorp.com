from django.contrib import admin
from dashboard.models import Property, Post, Comment


class PropertyAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['title','type','image','description']}),)

    list_display = ('title','category','location','price','image','description')

    list_editable = ('title','category','location','price','image','description')

class PostAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['title','author','link','published','post','count']}),)

    list_display = ('title','author','link','published','post','counter')

    list_editable = ('title','author','link','published','post','counter')
    


admin.site.register(Property, PropertyAdmin)
admin.site.register(Post, PostAdmin)



