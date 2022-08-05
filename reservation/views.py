from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from reservation.models import Reservation


def home(request):
    reservations = Reservation.objects.all()
    template = loader.get_template('reservation/index.html')
    context = {
        'reservations': reservations,
    }
    return HttpResponse(template.render(context, request))
