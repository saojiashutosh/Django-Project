from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.index, name='Index'),  # Root path of the app
]
