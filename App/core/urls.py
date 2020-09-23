from django.urls import path
from App.core.views import *

app_name = 'App.core'

urlpatterns = [
    path('prueba/', PaisesListView.as_view(), name='pais_list'),

]