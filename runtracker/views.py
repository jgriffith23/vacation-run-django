from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from runtracker.models import Workout
from runtracker.forms import WorkoutForm


class HomePageView(generic.TemplateView):
    template_name = "runtracker/home.html"

class WorkoutListView(LoginRequiredMixin, generic.ListView):
    """An exerciser's logged workouts. Only viewable by authenticated users."""

    form_class = WorkoutForm

    template_name = "runtracker/workout_list.html"

    context_object_name = "workouts"

    def get_queryset(self):
        print(self.request.user.exerciser)
        return Workout.objects.all().filter(exerciser=self.request.user.exerciser)

    def get_context_data(self, **kwargs):
        context = super(WorkoutListView, self).get_context_data(**kwargs)
        context['form'] = WorkoutForm()
        return context