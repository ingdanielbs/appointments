from .models import Specialty
from rest_framework import permissions, viewsets
from .serializers import SpecialtySerializer

class SpecialtyViewSet(viewsets.ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [permissions.AllowAny]