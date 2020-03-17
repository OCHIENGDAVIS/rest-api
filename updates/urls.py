from django.urls import path
from .views import updateTest, UpdateView, SerialisedListAPIView, SerialisedDetailAPIView

urlpatterns = [
    path('test/', updateTest),
    path('test/class-based', UpdateView.as_view()),
    path('test/class-based/list/', SerialisedListAPIView.as_view()),
    path('test/class-based/1/', SerialisedDetailAPIView.as_view()),

]