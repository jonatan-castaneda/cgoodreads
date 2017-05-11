from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token,refresh_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^authors/', include("modules.authors.urls")),
    url(r'^books/', include("modules.books.urls")),
    url(r'^auth/', obtain_jwt_token),
    url(r'^auth/refresh/', refresh_jwt_token),
    url(r'^auth/verify/', verify_jwt_token),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^docs/', schema_view),
]