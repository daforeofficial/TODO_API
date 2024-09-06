from rest_framework import serializers
from .models import *

# Serializers API ki representation k leay.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'deadline', 'priority', 'is_completed']
