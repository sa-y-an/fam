from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ParentSerializer, ChildSerializer
from django.shortcuts import get_object_or_404
from .models import Parent, Children

# Create your views here.
class ParentList(viewsets.ModelViewSet):
    serializer_class = ParentSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Parent, pk=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Parent.objects.all()


class ChildrenList(viewsets.ModelViewSet):
    serializer_class = ChildSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Children, pk=item)

    # Define Custom Queryset
    def get_queryset(self):
        return Children.objects.all()