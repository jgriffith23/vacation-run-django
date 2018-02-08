from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFit

###################
# Generic Concepts
###################

class Activity(models.Model):
    """A category of exercise. To be associated with workouts."""

    act_code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=64, null=False, blank=False)
    icon = models.ImageField(
        null=True,
        blank=True,
        upload_to='activities',
    )

    icon_display = ImageSpecField(
        source='photo',
        processors=[ResizeToFit(100, 100)],
        format='PNG',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f"{self.name}"


class State(models.Model):
    """A state. To be associated with events and users."""

    state_code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} ({self.state_code})"

    class Meta:
        ordering = ('name',)


###############
# User-Created
###############

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

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Event(models.Model):
    """An event where users can work out on a specific day."""

    added_by = models.ForeignKey(
        Exerciser,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="creator+"
    )

    title = models.CharField(max_length=64, null=False, blank=False)
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64, null=False, blank=False)
    zip = models.CharField(max_length=5)
    url = models.CharField(max_length=256, null=True, blank=True)
    date = models.DateTimeField(null=False, blank=False)
    notes = models.TextField(null=True, blank=True)

    state = models.ForeignKey(
        State,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )

    exercisers = models.ManyToManyField(Exerciser, blank=True)

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%B %Y')})"


class Team(models.Model):
    """A group of people working together toward a vacation."""

    name = models.CharField(max_length=128, null=False, blank=False)
    captain = models.ForeignKey(
        Exerciser,
        null=False,
        on_delete=models.CASCADE,
        related_name="captain",
    )

    exercisers = models.ManyToManyField(Exerciser)

    def __str__(self):
        return f"{self.name}"


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

    exerciser = models.ForeignKey(
        Exerciser,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return f"{self.activity.name} ({self.date.strftime('%A, %B %d, %Y')})"




