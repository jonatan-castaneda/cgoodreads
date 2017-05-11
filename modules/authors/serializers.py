from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("__all__") #('id', 'nombre', 'apellidos')

class AuthorExampleSerializer(serializers.Serializer):
    nombre = serializers.CharField