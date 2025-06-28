from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name="home_page"),
    path('reservation/', views.ReservationPageView.as_view(), name='booking_page')
]