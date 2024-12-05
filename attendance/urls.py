from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('attendants', views.attendants, name='attendants'),
    path('save_attendant', views.save_attendant, name='save'),
]