'''

from django.urls import path
from .views import display_data

urlpatterns = [
    path('display_data/', display_data, name='display_data'),
]
'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_data, name='data'),

]
