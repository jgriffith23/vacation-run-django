from django.contrib import admin
from .models import (
    Activity,
    State,
    Event,
    Exerciser,
    Team,
    Workout,
)

admin.site.register(Activity)
admin.site.register(State)
admin.site.register(Event)
admin.site.register(Exerciser)
admin.site.register(Team)
admin.site.register(Workout)