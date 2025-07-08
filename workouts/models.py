from django.db import models
from users.models import User
from django.utils.text import slugify


class ExerciseCategory(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Enter a name for this exercise category."
    )
    description = models.TextField(
        blank=True,
        default='',
        help_text="Provide an optional description for this category."
    )
    slug = models.SlugField(
        unique=True,
        help_text="Unique URL-friendly identifier for this category."
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='exercise_categories',
        related_query_name='exercise_category'
    )

    class Meta:
        verbose_name = 'ExerciseCategory'
        verbose_name_plural = 'ExerciseCategories'
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'exercises_bank'],
                name='unique_for_exercises_bank'
            )
        ]

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}")
        return super().save(*args, **kwargs)


class Exercise(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Enter the name of the exercise."
    )
    description = models.TextField(
        blank=True,
        default='',
        help_text="Provide an optional description for this exercise."
    )
    exercise_category = models.ForeignKey(
        to=ExerciseCategory,
        on_delete=models.CASCADE,
        related_name='exercises',
        related_query_name='exercise',
        help_text="Select the category this exercise belongs to."
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='exercise_categories',
        related_query_name='exercise_category'
    )
    instruction_link = models.URLField(
        blank=True,
        null=True,
        help_text="Provide a URL to instructions or a demonstration video."
    )
    slug = models.SlugField(
        unique=True,
        help_text="Unique URL-friendly identifier for this exercise."
    )

    class Meta:
        verbose_name = 'Exercise'
        verbose_name_plural = 'Exercise'
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'exercise_category', 'instruction_link'],
                name='unique_for_category'
            )
        ]

    def __str__(self):
        return f"{self.name}-{self.exercise_category.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}")
        return super().save(*args, **kwargs)


class TrainingPlan(models.Model):
    class AccessStatuses(models.TextChoices):
        PRIVATE = 'PRIVATE', 'Private'
        PROTECTED = 'PROTECTED', 'Protected'
        PUBLIC = 'PUBLIC', 'Public'

    name = models.CharField(
        max_length=100,
        help_text="Enter a name for the training plan."
    )
    description = models.TextField(
        blank=True,
        default='',
        help_text="Provide an optional description for this training plan."
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='training_plans',
        related_query_name='training_plan',
        help_text="Select the user who owns this training plan."
    )
    access_status = models.CharField(
        max_length=20,
        choices=AccessStatuses.choices,
        default=AccessStatuses.PUBLIC,
        help_text="Set the access level for this training plan."
    )
    slug = models.SlugField(
        unique=True,
        help_text="Unique URL-friendly identifier for this training plan."
    )

    class Meta:
        verbose_name = 'TrainingPlan'
        verbose_name_plural = 'TrainingPlans'
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'owner'],
                name='unique_plan_name_for_owner'
            )
        ]

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.owner.username}")
        return super().save(*args, **kwargs)


class TrainingDay(models.Model):
    description = models.TextField(
        default='',
        help_text="Provide a description for this training day."
    )
    training_plan = models.ForeignKey(
        to=TrainingPlan,
        on_delete=models.CASCADE,
        related_name='training_days',
        related_query_name='training_day',
        help_text="Select the training plan this day is part of."
    )
    tasks = models.ManyToManyField(
        to=Exercise,
        through='DailyExercise',
        related_name='training_days',
        related_query_name='training_day',
        help_text="Exercises scheduled for this training day."
    )
    order = models.PositiveSmallIntegerField(
        help_text="Specify the sequence order of this training day."
    )
    slug = models.SlugField(
        unique=True,
        help_text="Unique URL-friendly identifier for this training day."
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='exercise_categories',
        related_query_name='exercise_category'
    )

    class Meta:
        verbose_name = 'TrainingDay'
        verbose_name_plural = 'TrainingDays'
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(
                fields=['training_plan', 'order'],
                name='unique_for_training_plan'
            )
        ]

    def __str__(self):
        return f"{self.training_plan.name}, day {self.order}"

    def __lt__(self, other):
        if not isinstance(other, TrainingDay):
            return NotImplemented
        return self.order < other.order

    def __gt__(self, other):
        if not isinstance(other, TrainingDay):
            return NotImplemented
        return self.order > other.order

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.training_plan.name}-{self.order}day")
        return super().save(*args, **kwargs)


class DailyExercise(models.Model):
    exercise = models.ForeignKey(
        to=Exercise,
        on_delete=models.CASCADE,
        related_name='daily_exercises',
        related_query_name='daily_exercise',
        help_text="Select the exercise for this daily entry."
    )
    day = models.ForeignKey(
        to=TrainingDay,
        on_delete=models.CASCADE,
        related_name='daily_exercises',
        related_query_name='daily_exercise',
        help_text="Select the training day this exercise is scheduled for."
    )
    repetitions = models.PositiveSmallIntegerField(
        help_text="Number of repetitions for this exercise."
    )
    work_weight = models.DecimalField(
        blank=True,
        null=True,
        max_digits=3,
        decimal_places=2,
        help_text="Planned weight to be used for this exercise."
    )
    actual_used_weight = models.DecimalField(
        blank=True,
        null=True,
        max_digits=3,
        decimal_places=2,
        help_text="Actual weight used during the exercise."
    )
    order = models.PositiveSmallIntegerField(
        help_text="Specify the sequence order of this exercise within the day."
    )

    class Meta:
        verbose_name = 'DailyExercise'
        verbose_name_plural = 'DailyExercises'
        ordering = ['order']

    def __str__(self):
        return f"Day {self.day.order}, {self.exercise.name}"

    def __lt__(self, other):
        if not isinstance(other, DailyExercise):
            return NotImplemented
        return self.order < other.order

    def __gt__(self, other):
        if not isinstance(other, DailyExercise):
            return NotImplemented
        return self.order > other.order
