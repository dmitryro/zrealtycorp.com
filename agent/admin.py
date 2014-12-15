# Register your models here.
from django.contrib import admin
from agent.models import Agent

class AgentAdmin(admin.ModelAdmin):
    fieldsets = ((None, {'fields': ['title','first_name', 
                         'last_name','role','phone','email','bio',
                         'avatar']}),)

    list_display = ('title', 'first_name',
                    'last_name', 'role','phone','email','bio','avatar')

    list_editable = ('role',)

admin.site.register(Agent, AgentAdmin)

