from rest_framework import serializers
from turfapp.models import TurfDB, BookingDB

class TurfSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurfDB
        fields = '__all__'
        read_only_fields = ['id']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingDB
        fields = '__all__'
        read_only_fields = [
            'id',
            'total_amount',
            'status',
            'created_at'
        ]

