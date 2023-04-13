
from rest_framework import viewsets
from .serializers import *


# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch', 'put', 'post']

    # django filters fields
    filterset_fields = []
    search_fields = ['id']
    ordering_fields = []
    ordering = ['-id']