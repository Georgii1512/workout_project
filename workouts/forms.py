from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import (
    ExerciseCategory,
    Exercise,
    TrainingPlan,
    TrainingDay,
    DailyExercise,
)


class ExerciseCategoryForm(ModelForm):
    class Meta:
        model = ExerciseCategory
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'exercise_category', 'instruction_link']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class TrainingPlanForm(ModelForm):
    class Meta:
        model = TrainingPlan
        fields = ['name', 'description', 'access_status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class TrainingDayForm(ModelForm):
    class Meta:
        model = TrainingDay
        fields = ['description', 'order']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class DailyExerciseForm(ModelForm):
    class Meta:
        model = DailyExercise
        fields = ['exercise', 'repeats', 'work_weight', 'actual_used_weight', 'order']
        widgets = {
            'work_weight': forms.NumberInput(attrs={'step': '1', 'min': '0'}),
            'actual_used_weight': forms.NumberInput(attrs={'step': '1', 'min': '0'}),
        }


# formsets
# TrainingDayFormset = inlineformset_factory(TrainingPlan,
#                                            TrainingDay,
#                                            TrainingDayForm,
#                                            can_delete=True,
#                                            extra=1
#                                            )
#
# DailyExerciseFormset = inlineformset_factory(TrainingDay,
#                                              DailyExercise,
#                                              can_delete=True,
#                                              extra=1
#                                              )
#
# ExerciseFormset = inlineformset_factory(
#     ExercisesBank,
#     Exercise,
#     can_delete=True,
#     extra=1
# )
