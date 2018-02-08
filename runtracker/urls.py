from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="home"),
    url(r'^dashboard', views.DashboardView.as_view(), name="dashboard"),
]