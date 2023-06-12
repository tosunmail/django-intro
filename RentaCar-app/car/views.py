from rest_framework.viewsets import ModelViewSet

from .serializers import (
    Car, CarSerializer,Reservation,ReservationSerializer
)


class FixView(ModelViewSet):
    pass

class CarView(FixView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ReservationView(FixView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer