from django.shortcuts import render
from rest_framework import generics, filters, status
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from django.conf import settings


# Create your views here.

class ListBook(generics.ListCreateAPIView):

    #permission_classes = (IsAuthenticated,)

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend)
    filter_fields = ("nombre","isbn","autor","genero",)
    search_fields = ("nombre","isbn","descripcion")


class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UploadFiles(APIView):
    parser_classes = (FormParser, MultiPartParser)

    def handle_uploaded_file(self, f):
        path = "%s/%s" % (settings.MEDIA_ROOT, str(f))
        print (path)
        with open(path, 'wb+') as destination:
            for chunk in f.chunks():    
                destination.write(chunk)

    def post(self,request):
        try:
            self.handle_uploaded_file(request.FILES['file'])
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_200_OK)

    