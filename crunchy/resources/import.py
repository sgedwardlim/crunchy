import sys, os, django
sys.path.append("C:/Users/Didar Bhullar/PycharmProjects/crunchy/crunchy") #here store is root folder(means parent).
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crunchy.settings")
django.setup()

from hotels.models import Hotel
import csv



with open('hotel_db.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # The header row values become your keys

        name = row['Name']
        city = row['City']
        address = row['Address']
        phone = row['Phone']
        rating = row['Rating']
        price = row['Price']
        images = row['Photo Urls']

        new_hotel = Hotel(name = name, city= city, address= address, phone = phone, rating = rating, price = price,
                          images = images)
        new_hotel.save()