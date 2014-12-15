from rest_framework import serializers
from agent.models import Agent

class AgentSerializer():
    class Meta:
        model = Agent
        fields = ('title', 'first_name', 'last_name', 'role','phone','email','bio','avatar')

