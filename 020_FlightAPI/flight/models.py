from django.db import models
from django.contrib.auth.models import User


class FixModel(models.Model):
    created = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Passenger(FixModel):

    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('U', 'Undefined')
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDERS, default="U")
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Flight(FixModel):

    AIRLINES = (
        ('THY', 'Turkish Airlines'),
        ('TOST', 'Tost Airlines'),
        ('SUN', 'Sun Airlines')
    )

    CITIES = (
        (1, 'Adana'),
        (6, 'Ankara'),
        (7, 'Antalya'),
        (9, 'Aydin'),
        (10, 'Balikesir'),
        (16, 'Bursa'),
        (32, 'Isparta'),
        (34, 'Istanbul'),
        (35, 'Izmir'),
        (44, 'Malatya'),
        (52, 'Ordu'),
    )

    flight_number = models.CharField(max_length=64)
    airline = models.CharField(max_length=4, choices=AIRLINES)
    departure = models.PositiveSmallIntegerField(choices=CITIES)
    departure_date = models.DateField()
    arrival = models.PositiveSmallIntegerField(choices=CITIES)
    arrival_date = models.DateField()


    def __str__(self):
        return f'{self.flight_number} # {self.airline} {self.departure} -> {self.arrival}'

class Reservation(FixModel):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ManyToManyField(Passenger)

