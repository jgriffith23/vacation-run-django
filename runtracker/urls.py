from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="home"),
    url(r'^workouts', views.WorkoutListView.as_view(), name="workout_list"),
]