from django.db import models
from users.models import User


# Create your models here.

class ExercisesBank(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        to=User, related_name='exercises_banks', related_query_name='exercises_bank', on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, default='no description', max_length=500)

    class Meta:
        verbose_name = 'exercises bank'
        verbose_name_plural = 'exercises banks'
        ordering = '-id'
        constraints = models.UniqueConstraint(
            fields=('name', 'owner'), name='unique_for_owner'
        )

    def __str__(self):
        return f"{self.name}"


class ExerciseCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='no description', max_length=300)
    exercises_bank = models.ForeignKey(
        to=ExercisesBank, on_delete=models.CASCADE, related_name='exercise_categories',
        related_query_name='exercise_category'
    )

    class Meta:
        verbose_name = 'exercise category'
        verbose_name_plural = 'exercise categories'
        ordering = 'name'
        constraints = models.UniqueConstraint(
            fields=('name', 'exercises_bank')
        )

    def __str__(self):
        return f"{self.name}"


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='no description', max_length=300, unique=True)
    exercise_category = models.ForeignKey(to=ExerciseCategory, on_delete=models.CASCADE, related_name='exercise')
    instruction_link = models.URLField(blank=True)
    task_bank = models.ForeignKey(
        to=ExercisesBank, on_delete=models.CASCADE, related_name='exercises', related_query_name='exercise'
    )

    class Meta:
        verbose_name = 'exercise'
        verbose_name_plural = 'exercises'
        ordering = 'name'
        constraints = models.UniqueConstraint(
            fields=('name', 'exercise_category', 'instruction_link')
        )

    def __str__(self):
        return f"{self.name}"


class TrainingPlan(models.Model):
    class AccessStatuses(models.TextChoices):
        PRIVATE = 'PRIVATE', 'Private'
        PROTECTED = 'PROTECTED', 'Protected'
        PUBLIC = 'PUBLIC', 'Public'

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, default='no description')
    owner = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='training_plans', related_query_name='training_plan'
    )
    access_status = models.CharField(
        max_length=20, choices=AccessStatuses.choices, default=AccessStatuses.PUBLIC
    )

    class Meta:
        verbose_name = 'training plan'
        verbose_name_plural = 'training plans'
        ordering = 'name'
        constraints = models.UniqueConstraint(
            fields=('name', 'description', 'owner')
        )

    def __str__(self):
        return f"{self.name}"


class TrainingDay(models.Model):
    description = models.TextField(max_length=200, default='no description')
    training_plan = models.ForeignKey(
        to=TrainingPlan, on_delete=models.CASCADE, related_name='training_days', related_query_name='training_day'
    )
    tasks = models.ManyToManyField(
        to=Exercise, through='DailyExercise', related_name='training_days', related_query_name='training_day'
    )
    order = models.PositiveSmallIntegerField()
    # appointment_date = models.DateTimeField()
    # training_duration = models.DurationField()

    class Meta:
        verbose_name = 'training day'
        verbose_name_plural = 'training days'
        ordering = 'order'
        constraints = models.UniqueConstraint(
            fields=('training_plan', 'order')
        )

    def __str__(self):
        return f"{self.training_plan.name}, day {self.order}"


class DailyExercise(models.Model):
    exercise = models.ForeignKey(
        to=Exercise, on_delete=models.CASCADE, related_name='daily_exercises', related_query_name='daily_exercise'
    )
    day = models.ForeignKey(
        to=TrainingDay, on_delete=models.CASCADE, related_name='daily_exercises', related_query_name='daily_exercise'
    )
    repetitions = models.PositiveSmallIntegerField()
    work_weight = models.PositiveSmallIntegerField(blank=True, null=True)
    order = models.CharField()

    class Meta:
        verbose_name = 'daily exercise'
        verbose_name_plural = 'daily exercises'
        ordering = 'order'

    def __str__(self):
        return f"Day {self.day.order}, {self.exercise.name}"
