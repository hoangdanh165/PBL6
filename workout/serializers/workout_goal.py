from rest_framework import serializers
from workout.models.workout_goal import WorkoutGoal

class WorkoutGoalSerializer(serializers.Serializer):
    class Meta:
        model = WorkoutGoal
        fields = '__all__'
