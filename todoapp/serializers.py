from rest_framework import serializers
from todoapp.models import TodoModel

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ["id", "name", "description"]