from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from modules.authors.models import Author 
import json 

# Create your tests here.

class BookListTest(APITestCase):

    def setUp(self):
        self.author = Author()
        self.author.nombre = "Un autor"
        self.author.apellidos = "apellidos"
        self.author.nacionalidad = "Mexicana"
        self.author.biografia = ""
        self.author.sexo = "M"
        self.author.edad = 67
        self.author.save()

        self.book = {
            "nombre":"Un libro",
            "isbn":"124134145",
            "autor":self.author.id,
            "fecha_pub":"2017-01-01",
            "descripcion":"jsdlkvjfvjafdj",
            "rating":0.90,
            "genero":"TR"
        }
        self.url = reverse('list-books')#nombre de la url de referencia

    def test_list_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_books(self):
        response = self.client.post(self.url, self.book, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class BookDetailTest(APITestCase):

    def setUp(self):
        self.author = Author()
        self.author.nombre = "Un autor"
        self.author.apellidos = "apellidos"
        self.author.nacionalidad = "Mexicana"
        self.author.biografia = "vhgvdfhfgjfgdj"
        self.author.sexo = "M"
        self.author.edad = 67
        self.author.save()

        self.book = Book(nombre="Un Libro",
            autor = self.author, isbn = "213435245",
            fecha_pub = "2017-01-01",
            descripcion = "faskjgnajgk", genero = "TR",
            rating = 0.0)
        self.book.save()

        self.url = reverse('detail-books', args=[self.book.id])

    def test_retrieve_book(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_book(self):
        self.data = {
            "nombre":"Un libro",
            "isbn":"124134145",
            "autor":self.author.id,
            "fecha_pub":"2017-01-01",
            "descripcion":"bcshcshvshkfjk",
            "rating":0.90,
            "genero":"TR"
        }
        response = self.client.put(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #self.assertEqual(response.data, self.data)
    
    def test_destroy_book(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)