from django.urls import path
from api import views
urlpatterns=[
    path('comp/',views.ComputerListAPIView.as_view())
]