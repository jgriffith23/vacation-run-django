from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    """How users log their runs/biking sessions/etc."""

    activity = forms.Select()
    calories = forms.IntegerField()

    # Will need to populate this with user's events, if any
    evt = forms.Select()

    date = forms.SplitDateTimeWidget()

    distance = forms.FloatField()

    duration = forms.TimeInput()

    class Meta:
        model = Workout
        fields = ('activity',
                  'calories',
                  'evt',
                  'date',
                  'distance',
                  'duration',
        )
