from django.urls import path
from . import views

urlpatterns = [
    path('',views.StatusListAPIView.as_view()),
    path('create/', views.StatusCreateAPIView.as_view())

]