from django.shortcuts import get_object_or_404
from turfapp.models import TurfDB, BookingDB
from turfapp.serializers import TurfSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


# Class for listing and creating turfs
class TurfListCreateView(APIView):

    def get(self, request):
        qs = TurfDB.objects.all()
        serializer_instance = TurfSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = TurfSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)

        return Response(serializer_instance.errors)


# Class for retrieving, updating and deleting a turf
class TurfRetrieveUpdateDeleteView(APIView):

    def get(self, request, pk):
        qs = get_object_or_404(TurfDB, pk=id)
        serializer_instance = TurfSerializer(TurfDB,qs)
        return Response(serializer_instance.data)

    def put(self, request, pk):
        form_data = request.data
        turf_object = get_object_or_404(TurfDB, pk=pk)

        serializer_instance = TurfSerializer(
            turf_object,
            data=form_data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)

        return Response(serializer_instance.errors)

    def delete(self, request, pk):
        turf_object = get_object_or_404(TurfDB, pk=pk)
        turf_object.delete()

        return Response({
            "message": "Turf deleted successfully."
        })


# Class for listing and creating bookings
class BookingListCreateView(APIView):

    def get(self, request):
        qs = BookingDB.objects.all()
        serializer_instance = BookingSerializer(qs, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        form_data = request.data
        serializer_instance = BookingSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)

        return Response(serializer_instance.errors)

