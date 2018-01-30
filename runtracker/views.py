from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(generic.TemplateView):
    template_name = "runtracker/home.html"

class WorkoutListView(LoginRequiredMixin, generic.ListView):
    """An exerciser's logged workouts. Only viewable by authenticated users."""



