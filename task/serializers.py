from .models import Tasks
from rest_framework import serializers
class TasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Tasks
        fields=('id', 'title', 'details', 'dueDateTime', 'completed')