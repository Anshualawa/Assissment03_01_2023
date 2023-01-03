from rest_framework import serializers
from myapp.models import*

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = productMainModel
        fields='__all__'