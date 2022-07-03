import imp
from django.urls import path
from .views import VocListCreateAPIView,VocDetailAPIView

urlpatterns = [
    path('',VocListCreateAPIView.as_view()),
    path('<int:pk>/',VocDetailAPIView.as_view())
]
