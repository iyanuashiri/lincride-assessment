from django.urls import path

from rest_framework.schemas import get_schema_view

from . import views


schema_view = get_schema_view(title='Rides API')


app_name = 'rides'
urlpatterns = [
    path('calculate-fare/', views.CalculateFareAPIView.as_view()),
]