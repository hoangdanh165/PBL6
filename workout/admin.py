from django.contrib import admin
from .models.exercise import Exercise
from .models.workout_goal import WorkoutGoal
from .models.workout_plan import WorkoutPlan
from .models.workout_schedule import WorkoutSchedule


admin.register(Exercise)
admin.register(WorkoutGoal)
admin.register(WorkoutPlan)
admin.register(WorkoutSchedule)

