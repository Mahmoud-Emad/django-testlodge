from rest_framework.serializers import ModelSerializer
from server.test_tracker.models.dashboard import Project


class ProjectsSerializer(ModelSerializer):
    """class ProjectsSerializer to serialize the project obj"""
    class Meta:
        model = Project
        exclude = ('user',)
