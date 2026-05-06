from xml.etree.ElementInclude import include

from django.urls import path

from articles.views import home
from blog import settings

urlpatterns = [
    path ('', home , name='articles'), 
]

