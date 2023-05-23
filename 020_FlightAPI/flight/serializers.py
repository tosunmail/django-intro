from rest_framework import serializers
from .models import (Passenger,Flight,Reservation)


class FixSerializer(serializers.Serializer):

    created = serializers.StringRelatedField()
    created_id = serializers.IntegerField(required=False, write_only=True)

    def create(self, validated_data):
        validated_data['created_id'] = self.context['request'].user.id
        return super().create(validated_data)


class PassengerSerializer(FixSerializer):

    class Meta:
        model = Passenger
        exclude = []


class FlightSerializer(FixSerializer):

    departure_text = serializers.SerializerMethodField()
    arrival_text = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        exclude = []


class ReservationSerializer(FixSerializer):

    class Meta:
        model = Reservation
        exclude = []