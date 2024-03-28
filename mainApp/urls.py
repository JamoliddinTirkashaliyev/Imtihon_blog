from django.urls import path
from .views import *

urlpatterns = [

    path('muallif/', MuallifView.as_view(), name='muallif'),
    path('maqola/', MaqolaView.as_view(), name='maqola'),
]
