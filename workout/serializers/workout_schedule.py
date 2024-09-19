from rest_framework import serializers
from workout.models.workout_schedule import WorkoutSchedule

class WorkoutScheduleSerializer(serializers.Serializer):
    class Meta:
        model = WorkoutSchedule
        fields = '__all__'
