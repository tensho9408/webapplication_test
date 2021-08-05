from django.shortcuts import render, reverse
from .models import Flight, Passenger
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    print(flight)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()

    })


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        # 乗客情報の氏名を取得
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # 乗客情報を搭乗名簿に追加する
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))
