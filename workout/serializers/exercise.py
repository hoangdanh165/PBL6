from rest_framework import serializers
from workout.models.exercise import Exercise

class ExerciseSerializer(serializers.Serializer):
    class Meta:
        model = Exercise
        fields = '__all__'
