from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from bookings.models import Booking
from datetime import datetime
from hotels.models import Hotel
from bookings.models import RewardPoint
from django.contrib import messages
import datetime

# from ..bookings.models import Booking
# Create your views here.
def reservations(request):
    return render(request, 'viewer/reservations.html')

def previous(request):
    user = request.user
    booking = Booking.objects.filter(user_id=user.id)

    today_min = datetime.datetime.combine(datetime.date(2017, 1, 1), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date(2017, 12, 3), datetime.time.max)
    bookings = Booking.objects.filter(check_in_date__range=(today_min, today_max))

    context = {
        'user': user,
        'bookings': bookings,
    'booking' : booking

    }
    return render(request, 'viewer/previous.html', context)

def upcoming(request):
    user = request.user
    booking = Booking.objects.filter(user_id=user.id)


    today_min = datetime.datetime.combine(datetime.date(2017, 12, 4), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date(2018, 12, 30), datetime.time.max)
    bookings = Booking.objects.filter(check_in_date__range=(today_min, today_max))

    context = {
        'user': user,
        'bookings': bookings,
        'booking' : booking
    }
    return render(request, 'viewer/upcoming.html', context)

def delete(request, booking_id):
    print('booking id: ' + booking_id)
    booking = Booking.objects.get(pk=booking_id)
    # if request.method == "POST":
    Booking.objects.get(id=booking_id).delete()
    hotel = Hotel.objects.get(pk=booking.hotel_id)
    delete_points = float(hotel.price) * .10

    rp_object = RewardPoint.objects.get(user=request.user)
    current_points = rp_object.reward_points
    total_points = int(current_points - delete_points)

    rp_object.reward_points = total_points
    rp_object.save()

    return redirect('/viewer/upcoming')
