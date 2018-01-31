from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from runtracker.models import Workout

class HomePageView(generic.TemplateView):
    template_name = "runtracker/home.html"

class WorkoutListView(LoginRequiredMixin, generic.ListView):
    """An exerciser's logged workouts. Only viewable by authenticated users."""

    template_name = "runtracker/workout_list.html"

    def get_queryset(self):
        print(self.request.user.exerciser)
        return Workout.objects.all().filter(exerciser_id=self.request.user.exerciser)

