from rest_framework import serializers
from workout.models.workout_plan import WorkoutPlan

class WorkoutPlanSerializer(serializers.Serializer):
    class Meta:
        model = WorkoutPlan
        fields = '__all__'
