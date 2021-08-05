from django.db import models

# Create your models here.

# step1: Making a model for a database of table
# step2: Making migrations for publishing a flight model of table
# step3: Making migrate for creating db of table from model into database

# check inside of django shell: using python manage.py shell
# Access to Flight model: from flights.models(appname.model) import Flight(modelname)
# Insert data: f = Flight(origin="New York", destination="London", duration=415), f.save()


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    # 異なるテーブル,親と子のテーブルを「１対多」の関係で結びつけることができる
    # on_deleteは親テーブルのデータが削除されると連動して子テーブルのデータも削除される
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destinations = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # call instance obj of __str_ method to return string object
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destinations}"

    # Check that origin and duration is the same as destination and greater than 0
    def is_valid_flight(self):
        return self.origin != self.destinations or self.duration >= 0


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
