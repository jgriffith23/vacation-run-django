from django.views import generic
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from runtracker.models import Workout, Event
from runtracker.forms import WorkoutForm


class HomePageView(generic.TemplateView):
    template_name = "runtracker/home.html"

class DashboardView(LoginRequiredMixin, generic.ListView):
    """An exerciser's logged workouts. Only viewable by authenticated users."""

    form_class = WorkoutForm

    template_name = "runtracker/dashboard.html"

    context_object_name = "actions"

    def get_queryset(self):
        print(self.request.user.exerciser)

        workouts = Workout.objects.all().filter(
            exerciser=self.request.user.exerciser
        )

        events = Event.objects.all().filter(
            exercisers=self.request.user.exerciser,
            date__gte=datetime.now(),
        )
        return {"workouts": workouts, "events": events}

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['form'] = WorkoutForm()
        return context