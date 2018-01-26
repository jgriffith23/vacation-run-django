from django.db import models
from django.contrib.auth.models import User

###################
# Generic Concepts
###################

class Activity(models.Model):
    """A category of exercise. To be associated with workouts."""

    act_code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=64, null=False, blank=False)
    icon = models.ImageField()

    class Meta:
        ordering = ('name',)


class State(models.Model):
    """A state. To be associated with events and users."""

    state_code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=30)


class Event(models.Model):
    """An event where users can work out on a specific day."""

    title = models.CharField(max_length=64, null=False, blank=False)
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64, null=False, blank=False)
    zip = models.CharField(max_length=5)
    date = models.DateTimeField(null=False, blank=False)
    notes = models.TextField()

    state = models.ForeignKey(
        State,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )

    users = models.ManyToManyField(User)

    class Meta:
        ordering = ('date',)


#############
# User-Owned
#############

class Exerciser(models.Model):
    """Profile information for a user, decoupled from auth info."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    email = models.EmailField(null=False, blank=False)
    fname = models.CharField(max_length=64, null=False, blank=False)
    lname = models.CharField(max_length=64, null=False, blank=False)
    phone = models.CharField(max_length=16, null=False, blank=False)
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    zip = models.CharField(max_length=5)

    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)


class Team(models.Model):
    """A group of people working together toward a vacation."""

    name = models.CharField(max_length=128, null=False, blank=False)
    captain = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE,
        related_name="captain+",
    )

    users = models.ManyToManyField(User)


class Workout(models.Model):
    """A single workout that a user has done."""

    activity = models.ForeignKey(
        Activity,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    calories = models.IntegerField()

    event = models.ForeignKey(
        Event,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    date = models.DateTimeField(null=False, blank=False)

    # Stored in meters, though user may input miles for form

    distance = models.FloatField(null=False, blank=False)
    duration = models.DurationField(null=False, blank=False)

    user = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('date',)




