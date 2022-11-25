from django.urls import path

from galeria.views import carinanebula, smacs, index, stephan

urlpatterns = [
    path ('', index, name='index'),
    path('carinanebula/', carinanebula, name='carinanebula'),
    path('smacs/', smacs, name='smacs' ),
    path('stephan/', stephan, name ='stephan')
]