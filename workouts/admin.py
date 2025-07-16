from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.ExerciseCategory)
admin.site.register(models.Exercise)
admin.site.register(models.TrainingPlan)
admin.site.register(models.TrainingDay)
admin.site.register(models.DailyExercise)
