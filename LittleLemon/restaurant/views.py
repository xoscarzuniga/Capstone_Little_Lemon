from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Booking, Menu
from .serializers import BookingSerializer, menuSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html', {})

#@api_view
class MenuItemView(generics.ListCreateAPIView):
    permission_classes= [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

#@api_view
#@permission_classes([IsAuthenticated])
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

#@api_view
#@permission_classes([IsAuthenticated])
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    #permission_classes = [permissions.IsAutehtnicated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def msg(request):
    return HttpResponse({"message": "This view is protected"})