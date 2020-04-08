from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_home, name='workout_home'),
    path('list', views.workout_list, name='workout_list')
]