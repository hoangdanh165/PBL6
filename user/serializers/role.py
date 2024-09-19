from rest_framework import serializers
from user.models.role import Role

class RoleSerializer(serializers.Serializer):
    class Meta:
        model = Role
        fields = '__all__'
