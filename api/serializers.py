from rest_framework import serializers
from .models import Children, Parent


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('age', 'name','child','aadhar')
        model = Parent

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('age', 'name','aadhar')
        model = Children