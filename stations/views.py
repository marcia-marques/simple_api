from rest_framework import viewsets, permissions
from .models import Station
from .serializers import StationSerializer


class StationView(viewsets.ReadOnlyModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = [permissions.AllowAny]
