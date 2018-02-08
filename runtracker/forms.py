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

        fields = (
            "activity",
            "calories",
            "event",
            "date",
            "distance",
            "duration",
        )

        widgets = {
            "calories": forms.IntegerField(),
            "date": forms.DateTimeInput(format="%d/%m/%Y"),
            "distance": forms.FloatField(),
            "duration": forms.TimeInput(format="%H:%M:%S"),
        }
