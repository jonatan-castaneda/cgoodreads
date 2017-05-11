from rest_framework import serializers
from .models import Book, Comments
from modules.authors.serializers import AuthorSerializer
from modules.users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        user = UserSerializer(read_only=True)
        model = Comments
        fields = ("user","comentario")

class BookSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ("rating",)

class BookSerializer1(serializers.ModelSerializer):
    author_name = serializers.CharField(source="autor.nombre")
    author_lastname = serializers.CharField(source="autor.apellidos")
    class Meta:
        model = Book
        #exclude = ("rating",)
        fields = ("id", "nombre", "descripcion", "isbn", "author_name", "author_lastname")

class BookSerializer3(serializers.ModelSerializer):
    autor = AuthorSerializer(read_only = True) #tiene que ser en nombre de la llave foranea en el modelo
    class Meta:
        model = Book
        #exclude = ("rating",)
        fields = ("id", "nombre", "descripcion", "isbn", "autor")

class BookSerializer(serializers.ModelSerializer):
    comentarios = CommentSerializer(read_only = True, many=True) #tiene que ser en nombre de la llave foranea en el modelo
    class Meta:
        model = Book
        #exclude = ("rating",)
        fields = ("id", "nombre", "descripcion", "isbn", "comentarios","autor")