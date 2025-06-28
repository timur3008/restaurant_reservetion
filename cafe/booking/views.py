from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactUsForm, BookingForm
from .models import ContactUs, Booking

class HomePageView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'booking/index.html'

    def get_success_url(self):
        return reverse_lazy('home_page')

class ReservationPageView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/reservation.html'

    def get_success_url(self):
        return reverse_lazy('home_page')