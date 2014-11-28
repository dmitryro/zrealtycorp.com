from django.contrib import admin
from property.models import Property

class PropertyAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['property_id','title','fulltitle','type','category','status','price',
                         'borough','neighborhood','description', 'size','rooms','bathrooms',
                         'published','expires','picture1','picture2','picture3',
                         'picture4','pets_allowed','is_featured']}),)

    list_display = ('property_id','title','type', 'category','status','price','borough',
                    'neighborhood', 'size','rooms','bathrooms','published','expires','pets_allowed','is_featured')

    list_editable = ('type','rooms','category','status','borough','neighborhood')

admin.site.register(Property, PropertyAdmin)

