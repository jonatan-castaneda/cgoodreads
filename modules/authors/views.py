from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Author
from .serializers import AuthorSerializer
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ListAuthor(APIView):

    permission_classes = (TokenHasReadWriteScope,IsAuthenticated)

    def get(self, request):
        autores = Author.objects.all()
        serializer = AuthorSerializer(autores, many=True) #Trae todos los autores
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailAuthor(APIView):
    def get(self, request, pk):
        try:
            autor = Author.objects.get(id=pk)
        except Exception:
            raise Http404
        serializar = AuthorSerializer(autor)
        return Response(serializar.data, status = status.HTTP_200_OK)

    def put(self, request):
        pass

    def delete(self, request):
        pass